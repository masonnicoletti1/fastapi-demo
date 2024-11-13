#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import mysql.connector
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
