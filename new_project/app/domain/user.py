from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    role: str
    location: str
    skills: List[str]
