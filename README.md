# portfolio

Personal site for [@bekzat-uraimov](https://github.com/bekzat-uraimov). Flask + a single page that pulls projects live from the GitHub API.

## Run locally

```
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Configuration

Three optional env vars control which projects show up:

- `GITHUB_USER` — defaults to `bekzat-uraimov`.
- `GITHUB_TOKEN` — a personal access token. When set, the projects section pulls your **actual pinned repos** via GitHub's GraphQL API. Without it, falls back to REST. Use a fine-grained token with read-only access to public repos.
- `GITHUB_PINNED` — comma-separated repo names (e.g. `HabitTrackerBot,Poly_Predictor_Kit,AI_Visual_Novel_Creator`). Used as a manual override when no token is set, or as a way to feature specific repos that aren't actually pinned on your profile.

Selection order: token → GraphQL pinned. Else if `GITHUB_PINNED` set → those by name. Else all public repos sorted by recently updated.

```
export GITHUB_USER=your-handle
export GITHUB_TOKEN=ghp_xxx
python app.py
```

## What's in here

- `app.py` — Flask routes plus an in-memory cached proxy for the GitHub API
- `templates/index.html` — single page (hero, about, projects, contact)
- `static/css/style.css` — minimal black/white with one accent
- `static/js/script.js` — typed hero subtitle, dark mode toggle, copy-email, project loader

## Deploy

Any platform that runs Flask works. Render, Railway, Fly.io, and PythonAnywhere are all free for small apps. Add a `Procfile` with `web: gunicorn app:app` and a Python-version pin in `runtime.txt` if your platform needs them.
