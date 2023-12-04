import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from validators import User
from memdb import MemDB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
db = MemDB()
db.init()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    users = db.read_all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users")
async def read_users():
    logger.info('Отработал GET запрос /users')
    users = db.read_all()
    return {"users": users}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    logger.info(f'Отработал GET запрос /users/{user_id}')
    user = db.read_by_id(user_id)
    if user:
        try:
            resp_user = User(id=user.id, name=user.name, email=user.email)
            return {"user": resp_user}
        except Exception as e:
            return JSONResponse(content={"error": f"{e}"}, status_code=500)
    return JSONResponse(content={"error": f"no user with id = {user_id} found"}, status_code=404)        

@app.post("/users")
async def create_user(user: User):
    logger.info('Отработал POST запрос /users')
    try:
        user_id = db.create(user)
    except KeyError as e:
        return JSONResponse(content={"error": f"cannot create user = {user.name}: {e}"}, status_code=500)   
    if user_id:
        user.id = user_id
        return {"user": user} 

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    logger.info(f'Отработал PUT запрос /users/{user_id}')
    if user.id != user_id:
        user.id = user_id
    db.update(user)
    return {"user": user}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    logger.info(f'Отработал DELETE запрос /users/{user_id}')
    try:
        db.delete_by_id(user_id)
    except KeyError as e:
        return JSONResponse(content={"error": f"cannot delete user with id = {user_id}: {e}"}, status_code=404)
    return JSONResponse(content={"success": f"user with id = {user_id} was deleted"})