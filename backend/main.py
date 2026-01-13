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
products = {
    "stup": [
        {
            "id": 1,
            "name": "STUP OG",
            "price": "15€",
            "video": "https://cdn.pixabay.com/video/2023/09/03/178307-861779302_large.mp4"
        },
        {
            "id": 2,
            "name": "STUP ICE",
            "price": "20€",
            "video": "https://cdn.pixabay.com/video/2023/08/31/177876-860787987_large.mp4"
        }
    ],
    "puff": [
        {
            "id": 3,
            "name": "PUFF BLUE",
            "price": "10€",
            "video": "https://cdn.pixabay.com/video/2023/03/10/154331-807109997_large.mp4"
        }
    ],
    "tabac": [
    {
        "id": 4,
        "name": "TABAC GOLD",
        "price": "12€",
        "video": "https://cdn.pixabay.com/video/2023/07/24/173568-847726095_large.mp4"
    }
]
}

@app.get("/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])

