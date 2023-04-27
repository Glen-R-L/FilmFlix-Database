from connect import *

def read_report():

  reports_on = True

  while reports_on:

    report_options = input("\nfilmflix Database / tblFilms Table / Reports\n\nTo view a report from this database - Enter an option by number:\n\n1. View all records in a selected column\n2. View all films within a selected genre\n3. View all films released in a selected year\n4. View all films with a selected rating\n5. Exit\n\n")

    ops_flag = True

    while ops_flag:

      match report_options:

        case '1':

          column_view = input("\nSelect a table column to view for all records - Enter an option by letter:\n\nT. title\nY. yearReleased\nR. rating\nD. duration\nG. genre\n\n")

          column_view = column_view.upper()

          match column_view:
            case 'T':
              cursor.execute("Select title From tblFilms")
              column = cursor.fetchall()
              
              for field in column:
                print(field)
            case 'Y':
              cursor.execute("Select yearReleased From tblFilms")
              column = cursor.fetchall()
              
              for field in column:
                print(field)
            case 'R':
              cursor.execute("Select rating From tblFilms")
              column = cursor.fetchall()
              
              for field in column:
                print(field)
            case 'D':
              cursor.execute("Select duration From tblFilms")
              column = cursor.fetchall()
              
              for field in column:
                print(field)
            case 'G':
              cursor.execute("Select genre From tblFilms")
              column = cursor.fetchall()
              
              for field in column:
                print(field)

          ops_flag = False

        case '2':

          genre_view = input("\nTo view all films within a selected genre - Enter an option by letter code:\n\nac. Action\nan. Animation\nco. Comedy\ncr. Crime\nfa. Fantasy\nfi. Fighting\nsf. Scifi\nt. Test\n\n")

          genre_view = genre_view.upper()

          match genre_view:
            case 'AC':
              cursor.execute("Select * From tblFilms Where genre = \'Action\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'AN':
              cursor.execute("Select * From tblFilms Where genre = \'Animation\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'CO':
              cursor.execute("Select * From tblFilms Where genre = \'Comedy\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'CR':
              cursor.execute("Select * From tblFilms Where genre = \'Crime\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'FA':
              cursor.execute("Select * From tblFilms Where genre = \'Fantasy\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'FI':
              cursor.execute("Select * From tblFilms Where genre = \'Fighting\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'SF':
              cursor.execute("Select * From tblFilms Where genre = \'Scifi\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'T':
              cursor.execute("Select * From tblFilms Where genre = \'Test\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)

          ops_flag = False

        case '3':

          year_choice = input("\n To view all films released in a selected year - Enter a year.")
          year_choice = "'" + year_choice + "'"
          cursor.execute(f"Select * From tblFilms Where yearReleased = {year_choice}")
          row = cursor.fetchall()

          for record in row:
                print(record)

          ops_flag = False

        case '4':

          rating_view = input("\nTo view all films with a selected rating - Enter an option by letter code:\n\ng. General Audience\npg. Parental Guidance\nr. Restricted\n\n")

          rating_view = rating_view.upper()

          match rating_view:
            case 'G':
              cursor.execute("Select * From tblFilms Where rating = \'G\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'PG':
              cursor.execute("Select * From tblFilms Where rating = \'PG\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            case 'R':
              cursor.execute("Select * From tblFilms Where rating = \'R\'")
              row = cursor.fetchall()
              
              for record in row:
                print(record)
            

          ops_flag = False

        case '5':

          print("You have now Exited Reports.")
          
          ops_flag = False
          reports_on = False

        case _:

          print(f"{report_options} is not a valid value.")
          report_options = input("\nfilmflix Database / tblFilms Table / Reports\n\nEnter an option by number:\n\n1. View all records in a selected column\n2. View all films within a selected genre\n3. View all films released in a selected year\n4. View all films with a selected rating\n5. Return to Main Menu\n\n")


if __name__ == '__main__':
  read_report()

