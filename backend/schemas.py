from pydantic import BaseModel


class login(BaseModel):
    name: str
    password: str
