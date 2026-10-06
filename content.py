"""Everything a recruiter reads on the site.

Edit this file, not the template. Swapping a project means replacing one dict
in PROJECTS; adding an award link means filling in that award's `href`.
"""

PROFILE = {
    "name": "Bekzat Uraimov",
    "headline": "Software Engineer",
    "subhead": "Backend and systems",
    "blurb": (
        "Software Engineer | C++, Python, FastAPI, PostgreSQL | 2x Hackathon Award Winner | BS CS @ Bellevue College"
    ),
    "status": "Open to software engineering internships and entry level roles",
    "location": "Seattle, WA",
    "email": "bkzturaimov@gmail.com",
    "github": "https://github.com/bekzat-uraimov",
    "linkedin": "https://www.linkedin.com/in/bekzat-uraimov/",
    "leetcode": "https://leetcode.com/u/bekzat_uraimov/",
    "resume": "/static/Bekzat_Uraimov_Resume.pdf",
}

# Shown as chips under the hero headline.
HERO_CHIPS = [
    "Seattle, WA",
    "Python, Java, C++",
    "FastAPI, PostgreSQL, Docker",
]

# The scrolling strip under the hero.
STACK = [
    "Python", "C++", "Java", "JavaScript",
    "FastAPI", "Flask", "PostgreSQL", "REST APIs",
    "pytest", "Docker", "Git", "GitHub Actions",
    "LiteLLM", "Ollama",
]

# Filter pills above the project grid. The key matches a project's `filter`.
PROJECT_TABS = [
    ("all", "All"),
    ("backend", "Backend"),
    ("ai", "AI"),
]

# Projects shown on the site. Do not load from GitHub API.
PROJECTS = [
    {
        "title": "ONER",
        "category": "Course Platform Backend",
        "logo": "ON",
        "description": (
            "A paid course platform for Central Asia, getting ready to launch. "
            "I built the backend: payments, course access and video protection."
        ),
        "technologies": [
            "FastAPI", "PostgreSQL", "Docker",
            "Cloudflare R2", "Kinescope", "FreedomPay",
        ],
        "highlights": [
            "Stopped double charges and free access. Every payment webhook is checked for signature, amount and duplicates before a course opens.",
            "Kept paid lessons locked. Every request is checked on the server (JWT login plus an ownership check), so the browser can never unlock a course by itself.",
            "Made paid videos hard to share. Kinescope DRM gives short-lived playback tokens to course owners only.",
            "Let the team run the platform without touching the database, with a CRUD admin API for courses, file uploads to Cloudflare R2, users, purchases and refunds.",
        ],
        "github": "https://github.com/bekzat-uraimov/oner-platform",
        "demo": "https://oner-web-eta.vercel.app",
        "filter": "backend",
        "image": "/static/oner_cover.svg",
        "image_alt": "Animated ONER system design: checkout, signed FreedomPay webhook, entitlement granted once, DRM video for owners only",
        "badge": "LAUNCHING SOON",
        "placeholder": False,
    },
    {
        "title": "ThinkCoder",
        "category": "AI coding assistant",
        "logo": "TC",
        "description": (
            "An AI coding assistant built by a small team at akyldoo.ai. From March to May 2026, my part was the "
            "Python layer that picks which model answers each request."
        ),
        "technologies": ["Python", "LiteLLM", "Ollama"],
        "highlights": [
            "Cut estimated AI API spend by about 40%. Easy requests go to a free local model (Qwen2.5-Coder 7B on Ollama), and only hard ones go to a paid cloud model.",
            "Kept long coding sessions from breaking at the model's limit by managing how much context each request carries.",
        ],
        "github": None,
        "demo": None,
        "filter": "ai",
        "image": "/static/thinkcoder_cover.svg",
        "image_alt": "Animated ThinkCoder diagram: each problem gets its own session, and LiteLLM sends easy requests to a local model and hard ones to the cloud",
        "badge": "TEAM PROJECT",
        "placeholder": False,
    },
    {
        "title": "Fault tolerant inference",
        "short": "llm-failover",
        "category": "System design, C++ and Python",
        "logo": "FT",
        "description": (
            "A system design project. Kill a worker in the middle of an answer, and another one finishes it, byte for byte. "
            "It rebuilds the lost state from a small token log (about 1 KB) instead of copying the 3.5 MB KV cache. A tiny LLM is the workload. "
            "Early stage, built on top of llama2.c."
        ),
        "technologies": ["C++", "Python", "TCP", "Distributed systems"],
        "highlights": [],
        "github": "https://github.com/bekzat-uraimov/llm-failover",
        "demo": None,
        "filter": "backend ai",
        "image": "/static/failover_cover.svg",
        "image_alt": "Animated diagram: worker A streams tokens through a router that logs each one, worker A is killed mid sentence, the router replays its token log to worker B, and B finishes the same answer byte for byte",
        "badge": "NOW BUILDING",
        "placeholder": False,
    },
]

# Awards shown on the site
AWARDS = [
    {
        "event": "QuackHacks, University of Oregon",
        "award": "Polymarket Track, winner",
        "note": "Poly Predictor Kit. Led a team of 6 to build a Chrome extension that uses Gemini to sum up any Polymarket event and its risks.",
        "href": "https://github.com/bekzat-uraimov/Poly_Predictor_Kit",
    },
    {
        "event": "CodeDay Fall 2025, Seattle",
        "award": "Best Use of AI, winner",
        "note": "AI Visual Novel Creator. With my team, built a game that turns one prompt into a playable visual novel, using Gemini.",
        "href": "https://github.com/bekzat-uraimov/AI_Visual_Novel_Creator",
    },
]

ABOUT = [
    "I am a computer science student at Bellevue College, in Seattle. I build backends in Python, and I'm learning system design with C++.",
    "Right now most of my time goes to ONER and to my classes, Data Structures in C++ and Python for Data Science. I am looking for an internship or entry level role where I can learn from people with more experience than me.",
]

TIMELINE = [
    {"when": "NOW", "title": "ONER, Software Engineer", "detail": "Course platform backend, since May 2026"},
    {"when": "2026", "title": "akyldoo.ai, Software Engineer", "detail": "ThinkCoder model routing, March to May 2026"},
    {"when": "IN PROGRESS", "title": "Bellevue College", "detail": "BS in Computer Science, expected May 2028"},
    {"when": "2025 to 2026", "title": "Cascadia College", "detail": "Associate degree (DTA), GPA 3.6"},
    {"when": "2019 to 2023", "title": "Video editor and colorist", "detail": "Commercial video, before I started programming"},
]

CONTACT_BLURB = (
    "I am looking for a software engineering internship or entry level role. Email is the easiest way to reach me."
)
