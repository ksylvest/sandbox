from fastapi import FastAPI

app = FastAPI()


@app.get("/up")
def up():
    return {"Status": "OK"}
