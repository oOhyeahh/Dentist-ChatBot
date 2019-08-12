import sqlite3, datetime, os
from datetime import time
from .utils import *

# development env
# conn = psycopg2.connect("dbname=chatbot user=postgres password=Kanfer163")

# docker env
# conn = psycopg2.connect("dbname=chatbot user=testuser password=Kanfer163 host=db") 
# cur = conn.cursor()


# CREATE TABLE TIMESLOT (
#     BookingId SERIAL primary key,
#     DentistId integer,
#     PatientName varchar(256),
#     PhoneNumber varchar(256),
#     BookingDate varchar(256),
#     StartTime varchar(256),
# 	EndTime varchar(256)
# );
try:
    path = os.path.dirname(os.path.realpath(__file__))+"/init.sql"
    query = open(path, "r").read()
    conn = sqlite3.connect('timeslot.db')
    c = conn.cursor()
    c.executescript(query)
    conn.commit()
    c.close()
    conn.close()
except:
    print("Data has been inserted")

def cancel_booking(booking_id):
    try:
        conn = sqlite3.connect('timeslot.db')
        cur = conn.cursor()    
    except:
        return False

    query = "DELETE FROM timeslot WHERE bookingid = {}".format(booking_id)
    cur.execute(query)
    conn.commit()    
    conn.close()
    return True

def create_booking(dentist_id, patient_name, phonenumber, booking_date, starttime, endtime):
    try:
        conn = sqlite3.connect('timeslot.db')
        cur = conn.cursor()    
    except:
        return False
    query = "INSERT INTO TIMESLOT(DentistId, PatientName, PhoneNumber, BookingDate, startTime, endtime) VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(\
        dentist_id, patient_name, phonenumber, booking_date, starttime, endtime);
    cur.execute(query)
    conn.commit()
    cur.execute("SELECT bookingid FROM TIMESLOT ORDER BY bookingid DESC")
    row = cur.fetchone()
    conn.close()
    return row[0]
    

def serach_booking_by_dentist(dentist_id):
    list = []
    try:
        conn = sqlite3.connect('timeslot.db')
        cur = conn.cursor()    
    except:
        return list    
    query = "SELECT bookingdate, startTime, endtime FROM TIMESLOT Where dentistid = {}".format(dentist_id)
    cur.execute(query)
    row = cur.fetchone()

    while row is not None:
        bookingdate, startTime, endtime = row
        appointment = (combine_formatted_date_time(startTime, bookingdate), combine_formatted_date_time(endtime, bookingdate))
        list.append(appointment)
        row = cur.fetchone()

    return list  

def find_booking_by_id(id):
    booking = 0
    try:
        conn = sqlite3.connect('timeslot.db')
        cur = conn.cursor()    
    except:
        return booking    
    query = "SELECT COUNT(bookingid) AS Num FROM TIMESLOT WHERE bookingid = {}".format(id)
    cur.execute(query)
    row = cur.fetchone()
    booking = row[0]
    return booking        
              