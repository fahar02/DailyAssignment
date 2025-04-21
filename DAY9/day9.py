from fastapi import FastAPI , Request
from pydantic import BaseModel
from sqlalchemy import create_engine, text 
from functools import wraps
import os
app = FastAPI()
SCHEMA = ["name", "age"]
#create the sqlite engine
eng = create_engine("sqlite:///people.db")
drop_t = "drop table if exists people"
#create table query
sql_create_table='''
create table if not exists people(
name string,
age int)
'''
#uncomment this code for first time so that tabel must be created in the current directory
#then commit it
"""
with eng.connect() as con:
    con.execute(text(drop_t))
    con.execute(text(sql_create_table))
    con.commit()
"""
def get_all():
    with eng.connect() as conn:
        res = conn.execute(text("select name, age from people")).fetchall()
    return [dict(zip(SCHEMA,row)) for row in res]
    
def get_one(name):
    with eng.connect() as conn:
        res = conn.execute(text("select age from people where name=:name"),
            dict(name=name)).fetchone()
    return res
  
def delete_one(name):
    with eng.connect() as conn:
        conn.execute(text("delete from people where name=:name"),
                dict(name=name))
        conn.commit()
                
def update_one(name, age):
    with eng.connect() as conn:
        conn.execute(text("Update people SET age=:age where name=:name"),
                dict(name=name, age=age))
        conn.commit()

def insert_one(name, age):
    if get_one(name):
        return 
    with eng.connect() as conn:
        conn.execute(text("insert into people values(:name, :age)"),
                dict(name=name, age=age))
        conn.commit()


@app.get("/helloj/all")
async def read():
    result=get_all()
    return result

class People(BaseModel):
    name:str
    age:int

@app.put("/helloj/update")
async def update(people:People):
    get=get_one(people.name)
    if get is not None:
        update=update_one(people.name,people.age)
        return {"name":people.name,"age":people.age}
    else:
        return {"error":"no update"}

@app.delete("/helloj/delete/{name}")
async def delete(name:str):
    get=get_one(name)
    if get is not None:
        delete=delete_one(name)
        return {"name":name}
    else:
        return {"error":"no delete"}
        
class People(BaseModel):
        name:str
        age:int
        
@app.post('/helloj/create')
async def create(people:People):
    insert_one(people.name,people.age)
    return {"name":people.name,"age":people.age}
    
    