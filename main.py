from typing import Union

from fastapi import FastAPI
from app.routes.api.v1.hand_detection_router import HandGestureDetectionRouter

app = FastAPI(title="SMAGLATOR API")


app.include_router(HandGestureDetectionRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
