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
        {"id": 1, "name": "Purple Molt 🏴‍☠️", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup1.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 2, "name": "Live Rosin 🍋", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup2.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 3, "name": "Moncler 320Mg 💊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup3.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 4, "name": "Cali Exotic Biscottiz 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup4.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 5, "name": "Cali Shelf Gelato 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup5.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 6, "name": "Shop Jack Herrer 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup6.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 7, "name": "Drysift Mimosa 🍫", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup7.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 9, "name": "Rolex 300Mg 💊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup9.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 10, "name": "Piatella 🥶", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup10.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 11, "name": "Mdma Champagne 🍾", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup11.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 12, "name": "Wpff Sherbet X Piatella 🍯", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup12.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 13, "name": "Jaune Mousseux 🟡", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup13.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 14, "name": "Static Pineapple 🍍", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup14.mp4","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 17, "name": "Shop Nl Prenium 🪴", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup17.mp4","desc":"Qualité premium, goût intense et effet longue durée"}
    ],

    "puff": [
        {"id": 20, "name": "Alien 10k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff1.jpg","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 21, "name": "Falcon 16k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff2.jpg","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 22, "name": "Shisha Hookah 22k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff3.jpg","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 23, "name": "Falcon 28k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff4.jpg","desc":"Qualité premium, goût intense et effet longue durée"},
        {"id": 24, "name": "Falcon 18k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff5.jpg","desc":"Qualité premium, goût intense et effet longue durée"}
    ],

    "tabac": [
        {"id": 30, "name": "Cartouche 🚬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/tabac/tabac1.mp4","desc":"Qualité premium, goût intense et effet longue durée"}
    ],

    "info": [
        {
            "id": 100,
            "title": "📦 Livraison",
            "text": "Livraison rapide en moins de 30 minutes selon votre zone."
        },
        {
            "id": 101,
            "title": "🔒 Discrétion",
            "text": "Emballage discret et paiement sécurisé."
        },
        {
            "id": 102,
            "title": "📍 Zones",
            "text": "Nous livrons dans toute la région."
        }
    ]
}

@app.get("/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])