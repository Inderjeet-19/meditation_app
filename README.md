# 🧘 Calm CLI – Meditation App

A simple **terminal-based meditation app** built in Python.
Practice mindfulness, guided breathing, and meditation sessions directly from your terminal — no external libraries required.

---

## ✨ Features

* ⏳ Guided meditation sessions (5, 10, 15 minutes)
* 🕑 Custom silent timer with progress bar
* 🌬️ Box breathing exercise (configurable inhale/hold/exhale)
* 🛌 Body-scan meditation (default 10 minutes)
* 📝 Session logging saved to `meditation_log.csv`
* 🔔 Gentle bell sound (cross-platform)
* ✅ Works on Windows, Linux, and macOS (Python 3.6+)

---

## 📸 Demo

Here’s a calming meditation animation to represent the app:

![Meditation Demo](https://images.openai.com/thumbnails/url/hJS1cXicu1mUUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw6yyMpycs_3zqp0zfZOTLEIKK4Ktcg3dzPxNY73jMqKyLUoyXTLNi2KKnNLcjYOc09MD81NCo8q8DRXKwYAxtwpKw)

---

## 📥 Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/meditation-app.git
cd meditation-app
```

No dependencies needed — only Python’s standard library.

---

## ▶️ Usage

Run the app with:

```bash
python meditation_app.py
```

Then follow the on-screen menu:

```
1) Guided — 5 minutes
2) Guided — 10 minutes
3) Guided — 15 minutes
4) Custom silent timer
5) Box breathing exercise
6) Body-scan meditation
7) View session log
0) Exit
```

---

## 📂 Log File

* All sessions are stored in `meditation_log.csv` with:

  * Timestamp
  * Type of session
  * Duration

Example entry:

```
timestamp,type,duration_min,notes
2025-10-02 10:05:30,Guided 10 min,10,
```

---

## 🌱 Roadmap

* [ ] Add a Tkinter GUI version
* [ ] Add ambient audio guidance
* [ ] Add reminders / daily streaks
* [ ] Export session stats as charts

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License. Feel free to use, modify, and share.

