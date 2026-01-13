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
    "info": [
        {
            "id": 99,
            "title": "📦 Livraison",
            "text": "Livraison rapide dans toute la ville. 30–60 minutes selon zone."
        },
        {
            "id": 100,
            "title": "🕒 Horaires",
            "text": "Ouvert tous les jours de 18h à 04h."
        },
        {
            "id": 101,
            "title": "📲 Contact",
            "text": "Contactez-nous directement sur Telegram : @xr_shop_test_bot"
        }
    ],

    "stup": [
  {"id":1,"name":"STUP 1","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup1.mp4"},
  {"id":2,"name":"STUP 2","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup2.mp4"},
  {"id":3,"name":"STUP 3","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup3.mp4"},
  {"id":4,"name":"STUP 4","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup4.mp4"},
  {"id":5,"name":"STUP 5","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup5.mp4"},
  {"id":6,"name":"STUP 6","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup6.mp4"},
  {"id":7,"name":"STUP 7","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup7.mp4"},
  {"id":9,"name":"STUP 9","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup9.mp4"},
  {"id":10,"name":"STUP 10","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup10.mp4"},
  {"id":11,"name":"STUP 11","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup11.mp4"},
  {"id":12,"name":"STUP 12","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup12.mp4"},
  {"id":13,"name":"STUP 13","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup13.mp4"},
  {"id":14,"name":"STUP 14","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup14.mp4"},
  {"id":17,"name":"STUP 17","video":"https://telegram-miniapp-581.pages.dev/assets/media/stup/stup17.mp4"}
],

"puff": [
  {
    "id": 20,
    "name": "PUFF 1",
    "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff1.jpg"
  },
  {
    "id": 21,
    "name": "PUFF 2",
    "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff2.jpg"
  },
  {
    "id": 22,
    "name": "PUFF 3",
    "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff3.jpg"
  },
  {
    "id": 23,
    "name": "PUFF 4",
    "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff4.jpg"
  },
  {
    "id": 24,
    "name": "PUFF 5",
    "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff5.jpg"
  }
]

  "tabac": [
  {
    "id": 30,
    "name": "TABAC",
    "video": "https://telegram-miniapp-581.pages.dev/assets/media/tabac/tabac1.mp4"
  }
]
}

@app.get("/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])