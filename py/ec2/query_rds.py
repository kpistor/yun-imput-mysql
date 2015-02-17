from config import *
from emailer import send_email
import mysql.connector
import sys
import time

config = {
  'user': USER,
  'password': PASS,
  'host': HOST,
  'database': DBN,
  'raise_on_warnings': True,
}

while True:

	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	query = ('SELECT AVG(degree_f) FROM arduino1.sensor1 WHERE time > NOW() - INTERVAL 1 HOUR ')

	cursor.execute(query)

	for (degree_f) in cursor:
		hour_avg = degree_f[0]
		print(hour_avg)
		s_hour_avg = str(hour_avg)
		send_email(s_hour_avg )

	cursor.close()
	cnx.close()

	time.sleep(5)	

