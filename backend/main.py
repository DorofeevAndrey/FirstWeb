from fastapi import FastAPI, HTTPException
from depencies import SessionDependency
from schemas import login
from models import User

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/login")
async def login(session: SessionDependency, login_data: login):
    user = User(**login_data.dict())
    session.add(user)
    try:
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существет")

    return {"name": user.name}
