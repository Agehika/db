import models as md 
from sqlalchemy import create_engine
import uuid
from datetime import date, timedelta, time
from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("postgresql://postgres:1340@localhost:5432/spa")

def spe_data():
    one = md.Specialization(title="Маникюр", normative_time=60)
    two = md.Specialization(title="Педикюр", normative_time=30)
    three = md.Specialization(title="Массаж лица", normative_time=30)
    four = md.Specialization(title="Полный массаж", normative_time=60)
    five = md.Specialization(title="SPA для волос", normative_time=30)
   
    md.SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(one)
        session.add(two)
        session.add(three)
        session.add(four)
        session.add(five)

        session.commit()


def ins_data():

    one3 = md.Employees(id_number="1111", last_name="Иванова", first_name="Инна", middle_name="Ивановна", title="Маникюр")
    two3 = md.Employees(id_number="2222", last_name="Сидорова", first_name="Анна", middle_name="Олеговна", title="Педикюр")
    three3 = md.Employees(id_number="3333", last_name="Васина", first_name="Мила", middle_name="Сергеевна", title="Массаж лица")
    four3 = md.Employees(id_number="4444", last_name="Логинова", first_name="Мария", middle_name="Михайловна", title="Полный массаж")
    five3 = md.Employees(id_number="5555", last_name="Миронова", first_name="Ольга", middle_name="Игоревна", title="SPA для волос")
 
    one4 = md.Clients(id=uuid.uuid4(),last_name="Кирова", first_name="Анна", middle_name="Юрьевна", phone_numb="89112388811",date_of_birth=date(2000,2,10))
    two4 = md.Clients(id=uuid.uuid4(),last_name="Князева", first_name="Инга", middle_name="Михайловна", phone_numb="89119998811", date_of_birth=date(1995,10,15))
    three4 = md.Clients(id=uuid.uuid4(),last_name="Попова", first_name="Лариса", middle_name="Олеговна", phone_numb="89113338811",date_of_birth=date(1965,12,3))
    four4 = md.Clients(id=uuid.uuid4(),last_name="Любимова", first_name="Зоя", middle_name="Игоревна", phone_numb="89115556677",date_of_birth=date(1975,10,5))
    five4 = md.Clients(id=uuid.uuid4(),last_name="Павлова", first_name="Дарья", middle_name="Юрьевна", phone_numb="89112238843",date_of_birth=date(1999,2,28))
   
    md.SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
     
        session.add(one3)
        session.add(two3)
        session.add(three3)
        session.add(four3)
        session.add(five3)
        
        session.add(one4)
        session.add(two4)
        session.add(three4)
        session.add(four4)
        session.add(five4)
     
        session.commit()

def shc_data():
    with Session(engine) as session:
        emp = session.query(md.Employees.id_number).all()
    
        for idd in emp:
            datee = date(2024, 12, 10)
            id_emp = str(idd)[2:6]
            title = session.query(md.Employees.title).filter(md.Employees.id_number==id_emp)
            stop = datee + timedelta(days=4)
            while datee <= stop:
                start_time = time(10,0)
                normative_time = session.query(md.Specialization.normative_time).filter(md.Specialization.title==title).scalar()
                i = 0
                while i <= 5:
                    session.add(md.EmployeesSchedule(id_number=id_emp,datee=datee,title=title,start_time=start_time,normative_time=normative_time))
                    secs = start_time.hour * 3600 + start_time.minute * 60 + start_time.second
                    secs += normative_time * 60
                    start_time = time(secs // 3600, (secs % 3600) // 60, secs % 60)
                    i+=1
                datee += timedelta(days=1)
        session.commit()

def rec_data():
    one1 = md.Record(id="061ab7ec-d647-4abd-a3a6-77d29d128796", datee="2024-12-10",id_number="1111",starting_time="10:00:00",title="Маникюр")    
    one2 = md.Record(id="ae59f637-e563-42aa-b873-e59e0e815703", datee="2024-12-10",id_number="1111",starting_time="11:00:00",title="Маникюр")
    one3 = md.Record(id="061ab7ec-d647-4abd-a3a6-77d29d128796", datee="2024-12-11",id_number="2222",starting_time="10:30:00",title="Педикюр")
    one4 = md.Record(id="cf021a74-4878-4e7f-a272-38f69606b454", datee="2024-12-10",id_number="2222",starting_time="11:00:00",title="Педикюр")
    one5 = md.Record(id="cfca23c9-fe24-4b9b-8246-901cd5cee2fa", datee="2024-12-10",id_number="3333",starting_time="10:00:00",title="Массаж лица")
    one6 = md.Record(id="cf021a74-4878-4e7f-a272-38f69606b454", datee="2024-12-10",id_number="3333",starting_time="11:00:00",title="Массаж лица")
    one7 = md.Record(id="f9051539-e718-48f4-b46d-71526dcccbb9", datee="2024-12-10",id_number="1111",starting_time="12:00:00",title="Маникюр")
    one8 = md.Record(id="f9051539-e718-48f4-b46d-71526dcccbb9", datee="2024-12-10",id_number="4444",starting_time="10:00:00",title="Полный массаж")
    one9 = md.Record(id="061ab7ec-d647-4abd-a3a6-77d29d128796", datee="2024-12-10",id_number="4444",starting_time="13:00:00",title="Полный массаж")

    md.SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(one1)
        session.add(one2)
        session.add(one3)
        session.add(one4)
        session.add(one5)
        session.add(one6)
        session.add(one7)
        session.add(one8)
        session.add(one9)

        session.commit()
        
spe_data() 
ins_data()
shc_data()
rec_data()

