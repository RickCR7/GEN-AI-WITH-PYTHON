from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Akash",
    email="a@gmail.com",
    created_at=datetime(2025,11,12, 11, 4),
    address=Address(
        street = "Something",
        city="Burnpur",
        zip_code = "713325"
    ),
    is_active=False,
    tags=["Premium", "Subscriber"]
)

python_dict = user.model_dump()
print(user)
print("-"*50)
print(python_dict)

json_str = user.model_dump_json()
print("-"*50)
print(json_str)
