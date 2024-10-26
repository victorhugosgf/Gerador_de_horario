from fastapi import FastAPI, HTTPException
from models import Item

app = FastAPI()

db = []

# Create
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

# Read
@app.get("/items/", response_model=list[Item])
def get_items():
    return db

# Read
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            del db[index]
            return {"message": "Item removido com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")
