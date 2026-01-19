from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()
class Item(BaseModel):
    name: str
    price: float
db={
}

counter=1

@app.post("/items")
def create_item(item: Item):
    global counter
    db[counter]=item
    counter+=1
    return {"id": counter -1, "item": item}

@app.get("/items")
def read_items():
    return db

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item topilmadim")
    return db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item toplmadi")
    db[item_id]= item
    return {"id": item_id, "item": item}

@app.delete("items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="item yo'q")
    
    del db[item_id]
    return {"message": "Item end oramizda yo'q"}
    