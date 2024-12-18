from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date, time
import queries as qr
import uuid

class ClientForm(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    phone_numb: str
    date_of_birth: date

class ClientFormDelete(BaseModel):
    id: Optional[uuid.UUID]

class GetRecEmp(BaseModel):
    id_number: str
    
class GetRecCli(BaseModel):
    id: Optional[uuid.UUID]

class DelRecord(BaseModel):
    id: Optional[uuid.UUID]
    datee: date
    starting_time: time

class MakeRecord(BaseModel):
    id: Optional[uuid.UUID]
    datee: date
    id_number: str
    starting_time: time

class FreeRecord(BaseModel):
    datee: date
    title: str
    
app = FastAPI()

@app.post("/addClients")
async def addClients(data: ClientForm):
    print(data)
    return qr.addClients(last_name=data.last_name, first_name=data.first_name,
                    middle_name=data.middle_name, phone_numb=data.phone_numb,
                    date_of_birth=data.date_of_birth)

@app.post("/deleteClients")
async def deleteClients(data: ClientFormDelete):
    print(data)
    return qr.deleteClients(id=data.id)

@app.post("/get_record_emp")
async def get_record_emp(data: GetRecEmp):
    return qr.get_record_emp(id_number=data.id_number)

@app.post("/get_record_cli")
async def get_record_cli(data: GetRecCli):
    return qr.get_record_cli(id=data.id)

@app.post("/delete_record")
async def delete_record(data: DelRecord):
    return qr.delete_record(id=data.id, datee=data.datee,
                            startimg_time=data.startimg_time)

@app.post("/make_record")
async def make_record(data: MakeRecord):
    return qr.make_record(id=data.id, datee=data.datee,
                          id_number=data.id_number,
                          startimg_time=data.startimg_time)

@app.post("/free_record")
async def free_record(data: FreeRecord):
    return qr.free_record(datee=data.datee,title=data.title)
