from faker import Faker
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy_utils import create_database, database_exists

connection_string = "mysql+mysqlconnector://root:@127.0.0.1:3306/sat_scores"

fake = Faker()
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student = Column("student", String(128))
    score = Column("score", Integer)


def main():
    Base.metadata.create_all(engine)
    count = 1000
    session.bulk_insert_mappings(
        Student,
        [
            {
                "student": fake.name(),
                "score": fake.pyint(min_value=1700, max_value=2200, step=1),
            }
            for _ in range(count)
        ],
    )
    session.commit()


if __name__ == "__main__":
    main()
