from sqlalchemy import Column, Integer, String, MetaData, Table

# Получаем таблицу users для БД
def get_users_table(metadata: MetaData) -> Table:
    return Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("first_name", String(32)),
        Column("last_name", String(32)),
        Column("email", String(128)),
        Column("password", String(128)),
    )
