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
        {"id": 1, "name": "Purple Molt 🏴‍☠️", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup1.mp4","desc":"Purple Molt 💜🔥 — saveur fruitée intense, effet relaxant et vibes ultra smooth 😮‍💨✨"},
        {"id": 2, "name": "Live Rosin 🍋", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup2.mp4","desc":"extrait ultra pur, goût naturel puissant et effet premium relaxant 😮‍💨💎"},
        {"id": 3, "name": "Moncler 320Mg 💊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup3.mp4","desc":"Moncler 320 mg 💎⚡ — intensité élevée, sensation premium et performance longue durée 🚀✨"},
        {"id": 4, "name": "Cali Exotic Biscottiz 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup4.mp4","desc":"Cali Exotic Biscottiz 🍪✨ — saveur gourmande, vibes exotiques et sensation premium 💎🔥"},
        {"id": 5, "name": "Cali Shelf Gelato 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup5.mp4","desc":"Cali Sheld Gelato 💜🍨 — douceur crémeuse, vibes cali et sensation ultra premium ✨😮‍💨"},
        {"id": 6, "name": "Shop Jack Herrer 🥬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup6.mp4","desc":"DrySift Mimosa 🍊✨ — notes fraîches et pétillantes, vibe élégante et sensation ultra clean 💎🔥"},
        {"id": 7, "name": "Drysift Mimosa 🍫", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup7.mp4","desc":"Rolex 300 mg ⌚💎 — intensité élevée, style iconique et sensation ultra premium ✨🔥"},
        {"id": 9, "name": "Rolex 300Mg 💊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup9.mp4","desc":"Piatella 💎🍯 — texture fondante, finition haut de gamme et vibes ultra premium ✨😮‍💨"},
        {"id": 10, "name": "Piatella 🥶", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup10.mp4","desc":"WPFF Sherbet × Piatella 🍧💎 — fusion gourmande, texture soyeuse et vibes ultra premium ✨😮‍💨"},
        {"id": 11, "name": "Mdma Champagne 🍾", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup11.mp4","desc":"MDMA Champagne 🥂✨ — énergie pétillante, style festif et sensation luxe premium 💎🔥"},
        {"id": 12, "name": "Wpff Sherbet X Piatella 🍯", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup12.mp4","desc":"Static Pineapple 🍍⚡ — fraîcheur tropicale, vibes électriques et sensation premium ✨🔥"},
        {"id": 13, "name": "Jaune Mousseux 🟡", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup13.mp4","desc":"Jaune Mousseux 🥂💛 — bulles dorées, style lumineux et vibes élégantes ✨🍾"},
        {"id": 14, "name": "Static Pineapple 🍍", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup14.mp4","desc":"Static Pineapple 🍍⚡ — fraîcheur tropicale, vibes électriques et sensation premium ✨🔥"},
        {"id": 17, "name": "Shop Nl Prenium 🪴", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup17.mp4","desc":"Shop NL Premium 🛍️💎 — sélection haut de gamme, qualité au top et vibes ultra clean ✨🔥"}
    ],

    "puff": [
        {"id": 20, "name": "Alien 10k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff1.jpg","desc":"Alien 10K 👽💚 — intensité maximale, style futuriste et vibes ultra premium ⚡💎"},
        {"id": 21, "name": "Falcon 16k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff2.jpg","desc":"Falcon 16K 💨🦅 — puissance extrême, sensation fluide et performance haut niveau ⚡💎"},
        {"id": 22, "name": "Shisha Hookah 22k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff3.jpg","desc":"Shisha Hookah 22K 💨🔥 — tirage ultra smooth, style premium et vibes lounge luxe ✨💎"},
        {"id": 23, "name": "Falcon 28k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff4.jpg","desc":"Falcon 28K 💨🚀 — puissance ultime, sensation ultra fluide et vibes high-tech premium ⚡💎"},
        {"id": 24, "name": "Falcon 18k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff5.jpg","desc":"Falcon 18K 💨🦅 — équilibre parfait, tirage fluide et vibes premium ⚡💎"}
    ],

    "tabac": [
        {"id": 30, "name": "Cartouche 🚬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/tabac/tabac1.mp4","desc":"Cartouche 🚬📦 — format pratique, qualité constante et style clean & premium ✨💎"}
    ],

    "info": [
        {
            "id": 100,
            "title": "SUR PLACE📍/ LIVRAISON RAPIDE 🚚 / ENVOIE MONDIAL RELAY 📩 / PRIX IMBATTABLE‼️",
            "text": "Livraison Disponible dans tous les 59/62 📌"
        },
        {
            "id": 101,
            "title": "📦 Envoie Colis",
            "text": "Pour un traitement rapide, veuillez fournir : Vérification d identité (nouveaux clients) L adresse de livraison complète Vos disponibilités pour la réception Les détails de votre commande Vérification d'identité Modes de paiement : CASH, BTC…."
        },
        {
            "id": 102,
            "title": "📍 Meet-Up",
            "text": "Plusieurs Meet-Up à votre disposition : En privée pour + d’informations.."
        }
    ]
}

@app.get("/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])