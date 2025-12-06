import logging
from typing import Annotated
from pydantic import BaseModel


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MyClass(BaseModel):
    id: int
    name: str

d = {
    "id": 167,
    "name": "ygug"
}

try:
    obj = MyClass(**d)
    print(obj)
    logging.info(f"Object created successfully: {obj}")
except Exception as e:
    print("Error:", e)
    logging.error(f"Validation failed: {e}")
