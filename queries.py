import models as md 
from sqlmodel import Session, select, join
from sqlalchemy import func, desc, and_
from sqlalchemy import create_engine
import uuid

engine = create_engine("postgresql://postgres:1340@localhost:5432/spa")


# удаление клиента из базы
def deleteClients(id):
    with Session(engine) as session:
        statement = select(md.Clients).where(md.Clients.id == id)
        clients = session.exec(statement).one()
        print("Deleting clients:", clients)
        session.delete(clients)
        session.commit()
        print("Clients deleted successfully")

# добавление нового клиента
def addClients(last_name, first_name, middle_name, phone_numb,
               date_of_birth):
    with Session(engine) as session:
        new_Clients = md.Clients(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            phone_numb=phone_numb,
            date_of_birth=date_of_birth
        )
        session.add(new_Clients)
        session.commit()
        session.refresh(new_Clients)
        print("Added new clients:", new_Clients)

# показать записи специалиста   
def get_record_emp(id_number):
    with Session(engine) as session:
        statement = select(md.Record).where(md.Record.id_number == id_number)
        record = session.exec(statement).all()
        print("Record:", record)

# показать записи клиента   
def get_record_cli(id):
    with Session(engine) as session:
        statement = select(md.Record).where(md.Record.id == id)
        record = session.exec(statement).all()
        print("Record:", record)

# удалить запись клиента
def delete_record(id, datee, starting_time):
    with Session(engine) as session:
        rec = session.exec(select(md.Record).where((md.Record.id == id) &
                                                   (md.Record.datee == datee) &
                                                   (md.Record.starting_time == starting_time))
                           ).first()

        if rec:
            session.delete(rec)
            session.commit()
            print("Delete record")
        else:
            print("Record not found")

# записать клиента на процедуру     
def make_record(id, datee, id_number, starting_time):
    with Session(engine) as session:
        record = session.exec(select(md.EmployeesSchedule).where(
                             (md.EmployeesSchedule.datee == datee) &
                             (md.EmployeesSchedule.id_number == id_number) &
                             (md.EmployeesSchedule.start_time == starting_time)
                              )).first()
        title = session.query(md.Employees.title).filter(md.Employees.id_number==id_number)

        if record:
            new_Record = md.Record(id=id,
                                   datee=datee,
                                   id_number=id_number,
                                   starting_time=starting_time,
                                   title=title)
            session.add(new_Record)
            session.commit()
            session.refresh(new_Record)
            print("Added new record:", new_Record)
        else:
            print("Incorrect data")

# свободное время для записи на процедуру в определенную дату
def free_record(datee, title):
    with Session(engine) as session:
        
        record = session.exec(select(md.EmployeesSchedule.start_time).where(
                             (md.EmployeesSchedule.datee == datee) &
                             (md.EmployeesSchedule.title == title))).all()
        
        record1 = session.exec(select(md.Record.starting_time).where((md.Record.datee == datee)&(md.Record.title == title))).all()
        record2 = list(set(record) - set(record1))

        if record2:
            print("Free record:", record2)
        else:
            print("Incorrect data")
