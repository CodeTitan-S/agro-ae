from fastapi import FastAPI

app = FastAPI(title="AgroAE API")

@app.get("/")
def read_root():
    return {"status": "AgroAE API is running"}