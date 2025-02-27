from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
def greeting(name: str = "world"):
    return {"message": f"Hello, {name}"}