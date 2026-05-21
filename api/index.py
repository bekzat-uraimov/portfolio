import os
import sys

# add project root to path so `app` is importable from the api/ subfolder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402

# vercel's python runtime looks for a WSGI callable named `app`
