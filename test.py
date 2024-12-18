import queries as q
from datetime import date, time
from sqlmodel import Session
from sqlalchemy import  create_engine

#engine = create_engine("postgresql://postgres:1340@localhost:5432/spa")

# добавление нового клиента
'''
q.addClients(last_name="Ким",
             first_name="Карина",
             middle_name="Игоревна",
             phone_numb="89113338811",
             date_of_birth=date(1980, 1, 1))
'''
# удаление клиента
#q.deleteClients(id="11c8800b-dc13-45af-9a03-9855191b9dfd")


# показать записи специалиста   
#q.get_record_emp(id_number="1111")

# показать записи клиента   
#q.get_record_cli(id="061ab7ec-d647-4abd-a3a6-77d29d128796")

# удалить запись клиента
'''
q.delete_record(id="061ab7ec-d647-4abd-a3a6-77d29d128796",
                datee=date(2024, 12, 11),
                starting_time=time(10, 30))
'''
# записать клиента на процедуру
'''
q.make_record(id="061ab7ec-d647-4abd-a3a6-77d29d128796",
              datee=date(2024, 12, 11),
              id_number="2222",
              starting_time=time(10, 30))
'''
# свободное время для записи на процедуру в определенную дату
q.free_record(datee=date(2024, 12, 10), title="Маникюр")


