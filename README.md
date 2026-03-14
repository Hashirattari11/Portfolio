# Hashir Attari — AI Engineer Portfolio

A modern, production-grade portfolio website built with **FastAPI** + **Jinja2** + **HTML/CSS/JS**.

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the development server
```bash
uvicorn main:app --reload
```

### 3. Open in browser
```
http://localhost:8000
```

---

## 📁 Project Structure

```
hashir_portfolio/
├── main.py                  ← FastAPI app (routes, data)
├── requirements.txt
├── templates/
│   ├── base.html            ← Shared layout (nav, footer)
│   ├── index.html           ← Home page
│   ├── about.html           ← About page
│   ├── skills.html          ← Skills page
│   ├── projects.html        ← Projects page
│   └── contact.html         ← Contact page + form
└── static/
    ├── css/
    │   └── style.css        ← All styles (dark AI theme)
    ├── js/
    │   └── main.js          ← Cursor, animations, nav
    └── images/              ← (add your images here)
```

---

## ✨ Features

- **FastAPI** backend with Jinja2 template rendering
- **Contact form** handled via POST `/contact/submit`
- Fully **responsive** — mobile, tablet, desktop
- Custom animated **cursor**
- **Scroll reveal** animations
- **Typewriter** effect on hero
- **Animated skill bars** on scroll
- **Project card tilt** on hover
- **Filter tabs** on skills page
- Dark developer theme with **Space Mono** + **Syne** fonts

---

## 🌐 Pages

| Route | Page |
|-------|------|
| `/` | Home (hero, stats) |
| `/about` | About (story, timeline) |
| `/skills` | Skills (filterable grid) |
| `/projects` | Projects (live demos) |
| `/contact` | Contact (form + info) |
| `/contact/submit` | POST — form submission |

---

## 📦 Deploy to Railway / Render

1. Push to GitHub
2. Connect repo to Railway or Render
3. Set start command: `uvicorn main:app --host 0.0.0.0 --port 8000`

---

© 2026 Hashir Attari – AI Engineer Portfolio
