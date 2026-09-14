# CAA Campaign Intelligence (Render)

Password-protected Flask app for sharing CAA campaign report summaries (May–August 2026)
with an embedded campaign chat assistant.

## Local run

```bash
cd campaign-reporting
python -m venv .venv
.venv\Scripts\activate          # mac/linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env          # set APP_PASSWORD + ANTHROPIC_API_KEY
python app.py
```

Open http://localhost:5000 — default username `caa` (password from env).

## What’s included

- Executive overview + campaign calendar / month story
- Monthly summary HTML archive under `All Campaigns/`
- Supporting August reports (Fireworks, Vape Loyalty, FoodToGo, Bagel Coffee Combo)
- Floating **Ask CAA AI** chat (Anthropic when `ANTHROPIC_API_KEY` is set; rule-based fallback otherwise)

## Render

`render.yaml` deploys from branch `main`. Set these as **secret** env vars in the Render dashboard (do not commit them):

- `APP_PASSWORD`
- `ANTHROPIC_API_KEY`

Health check: `GET /api/healthcheck`
