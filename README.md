<<<<<<< HEAD
# POCKET-SMART-AI-
POCKET SMART AI - your smart budget and recommendation assistant 
=======
# PocketSmart AI 🤖💰

PocketSmart AI is an AI-powered budget planning and recommendation assistant built with FastAPI, HTML, CSS, JavaScript, and Google Gemini.

It helps users create budget-based recommendations for:

- 🏠 Home Interior Planning
- 🎉 Party Planning
- 💎 Jewelry Planning

The system accepts the user's budget and requirements, sends them to the FastAPI backend, and uses Gemini AI to generate personalized recommendations.

---

## ✨ Features

### 🏠 Home Planner
Users can provide:

- Budget
- Room type
- Number of lights
- Number of fans
- Dining table quantity
- Additional requirements

The system generates an AI-powered home planning recommendation based on the given budget.

### 🎉 Party Planner
Users can provide:

- Budget
- Number of guests
- Occasion
- Venue
- Food preference
- Additional requirements

The system generates a budget-aware party recommendation.

### 💎 Jewelry Planner
Users can provide:

- Budget
- Occasion
- Jewelry style
- Preferred jewelry
- Additional requirements
- Optional outfit image

The system generates personalized jewelry recommendations.

---

## 🤖 AI Integration

PocketSmart AI uses Google Gemini to generate recommendations.

The general workflow is:

User Input
↓
Frontend
↓
FastAPI Backend
↓
Gemini AI
↓
AI Recommendation
↓
Recommendation Page

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### AI

- Google Gemini API
- Google GenAI Python SDK

### Development Tools

- VS Code
- Git
- GitHub
- uv

---

## 📁 Project Structure

```text
project pocketsmart AI/
│
├── frontend/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── home-planner.html
│   ├── home-recommendations.html
│   ├── party-planner.html
│   ├── party-recommendations.html
│   ├── jewelry-planner.html
│   ├── jewelry-recommendations.html
│   └── history.html
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   └── services/
│       ├── __init__.py
│       └── gemini_service.py
│
├── main.py
├── pyproject.toml
├── .env
└── .gitignore
>>>>>>> 9f6e01b (Initial PocketSmart AI project)
