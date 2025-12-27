from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


add = Address(
    street="123 abc",
    city="Burnpur",
    postal_code="713325"
)

user = User(
    id=1,
    name="Akash",
    address=add
)

user_data = {
    "id": 1,
    "name": "Akash",
    "address": {
        "street": "321 bgh",
        "city": "Asansol",
        "postal_code": "713304"
    }
}

user = User(**user_data)
print(user)