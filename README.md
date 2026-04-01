# 🔗 Elegant URL Shortener

A lightweight, beautifully designed URL shortener web application. Built with a Python/Flask backend and a modern "glassmorphism" frontend, this app allows users to easily convert long, cumbersome URLs into elegant, easily shareable short links.

## ✨ Features

* **Instant Shortening:** Converts any valid URL into a compact, 6-character alphanumeric short link.
* **Auto-Validation:** Automatically prepends `https://` to user inputs if a protocol is missing.
* **Modern UI/UX:** Features a stunning, responsive "glassmorphism" interface with soft blurred backgrounds, gradients, and premium typography.
* **Built-in Database:** Uses SQLite to store and retrieve URLs locally with zero complex setup required. Built-in collision detection ensures every short code is unique.
* **Cloud-Ready:** Pre-configured with a `Procfile` and `gunicorn` for immediate deployment on platforms like Render, Heroku, or Railway.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3 (Google Fonts: Cormorant Garamond, Inter)
* **Server / Deployment:** Gunicorn

## 📁 Project Structure

```text
├── app.py                 # Main Flask application and routing logic
├── database.py            # SQLite database initialization and queries
├── Procfile               # Deployment execution command
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules for virtual env and DB files
└── templates/
    └── index.html         # Frontend HTML structure and CSS styling
