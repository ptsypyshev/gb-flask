from db import db_connect, db_disconnect
from fastapi import FastAPI
from routers.users import router as router_users
from routers.items import router as router_items
from routers.orders import router as router_orders

# Инициализируем FastAPI
app = FastAPI()

# Добавляем группы маршрутов
app.include_router(router_users, tags=["users"])
app.include_router(router_items, tags=["items"])
app.include_router(router_orders, tags=["orders"])

# Инициализируем коннект к БД
app.add_event_handler("startup", db_connect)
app.add_event_handler("shutdown", db_disconnect)
