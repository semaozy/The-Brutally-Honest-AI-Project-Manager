from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database as db
import os
from groq import Groq
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

# GÖREVLERİ GETİR
@app.get("/tasks")
def get_tasks(session: Session = Depends(get_db)):
    return session.query(db.Task).all()

# YENİ GÖREV EKLE
@app.post("/tasks")
def create_task(title: str, priority: str = "Orta", session: Session = Depends(get_db)):
    new_task = db.Task(title=title, priority=priority)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

# GÖREVİ SİL
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_db)):
    task = session.query(db.Task).filter(db.Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return {"message": "İmha edildi."}
    return {"error": "Bulunamadı."}

# AI ANALİZÖR
@app.get("/ai-analyze")
def analyze_tasks(session: Session = Depends(get_db)):
    tasks = session.query(db.Task).all()
    if not tasks:
        return {"analysis": "Sistem boş. Kaçmak bir çözüm mü yoksa yeni bir başlangıç mı?"}
    
    task_list = ", ".join([t.title for t in tasks])
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Sen Viranora'nın sert ve dürüst AI asistanısın. Türkçe konuşuyorsun. Kullanıcıyı sertçe eleştir."},
                {"role": "user", "content": f"Görevler: {task_list}. Maksimum 20 kelime."}
            ],
            model="llama-3.3-70b-versatile",
        )
        return {"analysis": chat_completion.choices[0].message.content}
    except Exception as e:
        return {"analysis": f"AI meşgul: {str(e)}"}