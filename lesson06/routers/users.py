from fastapi import APIRouter, HTTPException
from db import database, users
from models.users import User, UserIn
from bcrypt import gensalt, checkpw, hashpw

# Инициализируем APIRouter
router = APIRouter()

# ручка /users, тип - get, вывод всех пользователей
@router.get('/users/', response_model=list[User])
async def get_users():
    users_ = users.select()
    return await database.fetch_all(users_)

# ручка /users, тип - post, создание пользователя
@router.post('/users/')
async def add_user(user: UserIn):
    hashed_password = hash_pw(user.password.encode())
    query = users.insert().values(first_name=user.first_name, last_name=user.last_name, email=user.email, password=hashed_password)
    await database.execute(query)
    return {'msg': 'User added'}

# ручка /users, тип - get, вывод конкретного пользователя по id
@router.get('/users/{id}', response_model=User)
async def get_user(id: int):
    query = users.select().where(users.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="User not found")

# ручка /users, тип - put, обновление конкретного пользователя по id
@router.put('/users/{id}', response_model=User)
async def update_user(id: int, user: UserIn):
    user.password = hash_pw(user.password.encode())
    # hashed_password = hash_pw(user.password.encode())
    # user_dict['password'] = 
    query = users.update().where(users.c.id == id).values(**user.model_dump())
    result = await database.execute(query)
    if result:
        return {**user.model_dump(), 'id': id}
    raise HTTPException(status_code=404, detail="User not found")

# ручка /users, тип - delete, удаление конкретного пользователя по id
@router.delete('/users/')
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    result = await database.execute(query)
    if result:
        return {'msg': 'User deleted'}
    raise HTTPException(status_code=404, detail="User not found")

def hash_pw(password):
    return hashpw(password, gensalt())

def verify_pw(password, hashed_password):
    return checkpw(password.encode(), hashed_password)
