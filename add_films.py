from connect import *
from read_films import *
import time

def film_insert():

  films = []

  film_title = input("Enter a movie title.")
  film_year = int(input("Enter the year the movie was released."))
  film_rating = input("Enter the movie rating by letter:\n\nG (General Audience)\nPG (Parental Guidance)\nR (Restricted)\n\n")
  film_duration = int(input("Enter the movie duration in minutes."))
  film_genre = input("Enter the genre of the movie. Select from:\n\nAction\nAnimation\nComedy\nCrime\nFantasy\nFighting\nScifi\nTest\n\n")

  film_title = film_title.title()
  film_rating = film_rating.upper()
  film_genre = film_genre.title()

  films.append(film_title)
  films.append(film_year)
  films.append(film_rating)
  films.append(film_duration)
  films.append(film_genre)


  cursor.execute("Insert Into tblFilms(title, yearReleased, rating, duration, genre) Values (?,?,?,?,?)", films)

  conn.commit()
  print(f"{film_title} has been added to the table.")
  time.sleep(3)

  read()

if __name__ == '__main__':
  film_insert()
  


