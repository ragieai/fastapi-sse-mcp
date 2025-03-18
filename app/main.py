from fastapi import FastAPI
from app.sse import sse

app = FastAPI()

# Mount the Starlette app to the FastAPI app
app.mount("/", sse)


@app.get("/")
def read_root():
    return {"Hello": "World"}
