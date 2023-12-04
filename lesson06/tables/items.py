from sqlalchemy import Column, Integer, Float, String, MetaData, Table

# Получаем таблицу items для БД
def get_items_table(metadata: MetaData) -> Table:
    return Table(
        "items",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(128)),
        Column("description", String(1024)),
        Column("price", Float),
    )
