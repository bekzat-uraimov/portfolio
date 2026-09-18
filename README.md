# portfolio

My personal site. One page, no build step — Flask serves a single self-contained template.

**Live:** https://bekzat.dev

## Stack

- Flask 3 — serves the page, the crawler files, and a branded 404
- Vanilla JS — theme toggle, scroll reveal, project filter, count-up stats
- Vercel — hosting, zero-config Flask detection

The page carries its own CSS, JS, and hero image inline. No bundler, no CDN scripts, no runtime API calls.

## Run locally

```
pip install -r requirements.txt
python app.py
```

Open http://localhost:5050.

## Routes

| Route | Purpose |
|---|---|
| `/` | The page. |
| `/robots.txt`, `/sitemap.xml` | Served from `static/` at the root, where crawlers look. |
| `/static/*` | `og.png`, `apple-touch-icon.png`. Cached 24h. |
| anything else | Branded 404 (`templates/404.html`). |

No environment variables. No external services.

## Deploy (Vercel)

Vercel auto-detects the Flask `app` instance in `app.py` at the repo root and routes
everything to it. No `vercel.json`, no `api/` wrapper, no Procfile, no gunicorn.

1. Push to GitHub.
2. vercel.com → New Project → import the repo.
3. Deploy.

## Project structure

```
.
├── static/
│   ├── og.png                 # 1200x630 social card
│   ├── apple-touch-icon.png
│   ├── robots.txt
│   └── sitemap.xml
├── templates/
│   ├── index.html             # the whole site
│   └── 404.html
├── app.py
├── requirements.txt
└── README.md
```

## License

MIT.
