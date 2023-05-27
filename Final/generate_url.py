import uuid
import pyshorteners
from databse import *
from datetime import datetime, timedelta

db = database()

def generate_url():
    task_id = str(uuid.uuid4())
    endpoint = f'/generate/{task_id}'
    return endpoint

def shorten_url(url):
    url = url
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

def whitelist(ip,usn,dob):
    data = db.find({"usn":usn})
    if data == None:
        tim = datetime.today()
        data = {"usn":usn, "dob":dob, "count":1, "ip":[[ip ,tim, tim + timedelta(days=356)]]}
        db.insert(data)
    elif ip not in data["ip"] and data["count"] < 3:
        data["ip"].append({ip: datetime.today()})
        data["count"] += 1
        db.update({"usn":usn}, data)
    elif ip in data["ip"]:
        return "already allowed"
    else:
        return "not allowed"

def get_count(usn):
    data = db.find({"usn":usn})
    return data["count"]