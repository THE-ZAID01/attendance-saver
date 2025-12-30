from fastapi import FastAPI

app = FastAPI(title="Attendance Saver API")

@app.get("/health")
def health():
    return {"status": "ok"}
