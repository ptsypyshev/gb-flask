from pydantic import BaseModel, EmailStr, Field, field_validator

BCRYPT_HASHED_PW_LEN = 60

# pydantic класс для модели user, которая принимается из http-request
class UserIn(BaseModel):
    first_name: str = Field(..., max_length=32)
    last_name: str = Field(..., max_length=32)
    email: EmailStr = Field(..., max_length=128)
    password: str

    @field_validator("password")
    def check_password(cls, value):
        # Проверка на то, что пароль - это строка
        value = str(value)
        # Проверка на сложность пароля
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must have at least one digit")
        return value

# pydantic класс для модели user, на основе которой лежат данные в БД
class User(BaseModel):
    id: int    
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=BCRYPT_HASHED_PW_LEN, max_length=BCRYPT_HASHED_PW_LEN)
