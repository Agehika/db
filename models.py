from sqlalchemy import create_engine, func, UniqueConstraint
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date, time
import uuid

engine = create_engine("postgresql://postgres:1340@localhost:5432/spa")

class Specialization(SQLModel, table=True):
    title: str = Field(primary_key=True)
    normative_time: Optional[int] = None

class Employees(SQLModel, table=True):
    id_number: str = Field(primary_key=True)
    last_name: str
    first_name: str
    middle_name: str
    title: Optional[str] = Field(foreign_key="specialization.title") 

class EmployeesSchedule(SQLModel, table=True):
    id_number: str = Field(primary_key=True, nullable=False)
    datee: date = Field(primary_key=True, nullable=False)
    title: str
    start_time: time = Field(primary_key=True, nullable=False)
    normative_time: int

    class Config:
        constraints = [UniqueConstraint("datee", "id_number")]

class Clients(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    last_name: str
    first_name: str
    middle_name: str
    phone_numb: str
    date_of_birth: date

class Record(SQLModel, table=True):
    id: Optional[str]
    datee: date = Field(primary_key=True, nullable=False)
    id_number: str = Field(primary_key=True, nullable=False)
    starting_time: time = Field(primary_key=True, nullable=False)
    title: str

    class Config:
        constraints = [UniqueConstraint("datee", "id_number", "starting_time")]

SQLModel.metadata.create_all(engine)
