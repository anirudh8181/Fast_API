from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix="/items", tags=["items"])

# Data model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: Optional[str] = None

# In-memory database
items_db = {}
item_counter = 1

# Get all items
@router.get("", response_model=List[Item])
async def get_all_items():
    return list(items_db.values())

# Get single item
@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Create new item
@router.post("", response_model=Item)
async def create_item(item: Item):
    global item_counter
    item.id = item_counter
    items_db[item_counter] = item
    item_counter += 1
    return item

# Update item
@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[item_id] = item
    return item

# Delete item
@router.delete("/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# Search with pagination
@router.get("/search/all")
async def search_items(skip: int = 0, limit: int = 10):
    items_list = list(items_db.values())
    return items_list[skip : skip + limit]
