from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sum")
def do_sum(a: int, b: int):
    return {"result": a + b}
