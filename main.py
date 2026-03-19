from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Email config ────────────────────────────────────────────────────────────
GMAIL_USER     = os.getenv("GMAIL_USER", "hashirattari73@gmail.com")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", "aefi cwfd qigx pkmn")
NOTIFY_EMAIL   = "hashirattari73@gmail.com"


def send_email(name: str, sender_email: str, subject: str, message: str) -> bool:
    """Send contact form submission to Hashir's Gmail."""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"]  = f"Portfolio Contact: {subject}"
        msg["From"]     = GMAIL_USER
        msg["To"]       = NOTIFY_EMAIL
        msg["Reply-To"] = sender_email

        html_body = f"""
        <html><body style="font-family:Arial,sans-serif;background:#0d1120;color:#e2e8f0;padding:30px;">
          <div style="max-width:600px;margin:0 auto;background:#111827;border-radius:12px;
                      border:1px solid rgba(99,179,255,0.15);overflow:hidden;">
            <div style="background:linear-gradient(135deg,#3b82f6,#06b6d4);padding:24px 30px;">
              <h2 style="margin:0;color:#fff;font-size:1.4rem;">📬 New Portfolio Message</h2>
            </div>
            <div style="padding:30px;">
              <table style="width:100%;border-collapse:collapse;">
                <tr><td style="padding:10px 0;color:#64748b;width:120px;">From</td>
                    <td style="padding:10px 0;color:#f1f5f9;font-weight:bold;">{name}</td></tr>
                <tr><td style="padding:10px 0;color:#64748b;">Email</td>
                    <td style="padding:10px 0;"><a href="mailto:{sender_email}" style="color:#3b82f6;">{sender_email}</a></td></tr>
                <tr><td style="padding:10px 0;color:#64748b;">Subject</td>
                    <td style="padding:10px 0;color:#f1f5f9;">{subject}</td></tr>
              </table>
              <hr style="border:none;border-top:1px solid rgba(99,179,255,0.1);margin:20px 0;">
              <p style="color:#64748b;margin-bottom:8px;">Message:</p>
              <div style="background:#0d1120;border-radius:8px;padding:20px;
                          border-left:3px solid #3b82f6;color:#e2e8f0;line-height:1.7;">
                {message.replace(chr(10), '<br>')}
              </div>
            </div>
            <div style="padding:16px 30px;background:#0d1120;text-align:center;
                        color:#64748b;font-size:0.8rem;">
              Sent from your portfolio · hashirattari73@gmail.com
            </div>
          </div>
        </body></html>
        """

        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, NOTIFY_EMAIL, msg.as_string())

        return True
    except Exception as e:
        print(f"[Email Error] {e}")
        return False


app = FastAPI(title="Hashir Attari Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SKILLS = [
    {"name": "Artificial Intelligence",         "icon": "🤖", "level": 88, "category": "AI/ML"},
    {"name": "Machine Learning",                "icon": "📊", "level": 90, "category": "AI/ML"},
    {"name": "Deep Learning",                   "icon": "🧠", "level": 85, "category": "AI/ML"},
    {"name": "Natural Language Processing",     "icon": "💬", "level": 80, "category": "AI/ML"},
    {"name": "TensorFlow",                      "icon": "⚡", "level": 85, "category": "Frameworks"},
    {"name": "Keras",                           "icon": "🔥", "level": 83, "category": "Frameworks"},
    {"name": "Scikit-Learn",                    "icon": "🔬", "level": 88, "category": "Frameworks"},
    {"name": "MobileNetV2 / Transfer Learning", "icon": "🖼️", "level": 80, "category": "Frameworks"},
    {"name": "Python",                          "icon": "🐍", "level": 93, "category": "Languages"},
    {"name": "JavaScript",                      "icon": "🌐", "level": 75, "category": "Languages"},
    {"name": "HTML / CSS",                      "icon": "🎨", "level": 78, "category": "Languages"},
    {"name": "Pandas",                          "icon": "🐼", "level": 91, "category": "Data Science"},
    {"name": "NumPy",                           "icon": "🔢", "level": 89, "category": "Data Science"},
    {"name": "SQL",                             "icon": "🗄️", "level": 78, "category": "Data Science"},
    {"name": "Data Visualization",              "icon": "📈", "level": 82, "category": "Data Science"},
    {"name": "Django",                          "icon": "🦄", "level": 72, "category": "Web"},
    {"name": "Frontend Development",            "icon": "💻", "level": 75, "category": "Web"},
    {"name": "CI/CD",                           "icon": "⚙️", "level": 74, "category": "DevOps"},
    {"name": "Netlify / Vercel / Railway",      "icon": "🚀", "level": 82, "category": "DevOps"},
]

