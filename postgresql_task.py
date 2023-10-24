import os
import psycopg2
from random import choice, randint
import sqlalchemy
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base, Session
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('POSTGRES_PASSWORD')

engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres")
Base = declarative_base()
session = Session(engine)


class Books(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    author_name = Column(String(100), nullable=False)
    author_surname = Column(String(100), nullable=False)
    book_name = Column(String(100), nullable=False, unique=True)
    pages_amount = Column(Integer, nullable=False)


Base.metadata.create_all(engine)

authors = ['Лев Толстой', 'Иван Бунин', 'Александр Пушкин', 'Николай Гоголь', 'Сергей Есенин', 'Жюль Верн', 'Марк Твен']
book_names = ['Гамлет', 'Отелло', 'Ким', 'Повелитель мух', 'Золотая тетрадь', 'Сердце тьмы', 'Война и мир', 'На маяк']

for i in range(500):
    author = choice(authors).split(" ")
    author_name = author[0]
    author_surname = author[1]
    book_name = choice(book_names) + str(i)
    pages_amount = randint(50, 1000)
    book = Books(author_name=author_name, author_surname=author_surname, book_name=book_name, pages_amount=pages_amount)
    session.add(book)
    session.commit()

q = session.query(sqlalchemy.func.avg(Books.pages_amount)).one()
for data in q:
    print(f"Среднее количество страниц: {int(data)}")

q2 = session.query(Books.author_name, Books.author_surname, sqlalchemy.func.count()).\
    group_by(Books.author_name, Books.author_surname).all()

for data in q2:
    print(f"{data[0]} {data[1]}: {data[2]} книг")

session.query(Books).delete()
session.commit()
