from dbhelpers import connect_db, execute_statement, close_connection

cursor = connect_db()
results = execute_statement(cursor, 'CALL get_books()')
print(results)
close_connection(cursor)

print("------")


authorName = input("Write the name of an author? ")
cursor = connect_db()
statement = f"CALL get_author_books('{authorName}')"
results = execute_statement(cursor, statement)
print(results)
close_connection(cursor)