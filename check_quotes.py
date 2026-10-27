#!/usr/bin/env python3
"""Check that every quoted phrase in a draft really appears in a source text (no AI).

Usage: python3 check_quotes.py DRAFT.md SOURCE.txt
A "quote" is any text inside 「 」 or "double quotes" in the draft. Whitespace is ignored when
matching. Prints each quote that is NOT found in the source and exits 1 if there is any.
Why: AI-written drafts tend to turn a paraphrase into a quotation ("saying too much").
This only checks that the words exist in the source, not that they are used fairly.
"""
import re, sys


def norm(s):
    return re.sub(r"\s+", "", s)


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    draft = open(argv[0], encoding="utf-8").read()
    source = norm(open(argv[1], encoding="utf-8").read())
    quotes = re.findall(r"「([^」]+)」", draft) + re.findall(r'"([^"\n]+)"', draft)
    missing = [q for q in quotes if norm(q) not in source]
    for q in missing:
        print("NOT IN SOURCE:", q)
    print(f"quotes={len(quotes)} found={len(quotes) - len(missing)} missing={len(missing)}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
