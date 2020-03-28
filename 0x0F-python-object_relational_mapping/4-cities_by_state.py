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


    """Connecting with MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=usr,
                         passwd=pwd, db=db_name,
                         charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name " +
                "FROM cities AS c, states AS s " +
                "WHERE c.state_id=s.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
