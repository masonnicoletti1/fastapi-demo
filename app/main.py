#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Mason"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c:int, d:int):
    return {"multiply": c * d}

@app.get("/square/{e}")
def square(e:int):
    return {"square": e * e}

@app.get("/factorial/{f}")
def factorial(f:int):
  i = f - 1
  while i > 1:
    f = f * i
    i -= 1
  return {"factorial": f}


# dp1-diy-spotify
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "cxx6sw"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}

@app.get('/songs')
def get_songs():
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres ON songs.genre=genres.genreid ORDER BY songs.id;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}
