#!/usr/bin/python3
"""
Connecting with MySQL server
and listing all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    usr = argv[1]
    pwd = argv[2]
    db_name = argv[3]
    par = argv[4]

    conc = '%'+par+'%'

    """Connecting with MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=usr,
                         passwd=pwd, db=db_name,
                         charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON " +
                "cities.state_id = states.id WHERE states.name LIKE %s",
                (conc,))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    db.close()
