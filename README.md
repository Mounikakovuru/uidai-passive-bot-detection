# 🛡️ UIDAI Passive Bot Detection System

A full-stack machine learning–based solution to replace CAPTCHAs with a passive, privacy-friendly bot detection mechanism for UIDAI Aadhaar portals.

---

## 🎯 Objective

To eliminate CAPTCHA from UIDAI's online services by building a **passive detection system** that:
- Collects browser/environmental data silently
- Uses AI/ML to classify users as human or bot
- Ensures user-friendly experience with minimal interaction

---

## 📌 Problem Statement

UIDAI currently uses CAPTCHA to prevent bot-based Denial-of-Service (DoS/DDoS) attacks on its public-facing portals. However, CAPTCHA affects user accessibility and experience.

The solution must:
- Passively detect bots using browser fingerprinting
- Use AI/ML to classify traffic
- Be scalable, privacy-compliant, and non-intrusive

---

## 🧠 Solution Overview

### 🖥️ Frontend (React + TypeScript)
- Collects passive browser/environmental features
- Optional fallback minimal interaction (if needed)
- Sends data to backend for classification

### ⚙️ Backend (FastAPI + Python)
- Accepts environment data via `/analyze` API
- Uses trained ML model (`bot_model.pkl`) to classify
- Returns `is_bot` boolean and confidence score

---

## 📂 Project Structure

uidai_passive_bot_detection/
├── backend/                       # Backend API and ML model
│   ├── main.py                    # FastAPI application entry point
│   ├── requirements.txt           # Backend dependencies
│   └── model/
│       ├── features.py            # Feature engineering logic
│       ├── train_model.py         # Script to train the ML model
│       └── bot_model.pkl          # Trained ML model file (generated after training)
│
├── frontend/                      # React frontend for UIDAI portal simulation
│   ├── public/
│   │   └── index.html             # HTML entry point
│   ├── src/
│   │   ├── App.tsx                # Main component rendering UI
│   │   ├── api.ts                 # API call logic (POST to /analyze)
│   │   ├── dataCollector.ts       # Collects browser environment parameters passively
│   │   └── interactionFallback.ts # Optional fallback for user interaction
│   ├── package.json               # Frontend dependencies
│   └── tsconfig.json              # TypeScript configuration
│
├── data/                          # Datasets used for training
│   ├── raw/
│   │   ├── human_samples.json     # Sample raw human data
│   │   └── bot_samples.json       # Sample raw bot data
│   └── processed/
│       └── dataset.csv            # Final dataset used for ML training
│
├── test/                          # Testing and simulation scripts
│   ├── simulate_bot.py            # Simulates bot environment data to test API
│   └── simulate_human.py          # Simulates human-like behavior to test API
│
├── README.md                      # Project documentation and instructions
└── Uidai_Passive_Bot_Presentation.pptx # Final presentation 


---

## 🧪 How to Run

### 🔹 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python model/train_model.py
uvicorn main:app --reload
➡️ Access API at: http://127.0.0.1:8000/analyze

🔹 Frontend
cd frontend
npm install
npm start

📊 Sample API Input
{
  "data": {
    "userAgent": "Mozilla/5.0",
    "screen": {"width": 1366, "height": 768},
    "hardwareConcurrency": 4,
    "doNotTrack": "0",
    "touchSupport": 1,
    "timezoneOffset": 330,
    "mouseMovement": 15,
    "scrollDepth": 300
  }
}

---
✅ Features Collected
User agent string

Screen dimensions

Hardware concurrency

Touch support

Timezone offset

Mouse movement intensity

Scroll depth

Do Not Track status

------

✅ Key Highlights
⚡ Faster than traditional CAPTCHA

🔒 Privacy-preserving (no personal data)

🔧 Easy integration into UIDAI stack

👥 Enhanced accessibility for all users

🚀 Future Enhancements
Train on more diverse user data

Add adversarial bot detection tests

Dockerize for deployment

Add confidence-based thresholds for fallback UI

-----

📚 References
UIDAI Challenge Document

FingerprintJS

scikit-learn Documentation

FastAPI Documentation

Google reCAPTCHA Technical Papers
