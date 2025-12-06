from typing import Annotated
from pydantic import BaseModel

class MyClass(BaseModel):
    id: int
    name: str
d={
    "id":167,
    "name":"ygug"
}

obj = MyClass(**d)
print(obj)
