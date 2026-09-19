"""Everything a recruiter reads on the site.

Edit this file, not the template. Swapping a project means replacing one dict
in PROJECTS; adding an award link means filling in that award's `href`.
"""

PROFILE = {
    "name": "Bekzat Uraimov",
    "headline": "Software Engineer",
    "subhead": "Backend · AI · Developer Tools",
    "blurb": (
        "CS student in Seattle building backend systems, developer tools, "
        "and AI-powered applications."
    ),
    "status": "Open to software engineering internships and full-time roles",
    "location": "Seattle, WA",
    "email": "bkzturaimov@gmail.com",
    "github": "https://github.com/bekzat-uraimov",
    "linkedin": "https://www.linkedin.com/in/bekzat-uraimov",
    "leetcode": "https://leetcode.com/u/bekzat-uraimov",
    # TODO: drop the PDF into static/ and set this to "/static/resume.pdf".
    # While it is None the Resume link is hidden everywhere instead of
    # rendering a dead link.
    "resume": None,
}

# Shown as chips under the hero headline.
HERO_CHIPS = [
    "Python · Java · JavaScript",
    "FastAPI · PostgreSQL · Docker",
]

# The scrolling strip under the hero.
STACK = [
    "Python", "Java", "JavaScript",
    "FastAPI", "Flask", "PostgreSQL",
    "SQLModel", "Docker", "Git",
    "GitHub Actions", "REST APIs", "LLM APIs",
]

# Filter pills above the project grid. The key matches a project's `filter`.
PROJECT_TABS = [
    ("all", "All"),
    ("backend", "Backend"),
    ("ai", "AI and dev tools"),
    ("data", "Data"),
]

# Each project renders one card. Keys:
#   title, category, logo (2 letters), description (one sentence),
#   technologies (list), highlights (3-4 bullets on what was engineered),
#   github / demo (URL or None), filter (matches PROJECT_TABS),
#   image (path under /static, or None to draw the generic mock),
#   badge (small label over the thumbnail, or None),
#   placeholder (True marks the card as not-yet-built; see the note below).
#
# PLACEHOLDER PROJECTS: CodeLens and Signal are stand-ins for real repos.
# They render a "PLACEHOLDER" badge so the live site never claims work that
# does not exist. Replace the whole dict with a real project and set
# placeholder=False — nothing else needs to change.
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
        # Each bullet below was checked against the ONER repo, not paraphrased
        # from memory. See app/services/entitlements.py, app/services/payments.py,
        # app/api/drm.py and app/services/storage.py.
        "highlights": [
            "Modeled users, courses, modules, lessons, and materials around an entitlements "
            "table that is the only record of who owns what.",
            "Made server-side entitlements the single gate for content — access is never "
            "decided by the client or by a payment redirect, only by a verified webhook.",
            "Hardened the FreedomPay callback with signature, amount, and order checks, and "
            "made the grant idempotent behind a unique constraint so retried webhooks never "
            "double-grant.",
            "Gated video behind Kinescope DRM by answering the playback-authorization callback "
            "per play, and served course materials as expiring R2 presigned URLs.",
        ],
        # TODO: the repo is private for now. When you make it public, set this to
        # "https://github.com/bekzat-uraimov/ONER" and a Source button appears.
        "github": None,
        "demo": "https://oner-web-eta.vercel.app",
        "filter": "backend",
        "image": "/static/oner.webp",
        "image_alt": "ONER course platform home page",
        "badge": "LAUNCHING SOON",
        "placeholder": False,
    },
    {
        "title": "CodeLens",
        "category": "AI Developer Tool",
        "logo": "CL",
        "description": (
            "Developer tool that uses AI to analyze code and surface useful feedback "
            "directly in the development workflow."
        ),
        "technologies": ["Python", "LLM APIs", "GitHub Actions", "FastAPI"],
        "highlights": [
            "Integrated an LLM API into an automated developer workflow.",
            "Designed a backend/API layer for processing source code and returning "
            "structured analysis.",
            "Connected automated analysis to a developer workflow rather than requiring a "
            "separate standalone interface.",
            "Focused the tool on actionable developer feedback instead of generic "
            "AI-generated text.",
        ],
        "github": None,
        "demo": None,
        "filter": "ai",
        "image": None,
        "badge": "PLACEHOLDER",
        "placeholder": True,
    },
    {
        "title": "Signal",
        "category": "Data Analysis Platform",
        "logo": "SG",
        "description": (
            "Data-focused application for processing, analyzing, and presenting "
            "structured datasets through a useful software interface."
        ),
        "technologies": ["Python", "Pandas", "PostgreSQL", "JavaScript"],
        "highlights": [
            "Built a Python-based data processing pipeline.",
            "Designed structured storage for analyzed data.",
            "Used data transformation and analysis to produce useful outputs rather than "
            "raw datasets.",
            "Presented results through a simple application interface.",
        ],
        "github": None,
        "demo": None,
        "filter": "data",
        "image": None,
        "badge": "PLACEHOLDER",
        "placeholder": True,
    },
]

# `href` stays None until the write-up or proof exists; the card renders as
# plain text now and as a link the moment a URL is filled in.
AWARDS = [
    {
        "event": "Seattle Code Day",
        "award": "Best Use of AI — Winner",
        "note": "AI Novella Generator",
        "href": None,
    },
    {
        "event": "QuackHacks",
        "award": "Track Winner",
        "note": "Oregon State University",
        "href": None,
    },
]

ABOUT = [
    "I'm a CS student in Seattle who enjoys building software that solves real problems. "
    "My main interests are backend engineering, developer tools, and AI-powered applications.",
    "I learn by building — from APIs and database-backed systems to developer tools and "
    "applications that integrate AI.",
]

TIMELINE = [
    {
        "when": "NOW",
        "title": "Startup Intern · akyldoo.ai",
        "detail": "Python orchestration layer for ThinkCoder, since 2025",
    },
    {
        "when": "NOW",
        "title": "Software Engineer · ONER",
        "detail": "Video craft platform for Central Asia, since 2024",
    },
    {
        "when": "IN PROGRESS",
        # TODO: the site said Bellevue College, the profile notes say Cascadia.
        # Confirm which is correct.
        "title": "Bellevue College",
        "detail": "BS in Computer Science, coursework in machine learning and data science",
    },
    {
        "when": "DONE",
        "title": "Associate degree",
        "detail": "Finished before transferring in",
    },
    {
        "when": "2019 → 2023",
        "title": "Colorist and Editor",
        "detail": "Freelance commercial video",
    },
]

CONTACT_BLURB = (
    "I'm looking for software engineering opportunities where I can build useful "
    "software, learn from experienced engineers, and contribute to real systems."
)
