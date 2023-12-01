from pydantic import BaseModel, Field

# pydantic класс для модели item, которая принимается из http-request
class ItemIn(BaseModel):
    name: str = Field(..., max_length=128)
    description: str = Field(max_length=1024)
    price: float = Field(..., gt=0)

# pydantic класс для модели item, на основе которой лежат данные в БД
class Item(BaseModel):
    id: int    
    name: str = Field(..., max_length=128)
    description: str = Field(max_length=1024)
    price: float = Field(..., gt=0)
