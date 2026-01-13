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
        {"id":1,"name":"STUP 1","price":"15€","video":"https://cdn.pixabay.com/video/2023/09/03/178307-861779302_large.mp4"},
        {"id":2,"name":"STUP 2","price":"15€","video":"https://cdn.pixabay.com/video/2023/08/31/177876-860787987_large.mp4"},
        {"id":3,"name":"STUP 3","price":"15€","video":"https://cdn.pixabay.com/video/2023/03/10/154331-807109997_large.mp4"},
        {"id":4,"name":"STUP 4","price":"15€","video":"https://cdn.pixabay.com/video/2023/07/24/173568-847726095_large.mp4"},
        {"id":5,"name":"STUP 5","price":"15€","video":"https://cdn.pixabay.com/video/2023/02/20/150621-800567532_large.mp4"},
        {"id":6,"name":"STUP 6","price":"15€","video":"https://cdn.pixabay.com/video/2023/03/28/156841-812831195_large.mp4"},
        {"id":7,"name":"STUP 7","price":"15€","video":"https://cdn.pixabay.com/video/2023/04/10/160789-820949911_large.mp4"},
        {"id":8,"name":"STUP 8","price":"15€","video":"https://cdn.pixabay.com/video/2023/05/10/164209-828336023_large.mp4"},
        {"id":9,"name":"STUP 9","price":"15€","video":"https://cdn.pixabay.com/video/2023/06/15/169852-842736441_large.mp4"},
        {"id":10,"name":"STUP 10","price":"15€","video":"https://cdn.pixabay.com/video/2023/07/01/172543-846287764_large.mp4"},
        {"id":11,"name":"STUP 11","price":"15€","video":"https://cdn.pixabay.com/video/2023/08/05/175432-853281554_large.mp4"},
        {"id":12,"name":"STUP 12","price":"15€","video":"https://cdn.pixabay.com/video/2023/08/20/176543-857291143_large.mp4"},
        {"id":13,"name":"STUP 13","price":"15€","video":"https://cdn.pixabay.com/video/2023/09/01/178001-860901233_large.mp4"}
    ],
    "puff": [
        {"id":20,"name":"PUFF BLUE","price":"10€","image":"https://picsum.photos/400/600?1"},
        {"id":21,"name":"PUFF RED","price":"10€","image":"https://picsum.photos/400/600?2"},
        {"id":22,"name":"PUFF GREEN","price":"10€","image":"https://picsum.photos/400/600?3"},
        {"id":23,"name":"PUFF GOLD","price":"10€","image":"https://picsum.photos/400/600?4"},
        {"id":24,"name":"PUFF BLACK","price":"10€","image":"https://picsum.photos/400/600?5"}
    ],
    "tabac": [
        {"id":30,"name":"TABAC PREMIUM","price":"12€","video":"https://cdn.pixabay.com/video/2023/07/24/173568-847726095_large.mp4"}
    ]
}

@app.get("/products/{cat}")
def get_products(cat: str):
    return products.get(cat, [])