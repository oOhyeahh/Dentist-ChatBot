import os
import sqlite3

# development env
# conn = psycopg2.connect("dbname=chatbot user=postgres password=Kanfer163")

# docker env
# conn = psycopg2.connect("dbname=chatbot user=testuser password=Kanfer163 host=db") 
# cur = conn.cursor()
try:
    path = os.path.dirname(os.path.realpath(__file__))+"/init.sql"
    query = open(path, "r").read()
    conn = sqlite3.connect('dentist.db')
    c = conn.cursor()
    c.executescript(query)
    conn.commit()
    c.close()
    conn.close()
except:
    print("created already")

# CREATE TABLE DENTIST (
#     DentistId varchar(256) primary key, 
#     FullName varchar(256),
#     workplace varchar(256),
#     specialist varchar(256)
# );

def get_all_available_dentists_fromdb():
    list = []
    conn = sqlite3.connect('dentist.db')
    cur = conn.cursor()
    cur.execute("SELECT DentistId, FullName FROM DENTIST")
    row = cur.fetchone()

    while row is not None:
        dentist_id, name = row
        dentist = {
            "dentistId": dentist_id,
            "name": name
        }
        list.append(dentist)
        row = cur.fetchone()
    
    conn.close()

    return list

def get_dentist_info_fromdb(id):
    list = []
    conn = sqlite3.connect('dentist.db')
    cur = conn.cursor()
    query = "SELECT DentistId, FullName, workplace, specialist FROM DENTIST WHERE DentistId={}".format(str(id))
    cur.execute(query)
    row = cur.fetchone()
    
    while row is not None:
        dentist_id, name, workplace, specialist = row
        dentist = {
            "dentistId": dentist_id,
            "name": name,
            "location": workplace,
            "specialist": specialist
        }
        list.append(dentist)
        row = cur.fetchone()
    
    conn.close()

    return list

def serach_dentist_by_name(name):
    list = []
    conn = sqlite3.connect('dentist.db')
    cur = conn.cursor()
    query = "SELECT DentistId, FullName FROM DENTIST Where FullName like '{}' or LOWER(FullName) = '{}'".format(
        '%'+str(name).capitalize()+'%', name)
    cur.execute(query)
    row = cur.fetchone()

    while row is not None:
        dentist_id, name = row
        dentist = {
            "dentistId": dentist_id,
            "name": name
        }
        list.append(dentist)
        row = cur.fetchone()

    conn.close()

    return list    