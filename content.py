"""Everything a recruiter reads on the site.

Edit this file, not the template. Swapping a project means replacing one dict
in PROJECTS; adding an award link means filling in that award's `href`.
"""

PROFILE = {
    "name": "Bekzat Uraimov",
    "headline": "Software Engineer",
    "subhead": "Backend and systems",
    "blurb": "Building backend, distributed systems and ML projects.",
    "status": "Open to software engineering internships and entry level roles",
    # the sticker on the corner of the project laptop. hidden from screen readers, the awards section says the same
    "sticker": "2x hackathon winner",
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
    "Python, C++, Java, FastAPI, PostgreSQL, Docker",
]

# The scrolling strip under the hero.
STACK = [
    "Python", "C++", "Java", "SQL",
    "FastAPI", "Flask", "PostgreSQL", "REST APIs",
    "JWT auth", "pytest", "TCP sockets",
    "Docker", "Git", "GitHub Actions", "Cloudflare R2",
    "scikit-learn", "XGBoost", "pandas",
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
            "A paid course platform for Central Asia, in closed testing with 10 users. "
            "I built the backend: payments, course access and video protection."
        ),
        "technologies": [
            "FastAPI", "PostgreSQL", "Docker",
            "Cloudflare R2", "Kinescope", "FreedomPay",
        ],
        "highlights": [
            "Stopped double charges and free access. Payment providers can send the same webhook more than once and students double-click buy, so every webhook is checked for signature, amount and duplicates before a course opens, and a repeat click returns the same order.",
            "Kept paid lessons locked. Browser code can be changed, so every request is checked on the server (JWT login plus an ownership check) and the browser can never unlock a course by itself.",
            "Made paid videos hard to share. Course videos are what students pay for, so they play through Kinescope DRM with short-lived tokens that only course owners get.",
            "Let the team run the platform without touching the database, with a CRUD admin API for courses, file uploads to Cloudflare R2, users, purchases and refunds.",
        ],
        "summary": "Payments that never charge twice, and paid lessons only owners can open",
        "github": "https://github.com/bekzat-uraimov/oner-platform",
        "demo": "https://oner-web-eta.vercel.app",
        "filter": "backend",
        "image": "/static/oner_cover.svg",
        "image_alt": "Animated ONER system design: checkout, signed FreedomPay webhook, entitlement granted once, DRM video for owners only",
        "badge": "CLOSED TESTING",
        "placeholder": False,
    },
    {
        "title": "llm-failover",
        "short": "llm-failover",
        "category": "Fault tolerant inference service, C++ and Python",
        "logo": "FT",
        "description": (
            "When an LLM server crashes, the answer it was writing is lost and the user has to start over. This system design project keeps the answer going: kill a worker in the middle of an answer, and another one finishes it, byte for byte. "
            "It rebuilds the lost state from a small token log (about 1 KB) instead of copying the 3.5 MB KV cache. A tiny LLM is the workload. "
            "Early stage, built on top of llama2.c."
        ),
        "technologies": ["C++", "Python", "TCP", "Distributed systems"],
        "highlights": [],
        "summary": "An LLM answer that survives a crashed server, byte for byte",
        "github": "https://github.com/bekzat-uraimov/llm-failover",
        "demo": None,
        "filter": "backend ai",
        "image": "/static/failover_cover.svg",
        "image_alt": "Animated diagram: worker A streams tokens through a router that logs each one, worker A is killed mid sentence, the router replays its token log to worker B, and B finishes the same answer byte for byte",
        "badge": "NOW BUILDING",
        "placeholder": False,
    },
    {
        "title": "ThinkCoder",
        "category": "AI coding assistant",
        "logo": "TC",
        "description": (
            "ThinkCoder is akyldoo.ai's AI coding assistant. As an AI Engineer Intern from March to May 2026, I built the "
            "Python model routing layer that decides which model answers each request."
        ),
        "technologies": ["Python", "LiteLLM", "Ollama"],
        "highlights": [
            "Cut estimated AI API spend by about 40%. Easy requests go to a free local model (Qwen2.5-Coder 7B on Ollama), and only hard ones go to a paid cloud model.",
            "Kept long coding sessions from breaking at the model's limit by managing how much context each request carries.",
        ],
        "summary": "About 40% lower estimated AI cost by sending easy questions to a free local model",
        "links": [
            ("akyldoo.ai", "https://akyldoo.ai"),
        ],
        "github": None,
        "demo": None,
        "filter": "ai",
        "image": "/static/thinkcoder_cover.svg",
        "image_alt": "Animated ThinkCoder diagram: each problem gets its own session, and LiteLLM sends easy requests to a local model and hard ones to the cloud",
        "badge": "INTERNSHIP",
        "placeholder": False,
    },
    {
        "title": "Heart Disease Models",
        "short": "heart-disease",
        "category": "Machine learning model comparison, Python",
        "logo": "HD",
        "description": (
            "A machine learning study on 297 patients. I trained Logistic Regression and XGBoost to predict heart disease, "
            "then checked what L2 regularization does to accuracy and to the model's coefficients."
        ),
        "technologies": ["Python", "scikit-learn", "XGBoost", "pandas", "matplotlib"],
        "highlights": [
            "Got the best test accuracy, 90.0%, from Logistic Regression with stronger L2 regularization (C=0.1). It scored lower on training data than the default model and higher on new patients.",
            "Caught XGBoost overfitting. It scored 100% on training data but only 85.0% on the 60 test patients, the worst of the three.",
            "Fit the scaler on the training split only, so nothing from the test patients leaked into training.",
            "Wrote down the limits. C was picked with the test set and 60 patients is a small sample, so the next step is cross-validation.",
        ],
        "summary": "Caught XGBoost overfitting (100% train, 85% test) next to a regularized model",
        "github": "https://github.com/bekzat-uraimov/heart-disease-classification-model-comparison",
        "demo": None,
        "filter": "ai",
        "image": "/static/heart_cover.svg",
        "image_alt": "Animated chart: 60 held-out patients are scored by three models in turn, right answers in black and wrong ones in red. Logistic Regression gets 52 right with C=1 and 54 with C=0.1, XGBoost gets 51 after scoring 100% on its training data",
        "badge": "ML STUDY",
        "placeholder": False,
    },
]

