"""Everything a recruiter reads on the site.

Edit this file, not the template. Swapping a project means replacing one dict
in PROJECTS; adding an award link means filling in that award's `href`.
"""

PROFILE = {
    "name": "Bekzat Uraimov",
    "headline": "Software Engineer",
    "subhead": "Backend and AI",
    "blurb": (
        "CS student in Seattle building backend systems, developer tools, "
        "and AI-powered applications."
    ),
    "status": "Open to software engineering internships and entry level roles",
    "location": "Seattle, WA",
    "email": "bkzturaimov@gmail.com",
    "github": "https://github.com/bekzat-uraimov",
    "linkedin": "https://www.linkedin.com/in/bekzat-uraimov/",
    "leetcode": "https://leetcode.com/u/bekzat-uraimov",
    # keep resume as None until you drop a PDF in static/
    "resume": None,
}

# Shown as chips under the hero headline.
HERO_CHIPS = [
    "Seattle, WA | Python, Java, C++ | FastAPI, PostgreSQL, Docker",
]

# The scrolling strip under the hero.
STACK = [
    "Python", "Java", "JavaScript",
    "FastAPI", "Flask", "PostgreSQL",
    "SQLModel", "Docker", "Git",
    "GitHub Actions", "REST APIs", "LLM APIs",
    "LangGraph", "LiteLLM", "C++",
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
            "Backend platform for selling and delivering online courses, with "
            "authenticated content access, payments, webhooks, and protected media."
        ),
        "technologies": [
            "FastAPI", "PostgreSQL", "SQLModel", "Docker",
            "Cloudflare R2", "Kinescope", "FreedomPay",
        ],
        # Exact text kept from the repo; only the dash after "content" was replaced with a period.
        "highlights": [
            "Modeled users, courses, modules, lessons, and materials around an entitlements table that is the only record of who owns what.",
            "Made server-side entitlements the single gate for content. Access is never decided by the client or by a payment redirect, only by a verified webhook.",
            "Hardened the FreedomPay callback with signature, amount, and order checks, and made the grant idempotent behind a unique constraint so retried webhooks never double-grant.",
            "Gated video behind Kinescope DRM by answering the playback-authorization callback per play, and served course materials as expiring R2 presigned URLs.",
        ],
        "github": None,
        "demo": "https://oner-web-eta.vercel.app",
        "filter": "backend",
        "image": "/static/oner.webp",
        "image_alt": "ONER course platform home page",
        "badge": "LAUNCHING SOON",
        "placeholder": False,
    },
    {
        "title": "ThinkCoder",
        "category": "AI coding assistant",
        "logo": "TC",
        "description": (
            "An AI coding assistant made by a small team at akyldoo.ai. My part was the "
            "Python layer that decides how each problem is worked through."
        ),
        "technologies": ["Python", "LangGraph", "LiteLLM", "Ollama", "Gemini"],
        "highlights": [
            "Each problem runs as its own LangGraph session with its own state, instead of one long prompt.",
            "Requests go through LiteLLM: simple ones to a local Qwen2.5-Coder-7B model on Ollama, harder ones to Gemini, to keep the cost low.",
            "Worked on keeping long sessions inside the model context window.",
        ],
        "github": None,
        "demo": None,
        "filter": "ai",
        "image": "/static/thinkcoder_sys.svg",
        "image_alt": "ThinkCoder system design cover",
        "badge": "TEAM PROJECT",
        "placeholder": False,
    },
    {
        "title": "Tokenizer for Central Asian languages",
        "category": "C++ and Python",
        "logo": "TK",
        "description": (
            "Kyrgyz, Kazakh and Uzbek usually take more tokens than English in AI models, "
            "so the same sentence costs more and fits less. I want to measure how big that gap is first, "
            "and then try to build a better tokenizer in C++. Just starting, nothing to show yet."
        ),
        "technologies": ["C++", "Python"],
        "highlights": [],
        "github": None,
        "demo": None,
        "filter": "ai",
        "image": "/static/tokenizer_sys.svg",
        "image_alt": "Tokenizer system design cover",
        "badge": "NOW BUILDING",
        "placeholder": False,
    },
]

# Awards shown on the site
AWARDS = [
    {
        "event": "QuackHacks, University of Oregon",
        "award": "Polymarket Track, winner",
        "note": "Poly Predictor Kit, team of six",
        "href": "https://github.com/bekzat-uraimov/Poly_Predictor_Kit",
    },
    {
        "event": "Seattle Code Day",
        "award": "Best Use of AI, winner",
        "note": "AI Visual Novel Creator, team project",
        "href": "https://github.com/bekzat-uraimov/AI_Visual_Novel_Creator",
    },
]

ABOUT = [
    "I am a computer science student at Bellevue College, in Seattle. I like backend work the most: APIs, databases, and the parts that have to be right, like payments.",
    "Right now most of my time goes to ONER and to my classes, Data Structures in C++ and Python for Data Science. I am looking for an internship or entry level role where I can learn from people with more experience than me.",
]

TIMELINE = [
    {"when": "NOW", "title": "Founding Engineer, ONER", "detail": "Course platform backend, since May 2026"},
    {"when": "NOW", "title": "Software Engineer, akyldoo.ai", "detail": "ThinkCoder orchestration layer, since March 2026"},
    {"when": "IN PROGRESS", "title": "Bellevue College", "detail": "BS in Computer Science, expected 2028"},
    {"when": "2025 to 2026", "title": "Cascadia College", "detail": "Associate degree (DTA)"},
    {"when": "2019 to 2023", "title": "Colorist and video editor", "detail": "Commercial video, before I started programming"},
]

CONTACT_BLURB = (
    "I am looking for a software engineering internship or entry level role. Email is the easiest way to reach me."
)
