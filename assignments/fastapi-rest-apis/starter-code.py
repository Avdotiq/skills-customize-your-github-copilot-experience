from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True

items: Dict[int, Item] = {
    1: Item(name="Laptop", description="Portable computer", price=999.99, available=True),
    2: Item(name="Notebook", description="Paper notebook", price=4.99, available=True),
}

@app.get("/items")
def read_items():
    return list(items.values())

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items")
def create_item(item: Item):
    next_id = max(items.keys(), default=0) + 1
    items[next_id] = item
    return {"id": next_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}
