# portfolio

My personal site. Flask backend, single-page frontend, projects pulled live from the GitHub API. Deployed on Vercel.

**Live:** https://bekzat.dev

<img width="1501" height="784" alt="home" src="https://github.com/user-attachments/assets/4d41b86c-f099-410c-b564-dd2735e28a04" />


## Stack

- Flask 3 — routes and the cached GitHub proxy
- Vanilla JS — typed hero, dark mode toggle, project loader
- GitHub GraphQL API — real pinned repos when a token is set
- Vercel — hosting (serverless, no cold-sleep)

## Run locally

```
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Configuration

Two env vars control the Projects section. Both are optional but you want one of them — otherwise the section is empty.

| Var | Purpose |
|---|---|
| `GITHUB_USER` | Defaults to `bekzat-uraimov`. |
| `GITHUB_TOKEN` | Fine-grained personal access token with read access to public repos. When set, the site shows your real pinned repos via GraphQL. |
| `GITHUB_PINNED` | Comma-separated repo names, e.g. `HabitTrackerBot,Poly_Predictor_Kit`. Used when no token is set. |

Selection order: `GITHUB_TOKEN` (real pinned) → `GITHUB_PINNED` (manual list) → empty.

Local example:

```
export GITHUB_USER=your-handle
export GITHUB_TOKEN=ghp_xxx
python app.py
```

## Deploy (Vercel)

The repo is already wired for Vercel: `vercel.json` rewrites all traffic to `api/index.py`, which imports the Flask app. No Procfile, no gunicorn.

1. Push to GitHub.
2. vercel.com → New Project → import the repo.
3. Add env vars: `GITHUB_USER`, `GITHUB_TOKEN`.
4. Deploy. First build is ~30s.

## Project structure

```
.
├── api/
│   └── index.py       # Vercel entry — imports app:app
├── static/
│   ├── css/style.css
│   └── js/script.js
├── templates/
│   └── index.html
├── app.py             # Flask routes + GitHub fetch
├── requirements.txt
├── vercel.json
└── README.md
```

## License

MIT.