# Awards shown on the site
AWARDS = [
    {
        "event": "QuackHacks, University of Oregon",
        "award": "Polymarket Track, winner",
        "note": "Poly Predictor Kit. Led a team of 6 to build a Chrome extension that uses Gemini to sum up any Polymarket event and its risks, and rates its comments as emotional or rational. I built the comment collector that feeds our model.",
        "links": [
            ("Devpost", "https://devpost.com/software/poly-predictor-kit"),
            ("Code", "https://github.com/bekzat-uraimov/Poly_Predictor_Kit"),
        ],
    },
    {
        "event": "CodeDay Fall 2025, Seattle",
        "award": "Best Use of AI, winner",
        "note": "AI Visual Novel Creator. With my team of 6, built a game that turns one prompt into a playable visual novel, using Gemini. I built the Ren'Py game loop.",
        "links": [
            ("CodeDay showcase", "https://showcase.codeday.org/project/cmhgqspw91903j5my04z26yk6"),
            ("Code", "https://github.com/bekzat-uraimov/AI_Visual_Novel_Creator"),
        ],
    },
]

ABOUT = [
    "I am a computer science student at Bellevue College, in Seattle. I build backends in Python, and I'm learning system design with C++.",
    "Right now most of my time goes to ONER and to my classes, Data Structures in C++ and Python for Data Science. I am looking for an internship or entry level role where I can learn from people with more experience than me.",
]

TIMELINE = [
    {"when": "NOW", "title": "ONER, Backend Engineer", "detail": "Course platform backend, since May 2026"},
    {"when": "2026", "title": "akyldoo.ai, AI Engineer Intern", "detail": "Model routing for ThinkCoder, March to May 2026"},
    {"when": "IN PROGRESS", "title": "Bellevue College", "detail": "BS in Computer Science, September 2026 to June 2028"},
    {"when": "2025 to 2026", "title": "Cascadia College", "detail": "Associate degree (DTA), GPA 3.51"},
    {"when": "2021 to 2023", "title": "Antares and Mostcreative Agency, Video Editor and Colorist", "detail": "Delivered commercial videos for clients, from shoot to final color grade, before I started programming"},
]

CONTACT_BLURB = (
    "I am looking for a software engineering internship or entry level role. Email is the easiest way to reach me."
)
