from flask import Flask, render_template, request, url_for, session, jsonify
import os
from datetime import date

from services.dog_logic import evaluate_dog_match, QUESTIONS
from services.book_service import search_books
from services.drawing_prompt_service import generate_prompt, init_db

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
        static_url_path="/static",
    )
    # In a real project, keep this secret and load from env
    app.config["SECRET_KEY"] = "dev-cozy-corner-secret"
    app.config["DATABASE_PATH"] = os.path.join(app.instance_path, "cozy_corner.sqlite3")

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialize database tables (idempotent)
    init_db(app.config["DATABASE_PATH"])

    @app.route("/")
    def home():
        return render_template("home.html")

    # --- Dog Personality Matcher ---
    @app.route("/dog-matcher", methods=["GET", "POST"])
    def dog_matcher():
        questions = QUESTIONS

        if request.method == "POST":
            answers = {}
            missing = []
            for q in questions:
                value = request.form.get(q["id"])
                if not value:
                    missing.append(q["text"])
                else:
                    answers[q["id"]] = value

            if missing:
                return render_template(
                    "dog_matcher.html",
                    questions=questions,
                    error_message="Please answer all questions to meet your perfect pup 🐶",
                )

            match = evaluate_dog_match(answers)
            return render_template("dog_matcher_result.html", result=match)

        return render_template("dog_matcher.html", questions=questions)

    # --- Cat Facts + Images ---
    @app.route("/cats")
    def cats():
        return render_template("cats.html")

    @app.route("/api/cat")
    def api_cat():
        """
        Small JSON endpoint so the front-end JS can ask the server,
        and the server can talk to third‑party APIs.
        """
        import requests

        fact_text = None
        image_url = None
        error = None

        try:
            fact_resp = requests.get("https://catfact.ninja/fact", timeout=5)
            if fact_resp.ok:
                fact_text = fact_resp.json().get("fact")
        except Exception:
            error = "Could not fetch a new cat fact right now."

        try:
            img_resp = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5)
            if img_resp.ok:
                data = img_resp.json()
                if isinstance(data, list) and data:
                    image_url = data[0].get("url")
        except Exception:
            if error is None:
                error = "Cat images are taking a nap. Try again soon."

        if not fact_text:
            fact_text = "Cats purr in a cozy frequency that can even help humans relax. Probably."

        if not image_url:
            # Simple static fallback image path under static/images
            image_url = url_for("static", filename="images/cozy_cat_fallback.svg")

        # Optionally remember last fact in the session
        session["last_cat_fact"] = fact_text

        return jsonify({"fact": fact_text, "image_url": image_url, "error": error})

    # --- Random Book Generator ---
    @app.route("/books", methods=["GET", "POST"])
    def books():
        genres = [
            "fantasy",
            "sci-fi",
            "romance",
            "classics",
            "mystery",
            "non-fiction",
            "self-help",
            "ya",
            "dystopia",
            "psychology",
        ]
        suggestions = []
        error_message = None
        selected_genre = None
        keywords_value = ""

        if request.method == "POST":
            selected_genre = (request.form.get("genre") or "").strip()
            keywords_value = request.form.get("keywords", "").strip()
            if not selected_genre:
                error_message = "Please choose a genre to explore 📚"
                return render_template(
                    "books.html",
                    genres=genres,
                    suggestions=[],
                    error_message=error_message,
                    selected_genre=None,
                    keywords_value=keywords_value,
                )
            try:
                suggestions = search_books(selected_genre, keywords_value)
                if not suggestions:
                    error_message = "No matches found — try another keyword 📚"
            except Exception:
                error_message = "Book gnomes are on a break. Please try again in a moment."

        return render_template(
            "books.html",
            genres=genres,
            suggestions=suggestions,
            error_message=error_message,
            selected_genre=selected_genre,
            keywords_value=keywords_value,
        )

    # --- Image Puzzle Generator ---
    @app.route("/puzzle")
    def puzzle():
        """
        Displays an interactive click-swap puzzle. User can upload custom images
        or play with the default puzzle_default.jpg.
        """
        image_url = url_for("static", filename="images/puzzle_default.jpg")
        return render_template("puzzle.html", image_url=image_url)

    # --- Daily Drawing Prompt Generator ---
    @app.route("/drawing-prompt", methods=["GET", "POST"])
    def drawing_prompt():
        current_prompt = generate_prompt()
        return render_template(
            "drawing_prompt.html",
            prompt=current_prompt,
        )

    # --- About Me Page ---
    @app.route("/about")
    def about():
        return render_template("about.html")

    # --- Bonus Games Page ---
    @app.route("/bonus")
    def bonus():
        return render_template("bonus.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

