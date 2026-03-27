import sqlite3
import random
import string

DB_NAME = "urls.db"

def init_db():
    """Create the URLs table if it doesn't already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def generate_short_code(length=6):
    """Generate a random 6-character code like 'aB3kZ9'."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def save_url(original_url):
    """Save a URL and return its short code."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Keep generating until we get a unique code
    while True:
        code = generate_short_code()
        try:
            cursor.execute("INSERT INTO urls (short_code, original_url) VALUES (?, ?)", (code, original_url))
            conn.commit()
            break
        except sqlite3.IntegrityError:
            # Code already exists, try again
            continue

    conn.close()
    return code

def get_url(short_code):
    """Look up the original URL for a given short code."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None