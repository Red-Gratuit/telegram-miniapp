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

products = {

    "stup": [
        {"id": 1, "name": "Purple Molt 💜", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup1.mp4", "desc": "Purple Molt 💜 — saveur fruitée intense, effet relaxant et vibes ultra smooth 😮‍💨✨"},
        {"id": 2, "name": "Live Rosin 🍋", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup2.mp4", "desc": "extrait ultra pur, goût naturel puissant et effet premium relaxant 😮‍💨💎"},
        {"id": 3, "name": "Moncler 320mg 💊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup3.mp4", "desc": "Moncler 320 mg 💎 — intensité élevée, sensation premium et performance longue durée ✨🔥"},
        {"id": 4, "name": "Cali Exotic Biscottiz 🍪", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup4.mp4", "desc": "Cali Exotic Biscottiz 🍪 — saveur gourmande, vibes exotiques et sensation premium 🔥💎"},
        {"id": 5, "name": "Cali Shelf Gelato 🍨", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup5.mp4", "desc": "Cali Shelf Gelato 🍨 — douceur crémeuse, vibes cali et sensation ultra premium ✨😮‍💨"},
        {"id": 6, "name": "Shop Jack Herrera 🌿", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup6.mp4", "desc": "Shop NL Premium 🛍️💎 — sélection haut de gamme, qualité au top et vibes ultra clean ✨🔥"},
        {"id": 7, "name": "DrySift Mimosa 🍊", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup7.mp4", "desc": "DrySift Mimosa 🍊 — notes fraîches et pétillantes, vibe élégante et sensation ultra clean 💎"},
        {"id": 9, "name": "Rolex 300mg 💎", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup9.mp4", "desc": "Rolex 300 mg 💎 — intensité élevée, style iconique et sensation ultra premium 🔥"},
        {"id": 10, "name": "Piatella 🍯", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup10.mp4", "desc": "Piatella 🍯 — texture fondante, finition haut de gamme et vibes ultra premium ✨"},
        {"id": 11, "name": "MDMA Champagne 🍾", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup11.mp4", "desc": "MDMA Champagne 🍾 — énergie pétillante, style festif et sensation luxe premium 🔥"},
        {"id": 12, "name": "WPF Sherbet x Piatella 💎", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup12.mp4", "desc": "WPF Sherbet x Piatella 💎 — fusion gourmande, texture soyeuse et vibes luxe premium ✨"},
        {"id": 13, "name": "Jaune Mousseux 🟡", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup13.mp4", "desc": "Jaune Mousseux 🟡 — bulles dorées, style lumineux et vibes élégantes ✨"},
        {"id": 14, "name": "Static Pineapple 🍍", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup14.mp4", "desc": "Static Pineapple 🍍 — fraîcheur tropicale, vibes électriques et sensation premium 🔥"},
        {"id": 17, "name": "Shop NL Premium 💎", "video": "https://telegram-miniapp-581.pages.dev/assets/media/stup/stup17.mp4", "desc": "Shop NL Premium 💎 — sélection haut de gamme, qualité au top et vibes ultra clean ✨🔥"},
    ],

    "puff": [
        {"id": 20, "name": "Alien 10k 👽", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff1.jpg", "desc": "Alien 10k 👽 — intensité maximale, style futuriste et vibes ultra premium ⚡💎"},
        {"id": 21, "name": "Falcon 16k 🦅", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff2.jpg", "desc": "Falcon 16k 🦅 — puissance extrême, sensation fluide et performance haut niveau ⚡💎"},
        {"id": 22, "name": "Shisha Hookah 22k 💨", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff3.jpg", "desc": "Shisha Hookah 22k 💨 — tirage ultra smooth, style premium et vibes longue durée 💎"},
        {"id": 23, "name": "Falcon 28k 🦅", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff4.jpg", "desc": "Falcon 28k 🦅 — puissance ultime, sensation ultra fluide et vibes high-tech premium ⚡💎"},
        {"id": 24, "name": "Falcon 18k 🦅", "image": "https://telegram-miniapp-581.pages.dev/assets/media/puff/puff5.jpg", "desc": "Falcon 18k 🦅 — équilibre parfait, tirage fluide et vibes premium ⚡💎"},
    ],

    "tabac": [
        {"id": 30, "name": "Cartouche 🚬", "video": "https://telegram-miniapp-581.pages.dev/assets/media/tabac/tabac1.mp4", "desc": "Cartouche 🚬 — format pratique, qualité constante et style clean & premium ✨💎"},
    ],

    "info": [
        {
            "id": 999,
            "title": "ℹ️ Informations",
            "text": "CaliFastDrive — Commandes sécurisées et flexibles\n\n"
                    "SUR PLACE 📍 / LIVRAISON RAPIDE 🚚 / ENVOIE MONDIAL RELAY 📩 / PRIX IMBATTABLE‼️\n\n"
                    "📦 Envoie Colis\n"
                    "• Vérification d'identité\n"
                    "• Modes de paiement : CASH, BTC…\n"
                    "• Adresse de livraison complète\n"
                    "• Disponibilités pour la réception\n"
                    "• Détails de la commande\n\n"
                    "📍 Meet-Up\n"
                    "Plusieurs Meet-Up à votre disposition : En privée pour + d’informations..\n\n"
                    "🚚 Livraison\n"
                    "Livraison Disponible dans tous les 59/62 📌"
        }
    ]
}

@app.get("/api/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])

@app.post("/api/init")
def init(data: dict):
    return {"received": data}

@app.get("/api/ping")
def ping():
    return {"ping": "pong"}
