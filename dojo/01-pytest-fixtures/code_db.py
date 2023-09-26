import sqlite3


def write_to_db():
    # Connect to a SQLite database (create one if it doesn't exist)

    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                      (column1 TEXT, column2 TEXT)''')

    # Insert rows into the table
    cursor.execute("INSERT INTO mytable VALUES (?, ?)", ("Value 1", "Value 2"))
    cursor.execute("INSERT INTO mytable VALUES (?, ?)", ("Value 3", "Value 4"))

    # Commit the changes
    conn.commit()

    return True

