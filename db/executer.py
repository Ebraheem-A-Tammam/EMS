import sqlite3

def execute_query(query : str) -> list:

    """
        a function that takes a sql query, excutes it against
        the database and returns the output as a list of tuples
        each tuple represents the corresponding row of the output  
    """

    connection = sqlite3.connect('system.db')
    crsr = connection.cursor()
    
    crsr.execute(query)
    output = crsr.fetchall()

    connection.close()

    return output

def execute_command(cmd : str) -> list:

    connection = sqlite3.connect('system.db')
    crsr = connection.cursor()

    crsr.execute(cmd)
    connection.commit()

    connection.close()