from dbhelpers import connect_db, execute_statement, close_connection, run_statement

# def getAllBooks():
#  cursor = connect_db()
#  if(cursor == None):
#   return
 
#  results = execute_statement(cursor, 'CALL get_books()')
#  if(results != None):
#   print(results)
 
#  close_connection(cursor)
#  print("------")
 

# def getBooksByAuthor():
#  authorName = input("Write the name of an author? ")
#  cursor = connect_db()
 # statement = f"CALL get_author_books('{authorName}')"
#  results = execute_statement(cursor, statement)
#  close_connection(cursor)

result = run_statement('CALL get_books()')
print(result)
# Handle the connection error


authorName = input("Write the name of an author? ")
result = run_statement("CALL get_author_books(?)", authorName)
print(result)
