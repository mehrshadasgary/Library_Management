#                                  Library management Project(Back)

# Import
import sqlite3


# ==================================Database Function====================================

# Connect
def connect_db():
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("CREATE TABLE IF"
                   " NOT EXISTS library "
                   "(id INTEGER PRIMARY KEY,"
                   "titel text,"
                   "author text,"
                   "years INTEGER,"
                   "isbn INTEGER)")
    connect.commit()
    connect.close()


# View Database Function
def view_db():
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("SELECT * FROM library")
    all_view = cursor.fetchall()
    connect.close()
    return all_view


# Search Database Function
def search_db(titel='', author='', years='', isbn=''):
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("SELECT * FROM library WHERE "
                   "titel=? OR author=? OR years=? OR isbn=?",
                   (titel, author, years, isbn))
    all_search = cursor.fetchall()
    connect.close()
    return all_search


# Add Database Function
def add_db(titel, author, years, isbn):
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("INSERT INTO library VALUES"
                   " (NULL,?,?,?,?)",
                   (titel, author, years, isbn))

    connect.commit()
    connect.close()


# Edit Database Function
def edit_db(id, titel, author, years, isbn):
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("UPDATE library SET"
                   " titel=?,author=?,years=?, isbn=?"
                   " WHERE id=?",
                   (titel, author, years, isbn, id))

    connect.commit()
    connect.close()


# Delete Database Function
def delete_db(id):
    connect = sqlite3.connect('LibraryManagement.db')
    cursor = connect.cursor()
    # ejraye Query ha
    cursor.execute("DELETE FROM library"
                   " WHERE id=?", (id,))

    connect.commit()
    connect.close()


connect_db()
# add_db('Nineteen Eighty-Four', 'George Orwell', '1949', '#978-600-229-931-4')
# add_db('Da', 'Zahra Hosseini', '2008', '#978-964-506-488-2')
# add_db('Salam Bar Ebrahim', 'Groups', '2009', '#978-964-302-861-9')
# add_db('Animal Farm', 'George Orwell', '1945', '# 978-964-5620-54-5')
# add_db('The Forty Rules of Love', 'Elif Shafak', '2009', '#978-964-311-919-5')
# add_db('Daughter of Sheena', 'Behnaz Zarabi Zadeh', '2015', '#978-600-175-262-9')
# add_db('Gone with the Wind', 'Margaret Mitchell', '1936', '#978-964-8007-54-1')
# add_db('The Great Gatsby', 'F. Scott Fitzgerald', '1925', '#978-964-453-091-3')
# add_db('Man-e-oo', 'Reza Amirkhani', '2012', '#978-964-369-759-4')
# add_db('Ermia', 'Reza Amirkhani', '1996', '#978-964-369-766-2')

# add_db('iran', 'mohammad', 1398, 58977)
# delete_db()
# edit_db(4,'qaz','mehrshad',1401,88776655)
# print(view_db())
# print(search_db(author='ali'))
