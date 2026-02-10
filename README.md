# The Brutally Honest AI Project Manager

> **"Bahaneleri bırak. Gerçeklerle yüzleş. Harekete geç."**

Viranora, minimalist tasarımın nostaljiyle buluştuğu, yapay zeka destekli bir stratejik yönetim aracıdır. Sıradan proje yönetim araçlarının aksine, Viranora size nazik davranmaz. Görevlerinizi analiz eder, mantık hatalarınızı yüzünüze vurur ve sizi daha dürüst bir çalışma disiplinine zorlar.

---

## 🇹🇷 Proje Özeti (Turkish)

Viranora, modern yazılım dünyasının "uysal" araçlarına bir başkaldırıdır. Groq Cloud (Llama 3.3) altyapısını kullanarak görev listenizi bir aynaya dönüştürür.

### ✨ Temel Özellikler
* **Acımasız AI Analizör:** Görev listenizdeki tembelliği ve plansızlığı anında tespit eder.
* **Minimalist & Mat Tasarım:** Göz yormayan, sofistike ve nostaljik "Analog-Future" estetiği.
* **Full-Stack Mimari:** FastAPI (Backend) ve React (Frontend) ile yüksek performans.
* **Kalıcı Veri Yönetimi:** SQLite ve SQLAlchemy ile güvenli görev takibi.
* **İmha Mekanizması:** Görevleri sadece silmez, onları sistemden "imha" eder.

---

## 🇬🇧 Project Overview (English)

Viranora is an AI-powered strategic management tool where minimalist design meets nostalgic aesthetics. Unlike polite project tools, Viranora uses AI to strip away your excuses and confront you with the reality of your productivity.

### ✨ Key Features
* **Brutally Honest AI:** Powered by Groq (Llama 3.3) to expose procrastination in your workflow.
* **Matte & Sophisticated UI:** A unique, distraction-free "Analog-Future" visual experience.
* **Full-Stack Performance:** Built with FastAPI for speed and React for seamless interaction.
* **Data Persistence:** Reliable task management using SQLite and SQLAlchemy.
* **Task Destruction:** Tasks aren't just deleted; they are strategically "decommissioned."

---

## 🛠️ Tech Stack / Teknolojik Altyapı

* **Frontend:** React.js, Tailwind CSS, Axios
* **Backend:** Python, FastAPI, SQLAlchemy
* **Database:** SQLite
* **AI Engine:** Groq Cloud API (Llama-3.3-70b-versatile)

---

## 🚀 Setup / Kurulum

### 1. Backend

cd backend
python3 -m venv venv
source venv/bin/activate  # Windows için: .\venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy groq python-dotenv
 .env dosyası oluşturun ve ekleyin: GROQ_API_KEY=your_key
uvicorn main:app --reload

### 2. Frontend

cd frontend
npm install
npm start

by sema
