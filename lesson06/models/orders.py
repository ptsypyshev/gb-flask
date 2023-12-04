from pydantic import BaseModel, Field

# pydantic класс для модели order, которая принимается из http-request
class OrderIn(BaseModel):
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    status: int = Field(..., ge=0, le=4)

# pydantic класс для модели order, на основе которой лежат данные в БД
class Order(BaseModel):
    id: int
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    status: int = Field(..., ge=0, le=4)
