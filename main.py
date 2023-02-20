from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from sqlalchemy.orm import declarative_base

from models import StudentGroup, Student, Base


engine = create_engine("mysql+pymysql://root:qwerty123@localhost/alchemy_project")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

while True:
    name = input("Введите название группы: ")
    start = input("Введите время начало группы: ")
    end = input("Введите время завершение обучение: ")
    group = StudentGroup(name = name, start = start, end = end)
    session.add(group)
    session.commit()
    message = "Желаете ли вы, завершить работу программы, введите Y,y, если нет просто enter"
    text = input(message)
    if text.lower() == "y":
        break
