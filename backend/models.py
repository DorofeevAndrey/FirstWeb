import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker
import atexit

load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')
DB = os.getenv('POSTGRES_DB')

DSN = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))


Base.metadata.create_all(bind=engine)
