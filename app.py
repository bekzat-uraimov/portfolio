import os
import time
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

GITHUB_USER = os.environ.get("GITHUB_USER", "bekzat-uraimov")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # enables GraphQL pinned fetch
GITHUB_PINNED = [n.strip() for n in os.environ.get("GITHUB_PINNED", "").split(",") if n.strip()]
CACHE_TTL = 600  # seconds

_cache = {"data": None, "fetched_at": 0}


def _rest_headers():
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def fetch_pinned_via_graphql():
    """Real pinned repos. Requires GITHUB_TOKEN."""
    query = """
    query($login: String!) {
      user(login: $login) {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              description
              url
              isFork
              stargazerCount
              updatedAt
              primaryLanguage { name }
              repositoryTopics(first: 8) { nodes { topic { name } } }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    r = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"login": GITHUB_USER}},
        headers=headers,
        timeout=10,
    )
    r.raise_for_status()
    nodes = r.json()["data"]["user"]["pinnedItems"]["nodes"]
    return [
        {
            "name": n["name"],
            "description": n.get("description") or "",
            "url": n["url"],
            "language": (n["primaryLanguage"] or {}).get("name"),
            "topics": [t["topic"]["name"] for t in n["repositoryTopics"]["nodes"]],
            "stars": n["stargazerCount"],
            "forked": n["isFork"],
            "updated": n["updatedAt"],
        }
        for n in nodes
    ]


def fetch_all_repos():
    """All public repos via REST. Used for the named-pinned filter and the default."""
    url = f"https://api.github.com/users/{GITHUB_USER}/repos"
    r = requests.get(url, headers=_rest_headers(), params={"sort": "updated", "per_page": 100}, timeout=10)
    r.raise_for_status()
    return [
        {
            "name": repo["name"],
            "description": repo.get("description") or "",
            "url": repo["html_url"],
            "language": repo.get("language"),
            "topics": repo.get("topics", []),
            "stars": repo["stargazers_count"],
            "forked": repo.get("fork", False),
            "updated": repo["updated_at"],
        }
        for repo in r.json()
        if not (repo.get("fork") and not repo.get("description"))
    ]


def fetch_repos():
    now = time.time()
    if _cache["data"] and now - _cache["fetched_at"] < CACHE_TTL:
        return _cache["data"]

    if GITHUB_TOKEN:
        repos = fetch_pinned_via_graphql()
    elif GITHUB_PINNED:
        all_repos = fetch_all_repos()
        by_name = {r["name"]: r for r in all_repos}
        repos = [by_name[n] for n in GITHUB_PINNED if n in by_name]
    else:
        repos = fetch_all_repos()

    _cache["data"] = repos
    _cache["fetched_at"] = now
    return repos


@app.route("/")
def home():
    return render_template("index.html", github_user=GITHUB_USER)


@app.route("/api/repos")
def api_repos():
    try:
        return jsonify(fetch_repos())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)
