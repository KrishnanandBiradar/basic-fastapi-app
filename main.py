from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

# Endpoint items: Request body with path parameters
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/status/user")
def userinfo():
    return {"message": f"This user is Active"}

@app.get("/status/{course_id}")
def course(course_id: int):
    return {"message": f"This course id:{course_id} status is Active"}

