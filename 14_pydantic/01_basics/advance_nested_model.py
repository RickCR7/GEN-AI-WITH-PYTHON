from pydantic import BaseModel
from typing import Optional, List, Union

# optional nested models
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

# Mixed Data types
class TextContent(BaseModel):
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]] 

# Deeply nested structures
class Country(BaseModel):
    name: str
    code: str   

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organiztion(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []