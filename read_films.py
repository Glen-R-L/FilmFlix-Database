from connect import *

def read():
  cursor.execute("Select * From tblFilms")

  rows = cursor.fetchall()

  for record in rows:
    print(record)

if __name__ == '__main__':
  read()

  
