from fastapi import APIRouter, HTTPException
from db import database, items
from models.items import Item, ItemIn

# Инициализируем APIRouter
router = APIRouter()

# ручка /items, тип - get, вывод всех товаров
@router.get('/items/', response_model=list[Item])
async def get_items():
    items_ = items.select()
    return await database.fetch_all(items_)

# ручка /items, тип - post, создание товара
@router.post('/items/')
async def add_item(item: ItemIn):
    query = items.insert().values(name=item.name, description=item.description, price=item.price)
    await database.execute(query)
    return {'msg': 'Item added'}

# ручка /items, тип - get, вывод конкретного товара по id
@router.get('/items/{id}', response_model=Item)
async def get_item(id: int):
    query = items.select().where(items.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Item not found")

# ручка /items, тип - put, обновление конкретного товара по id
@router.put('/items/{id}', response_model=Item)
async def update_item(id: int, item: ItemIn):
    query = items.update().where(items.c.id == id).values(**item.model_dump())
    result = await database.execute(query)
    if result:
        return {**item.model_dump(), 'id': id}
    raise HTTPException(status_code=404, detail="Item not found")

# ручка /items, тип - delete, удаление конкретного товара по id
@router.delete('/items/')
async def delete_item(id: int):
    query = items.delete().where(items.c.id == id)
    result = await database.execute(query)
    if result:
        return {'msg': 'Item deleted'}
    raise HTTPException(status_code=404, detail="Item not found")
