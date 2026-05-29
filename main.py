from fastapi import FastAPI
from model import Recommender
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

model = Recommender()

# allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    return {
        "user_id": user_id,
        "recommendations": model.recommend(user_id)
    }