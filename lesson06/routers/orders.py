from fastapi import APIRouter, HTTPException
from db import database, orders
from models.orders import Order, OrderIn

# Инициализируем APIRouter
router = APIRouter()

# ручка /orders, тип - get, вывод всех заказов
@router.get('/orders/', response_model=list[Order])
async def get_orders():
    orders_ = orders.select()
    return await database.fetch_all(orders_)

# ручка /orders, тип - post, создание заказа
@router.post('/orders/')
async def add_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, item_id=order.item_id, status=order.status)
    await database.execute(query)
    return {'msg': 'Order added'}

# ручка /orders, тип - get, вывод конкретного заказа по id
@router.get('/orders/{id}', response_model=Order)
async def get_order(id: int):
    query = orders.select().where(orders.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Order not found")

# ручка /orders, тип - put, обновление конкретного заказа по id
@router.put('/orders/{id}', response_model=Order)
async def update_order(id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == id).values(**order.model_dump())
    result = await database.execute(query)
    if result:
        return {**order.model_dump(), 'id': id}
    raise HTTPException(status_code=404, detail="Order not found")

# ручка /orders, тип - delete, удаление конкретного заказа по id
@router.delete('/orders/')
async def delete_order(id: int):
    query = orders.delete().where(orders.c.id == id)
    result = await database.execute(query)
    if result:
        return {'msg': 'Order deleted'}
    raise HTTPException(status_code=404, detail="Order not found")
