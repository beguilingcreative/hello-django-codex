# Hello Django Codex
# v2

This example demonstrates a minimal Django application that doesn't persist any data. Messages are kept in memory using plain Python objects. The settings include a small SQLite database so Django can start up, but the database itself isn't used by the app. It still highlights a few Django features:

- Rendering templates with Bootswatch styling.
- Using Django forms for user input.
- Basic view logic written in Python.
- A small Python demo page with a random quote and factorial calculator.

## Quick start

Install dependencies and run the development server:

```bash
pip install -r requirements.txt
python manage.py runserver
```

Then open <http://localhost:8000/> in your browser.
Navigate to <http://localhost:8000/demo/> to see the Python demo utilities.
