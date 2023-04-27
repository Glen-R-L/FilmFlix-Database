from connect import *
from read_films import *
import time

def film_update():

  id_field = int(input("Enter the ID of the movie to be updated."))
  field_name = input("Enter the field you want to update, as shown in the list. Choose from:\n\ntitle\nyearReleased\nrating\nduration\ngenre\n\n")
  field_value = input(f"Enter the value for the {field_name} field.\n\nNotes:\nFor rating, select from G, PG, R\nFor genre, select from Action, Animation, Comedy, Crime, Fantasy, Fighting, Scifi, Test\n\n")

  match field_name:

    case 'title':
      field_value = field_value.title()
    
    case 'rating':
      field_value = field_value.upper()

    case 'genre':
      field_value = field_value.title()
      

  field_value = "'" + field_value + "'"

  cursor.execute(f"Update tblFilms Set {field_name} = {field_value} Where filmID = {id_field}")
  conn.commit()

  print(f"Record {id_field} updated in the tblFilms table.")
  time.sleep(3)

  read()


if __name__ == '__main__':
  film_update()