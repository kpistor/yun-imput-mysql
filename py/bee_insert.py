from __future__ import print_function
from datetime import date, datetime, timedelta
from config import *
import mysql.connector
import sys


from bridgeclient import BridgeClient as bridgeclient

config = {
  'user': USER,
  'password': PASS,
  'host': HOST,
  'database': DBN,
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

time = datetime.now()
emp_no = cursor.lastrowid
value = bridgeclient()
temp = value.get("A0")
dig = value.get("D13")


add_sesnor = ("INSERT INTO sensor1 "
               "(time, degree_f, digital) "
               "VALUES (%s, %s, %s)")

data_sensor = (time, temp, dig)

#Insert data
cursor.execute(add_sesnor, data_sensor)

#Commit
cnx.commit()

cursor.close()
cnx.close()