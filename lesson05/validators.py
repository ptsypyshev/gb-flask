from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator, Field

class User(BaseModel):
    id: Optional[int] = Field(None, ge=0, description="An optional field with a minimum value of 0")
    name: str
    email: EmailStr
    password: Optional[str] = None

    @field_validator("password")
    def check_password(cls, value):
        # convert the password to a string if it is not already
        value = str(value)
        # check that the password has at least 8 characters, one uppercase letter, one lowercase letter, and one digit
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must have at least one digit")
        return value