

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

def get_student_data(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Students WHERE Student_Id = ?"
    cursor.execute(query,(student_id,))
    records = cursor.fetchall()
    for row in records:
      print ("ID студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", get_school_name(row[2]))
      
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)


get_student_data(203)
