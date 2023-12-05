import mariadb
import dbcreds

def connect_db():
 try:
   conn = mariadb.connect(
    user=dbcreds.user, 
    password=dbcreds.password,
    host=dbcreds.host, 
    port=dbcreds.port, 
    database=dbcreds.database
   )
   cursor = conn.cursor()
   return cursor
 except mariadb.OperationalError as error:
   print("OPERATIONAL ERROR:", error)
 except Exception as error:
   print("UNEXPECTED ERROR:", error)
   
def execute_statement(cursor, statement):
  try:
    cursor.execute(statement)
    results = cursor.fetchall()
    return results
  except mariadb.ProgrammingError as error:
    print("PROGRAMMING ERROR:", error)
  except mariadb.IntegrityError as error:
    print("INTEGRITY ERROR:", error)
  except mariadb.DataError as error:
    print("DATA ERROR:", error)
  except Exception as error:
    print("UNEXPECTED ERROR:", error)
    
def close_connection(cursor):
  try:
    conn = cursor.connection
    cursor.close()
    conn.close()
    print("Disconnected from database")
  except mariadb.OperationalError as error:
    print("OPERATIONAL ERROR:", error)
  except mariadb.InternalError as error:
    print("INTERNAL ERROR:", error)
  except Exception as error:
    print("UNEXPECTED ERROR:", error)