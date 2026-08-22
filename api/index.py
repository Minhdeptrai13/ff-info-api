import os
import sys

# Ensure parent directory is in sys.path so proto and app modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

# Vercel needs app variable
