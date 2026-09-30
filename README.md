# deal-screen

One command → a first-pass diligence brief for an early-stage company, from its public website.

```bash
pip install -r requirements.txt
python screen.py https://www.zeroeyes.com
```

Output lands in `briefs/<domain>.md`:

- What they build
- Sector and category
- Stage signals (customers, contracts, hiring, certifications)
- Claimed technical advantage, each claim tagged **verifiable from site** or **unverified marketing**
- Risks and open questions
- Five founder questions specific to the company
- Screen verdict: PASS / LOOK CLOSER / PRIORITY

## Why

Sourcing at a small fund means looking at a lot of companies quickly. Most of the first 20 minutes on any
company is the same: read the site, work out what they actually sell, note what's claimed versus shown,
write down the questions. This automates that pass so the human time goes to the questions.

## How it works

1. Fetches the homepage plus the usual `about`, `product`, `technology`, `careers`, `team`, `news` paths (override with `--pages`).
2. Strips nav, footer, scripts; caps at 60k characters.
3. Sends the text to Claude through the `claude` CLI with a fixed brief template. The prompt forces
   "not stated" where the site is silent, so the output doesn't invent traction.
4. Writes markdown you can drop into a deal memo or CRM note.

## Examples

See `briefs/` for runs on companies in the AI / aerospace / defense lane.

## Limits

Public site only; no Crunchbase, PitchBook, or filings. JS-heavy sites may return little text.
The verdict is a screen, not a view.

## Next

- Batch mode from a CSV of URLs
- Pull open roles from the careers page as a hiring-velocity signal
- Cross-check named customers against news search

Built by Arjan Singh (UVA McIntire, Class of 2029). Python + Claude Code.
