# zdna0x_com

Small tools for counting before writing. No AI inside; they use public pages and APIs only.

| file | what it does |
|---|---|
| `count_demand.py` | Before writing about a topic, count how well similar Qiita titles do (likes). |
| `check_quotes.py` | Check that each quoted phrase in a draft exists in a source text. |
| `templates/prediction_ledger.csv` | Write the prediction, the stop condition and the check date *before* publishing; fill the result and the miss reason (topic / place / price) afterwards. |
| `data/` | Numbers collected with the tools. Each file says what was counted and when. |

Method: hypothesis -> prediction with a stop condition -> publish -> count -> record why it missed.
Numbers are counts of likes/views, not of sales. Sales so far: 0.

Python 3 standard library only.

Status: `check_quotes.py` and the statistics in `count_demand.py` were tested offline with sample data.
The live Qiita API call has been verified with `curl` (HTTP 200) but not yet end to end with this script.
