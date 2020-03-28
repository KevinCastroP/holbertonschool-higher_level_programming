#!/usr/bin/python3
"""
Connecting with MySQL server
and listing all states from the
database hbtn_0e_0_usa
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    """Connecting with MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
