from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Hashir Attari Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ─── Data ───────────────────────────────────────────────────────────────────

SKILLS = [
    {"name": "Artificial Intelligence", "icon": "🤖", "level": 88, "category": "AI/ML"},
    {"name": "Machine Learning",        "icon": "📊", "level": 90, "category": "AI/ML"},
    {"name": "Deep Learning",           "icon": "🧠", "level": 85, "category": "AI/ML"},
    {"name": "NLP",                     "icon": "💬", "level": 80, "category": "AI/ML"},
    {"name": "Python",                  "icon": "🐍", "level": 93, "category": "Languages"},
    {"name": "TensorFlow",              "icon": "⚡", "level": 83, "category": "Frameworks"},
    {"name": "Pandas",                  "icon": "🐼", "level": 91, "category": "Frameworks"},
    {"name": "NumPy",                   "icon": "🔢", "level": 89, "category": "Frameworks"},
    {"name": "SQL",                     "icon": "🗄️", "level": 78, "category": "Databases"},
    {"name": "Frontend Development",    "icon": "🌐", "level": 75, "category": "Web"},
    {"name": "CI/CD",                   "icon": "⚙️", "level": 72, "category": "DevOps"},
    {"name": "Netlify / Railway / Vercel", "icon": "🚀", "level": 80, "category": "DevOps"},
]

PROJECTS = [
    {
        "id": 1,
        "title": "House Price Prediction Dashboard",
        "emoji": "🏠",
        "description": "A production-ready machine learning web application that predicts house prices based on property features. Built with a trained regression model, interactive form inputs, and instant real-time predictions.",
        "tags": ["Machine Learning", "Python", "Railway", "Regression"],
        "demo": "https://house-price-prediction-production-a868.up.railway.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#3b82f6",
    },
    {
        "id": 2,
        "title": "Wine Quality Prediction Dashboard",
        "emoji": "🍷",
        "description": "A data science dashboard that predicts wine quality using chemical property inputs such as acidity, alcohol, and pH levels. Features a classification model with visual analytics and a polished UI.",
        "tags": ["Data Science", "Classification", "Netlify", "Analytics"],
        "demo": "https://agent-6990c8ba3ea9ca1bf190a75--jade-kheer-dd6708.netlify.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#8b5cf6",
    },
    {
        "id": 3,
        "title": "Stock Market Dashboard",
        "emoji": "📈",
        "description": "An interactive stock market data visualization platform with real-time charting, asset comparison, and market trend analysis. Built with a clean, responsive interface deployed on Vercel.",
        "tags": ["Data Visualization", "Dashboard", "Vercel", "Finance"],
        "demo": "https://stock-market-place-dashboard-1.vercel.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#06b6d4",
    },
    {
        "id": 4,
        "title": "Image Classification Model",
        "emoji": "🖼️",
        "description": "A deep learning image classification project using Convolutional Neural Networks with TensorFlow/Keras. Trained to classify images with industry-standard accuracy metrics and real-time inference.",
        "tags": ["Deep Learning", "CNN", "TensorFlow", "Computer Vision"],
        "demo": "https://github.com/Hashirattari11",
        "github": "https://github.com/Hashirattari11",
        "color": "#f59e0b",
    },
]

messages_store = []

# ─── Routes ─────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "home"})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "page": "about"})

@app.get("/skills", response_class=HTMLResponse)
async def skills(request: Request):
    return templates.TemplateResponse("skills.html", {
        "request": request,
        "page": "skills",
        "skills": SKILLS
    })

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "page": "projects",
        "projects": PROJECTS
    })

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "page": "contact"})

@app.post("/contact/submit")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
):
    messages_store.append({"name": name, "email": email, "subject": subject, "message": message})
    return JSONResponse({"success": True, "message": f"Thanks {name}! Your message has been received."})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
