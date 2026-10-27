#!/usr/bin/env python3
"""Count demand for a topic on Qiita before writing about it (no AI, public API only).

Usage: python3 count_demand.py TAG WORD [WORD ...] [--since YYYY-MM-DD]
Example: python3 count_demand.py ClaudeCode トークン キャッシュ コスト --since 2026-08-27

For each WORD it finds articles tagged TAG whose title contains WORD, and prints how many
there are, the median LGTM (likes), how many have >=5 and >=10, and the maximum.
Unauthenticated Qiita API v2 allows 60 requests/hour; this uses one request per word.
"""
import json, statistics, sys, time, urllib.parse, urllib.request


def fetch(query):
    url = "https://qiita.com/api/v2/items?per_page=100&query=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={"User-Agent": "count_demand/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main(argv):
    since = "2026-01-01"
    if "--since" in argv:
        i = argv.index("--since")
        since = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 2:
        print(__doc__)
        return 2
    tag, words = argv[0], argv[1:]
    print(f"tag={tag} since={since}")
    print("word\tn\tmedian\t>=5\t>=10\tmax")
    for w in words:
        items = fetch(f"tag:{tag} title:{w} created:>{since}")
        likes = sorted(i["likes_count"] for i in items)
        if not likes:
            print(f"{w}\t0\t-\t-\t-\t-")
        else:
            print(f"{w}\t{len(likes)}\t{statistics.median(likes)}\t"
                  f"{sum(x >= 5 for x in likes)}\t{sum(x >= 10 for x in likes)}\t{likes[-1]}")
        time.sleep(1.5)  # be polite
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
