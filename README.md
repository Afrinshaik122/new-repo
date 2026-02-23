# Simple Flask app for CI demo

This repository contains a minimal Flask application that serves a basic HTML UI.

- Start locally:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
python -m pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 to view the page.

The included GitHub Actions workflow runs the app in CI, fetches the UI, and uploads the result as an artifact named `ui-output`.
