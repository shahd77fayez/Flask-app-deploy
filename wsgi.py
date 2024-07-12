# wsgi.py
from application import app  # Assuming your Flask app instance is in server.py

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
