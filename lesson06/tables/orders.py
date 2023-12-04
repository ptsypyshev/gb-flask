from sqlalchemy import Column, Integer, MetaData, Table, ForeignKey, ForeignKeyConstraint

# Получаем таблицу orders для БД
def get_orders_table(metadata: MetaData) -> Table:
    return Table(
        "orders",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("user_id", Integer),
        Column("item_id", Integer),
        Column("status", Integer),
        ForeignKeyConstraint(['user_id'], ['users.id']),
        ForeignKeyConstraint(['item_id'], ['items.id'])
    )