PROJECTS = [
    {
        "id": 1,
        "title": "House Price Prediction Dashboard",
        "emoji": "🏠",
        "description": "Interactive web app predicting house prices using a Random Forest regression model achieving 76% accuracy. Deployed live on Railway with a clean UI for real-time user input and instant prediction output.",
        "tags": ["Python", "Scikit-Learn", "Random Forest", "Railway"],
        "accuracy": "76% Accuracy",
        "demo": "https://house-price-prediction-production-a868.up.railway.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#3b82f6",
        "live": True,
    },
    {
        "id": 2,
        "title": "Wine Quality Prediction Dashboard",
        "emoji": "🍷",
        "description": "Data-driven dashboard predicting wine quality ratings from chemical property inputs (acidity, alcohol, pH). Deployed on Netlify with a full CI/CD pipeline and ML classification model with responsive frontend.",
        "tags": ["Python", "Scikit-Learn", "Netlify", "CI/CD"],
        "accuracy": None,
        "demo": "https://agent-6990c8ba3ea9ca1bf190a75--jade-kheer-dd6708.netlify.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#8b5cf6",
        "live": True,
    },
    {
        "id": 3,
        "title": "Stock Market Place Dashboard",
        "emoji": "📈",
        "description": "Interactive analytics dashboard for exploring stock market trends and performance metrics. Deployed on Vercel with dynamic charting and real-time data exploration features built with React.",
        "tags": ["JavaScript", "React", "Data Visualization", "Vercel"],
        "accuracy": None,
        "demo": "https://stock-market-place-dashboard-1.vercel.app/",
        "github": "https://github.com/Hashirattari11",
        "color": "#06b6d4",
        "live": True,
    },
    {
        "id": 4,
        "title": "COVID-19 Image Classification",
        "emoji": "🦠",
        "description": "Deep learning model leveraging MobileNetV2 transfer learning to classify COVID-19 chest X-rays. Achieved 83% accuracy with data augmentation and fine-tuning on a medical imaging dataset.",
        "tags": ["TensorFlow", "MobileNetV2", "Transfer Learning", "CNN"],
        "accuracy": "83% Accuracy",
        "demo": "https://github.com/Hashirattari11",
        "github": "https://github.com/Hashirattari11",
        "color": "#ef4444",
        "live": False,
    },
    {
        "id": 5,
        "title": "Cats vs Dogs Image Classification",
        "emoji": "🐱",
        "description": "Custom CNN trained from scratch on the classic cats vs. dogs dataset using data augmentation. Achieved 79% accuracy exploring architecture tuning and regularization strategies.",
        "tags": ["TensorFlow", "CNN", "Data Augmentation", "Deep Learning"],
        "accuracy": "79% Accuracy",
        "demo": "https://github.com/Hashirattari11",
        "github": "https://github.com/Hashirattari11",
        "color": "#f59e0b",
        "live": False,
    },
    {
        "id": 6,
        "title": "Jarvis AI Assistant",
        "emoji": "🎙️",
        "description": "Voice-based AI assistant performing automated tasks, answering natural language queries, and executing system commands. Built with Python speech libraries and NLP for intent understanding.",
        "tags": ["Python", "NLP", "Voice Automation", "Speech Recognition"],
        "accuracy": None,
        "demo": "https://github.com/Hashirattari11",
        "github": "https://github.com/Hashirattari11",
        "color": "#10b981",
        "live": False,
    },
]

messages_store = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "home"})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "page": "about"})

@app.get("/skills", response_class=HTMLResponse)
async def skills(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request, "page": "skills", "skills": SKILLS})

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "page": "projects", "projects": PROJECTS})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "page": "contact"})

@app.post("/contact/submit")
async def submit_contact(
    name: str = Form(...), email: str = Form(...),
    subject: str = Form(...), message: str = Form(...),
):
    messages_store.append({"name": name, "email": email, "subject": subject, "message": message})

    email_sent = send_email(name, email, subject, message)

    if email_sent:
        return JSONResponse({
            "success": True,
            "message": f"Thanks {name}! Your message has been sent — I'll reply to {email} soon. 🚀"
        })
    else:
        return JSONResponse({
            "success": True,
            "message": f"Thanks {name}! Message received. (Note: email notification failed — check Gmail App Password config.)"
        })


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
