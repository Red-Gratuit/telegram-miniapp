from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Telegram Mini App backend running"}

@app.post("/init")
def init(data: dict):
    return {
        "received": data,
        "message": "Connected to Telegram Mini App"
    }
