import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

url = "http://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json"
request = requests.request("GET", url)
result_var = request.json()
var_interation = result_var["gold"]
with open ("file1.json", "w") as f:
    lst = []
    for i in var_interation:
        name = i.get("name")
        price = i.get("price")
        var_interation = {"name": name, "price":price}
        lst.append(var_interation)
         
    json.dump(lst, f)

class Data1(BaseModel):
    name: str
    price: int

class Data2(BaseModel):
    name: str
    price: int

app = FastAPI()

with open("file1.json", "r", encoding="utf_8") as f:
    database = json.load(f)

@app.get("/")
def getdata():
    return database

@app.post("/post/")
def postdata(data1: Data1):
    database.append(data1)
    return database

@app.put("/put/{put_name}")
def putdata(put_name: str, data2: Data2):
    for i, value in enumerate(database):
        if value["name"] == put_name:
            database[i] = data2.dict()
            return database
    raise HTTPException(status_code=404, detail="puterror")

@app.patch("/patch/{patch_name}")
def patchdata(patch_name: str, data1: Data1):
    for i, value in enumerate(database):
        if value["name"] == patch_name:
            database[i] = data1.name
            return database
    raise HTTPException(status_code=404, detail="patcherror")

@app.delete("/delete/{delete_name}")
def deletedata(delete_name: str):
    for i, value in enumerate(database):
        if value["name"] == delete_name:
            del database[i]
            return database
    raise HTTPException(status_code=404, detail="patcherror")
    