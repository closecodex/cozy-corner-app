# 🌿 Cozy Corner App

**Cozy Corner** is a warm, playful Flask web app made as a learning project — a small digital corner for relaxing, smiling, and experimenting with code.

This project brings together several cozy mini-features inspired by everyday hobbies like reading, drawing, puzzles, and cute animals 🐾  
It’s designed to be beginner-friendly, modular, and easy to explore.

---

## ✨ Features

🐶 **Dog Personality Matcher**  
A fun quiz that matches your personality to a dog breed.
![Cozy Corner Screenshot](https://github.com/user-attachments/assets/e43de58f-b601-407d-8a6b-f52d21af09bc)


🐱 **Cat Corner**  
Relaxing cat quotes and images for instant comfort.
![Cozy Corner Screenshot](https://github.com/user-attachments/assets/837cdc9e-298a-4215-bc45-44eaae431189)

📚 **Book Nook**  
Browse and discover books from a local database — no fake titles, no external APIs.

🧩 **Puzzle Time**  
A click-swap puzzle:
- upload your own image or use a default one  
- choose puzzle size (12 / 20 / 30 pieces)  
- enjoy a little celebration when you win 🎉
![Cozy Corner Screenshot](https://github.com/user-attachments/assets/3f95e4c5-485c-46ee-9ec4-5d673a44cf1b)


🎨 **Daily Drawing Prompt**  
Get a cozy drawing idea for the day, with recent prompts stored safely.

🎮 **Bonus Games**  
Classic games with a soft, hand-drawn vibe:
- Snake  
- Tic-Tac-Toe (with fanfare on victory!)
![Cozy Corner Screenshot](https://github.com/user-attachments/assets/62e6b8c1-dda7-41ed-a944-c6a817828c20)

🔊 **Sound Effects**  
- Tap sounds on navigation and buttons  
- Fanfare sounds for puzzle and game wins

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Jinja2**
- **SQLite**
- **Vanilla JavaScript**
- **Pytest** for automated testing

No external APIs — everything runs locally and safely.

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Make sure you have **Python 3** installed.

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
   Open your browser to `http://127.0.0.1:5000`.

## Running the Automated Tests

Automated testing is configured using `pytest` and the Flask test client. These tests verify that all routes load properly (HTTP 200) and that internal features (like Dog Matcher, Book database, etc.) function safely without external APIs.

1. Ensure test dependencies are installed:
   ```bash
   pip install pytest pytest-flask
   ```
2. Navigate to the project root directory.
3. Run the test suite:
   ```bash
   pytest tests/
   ```

*(Additional flags like `-v` (verbose) or `-s` (print output) can be useful for debugging!)*
