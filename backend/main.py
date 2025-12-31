from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)
