import databases
import sqlalchemy
from sqlalchemy import event
from tables.users import get_users_table
from tables.items import get_items_table
from tables.orders import get_orders_table

# Инициализизруем БД
DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)

# Добавляем таблицы в БД
metadata = sqlalchemy.MetaData()
users = get_users_table(metadata)
items = get_items_table(metadata)
orders = get_orders_table(metadata)

# Создаем и запускае движок БД
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)

# Асинхронно подключаемся к БД
async def db_connect():
    await database.connect()

# Асинхронно отключаемся от БД
async def db_disconnect():
    await database.disconnect()


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()