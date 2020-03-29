#!/usr/bin/python3
"""
Listing all objects from State table
"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(City, State).filter(City.state_id == State.id)\
                                          .order_by(City.id.asc())
    for c, s in new_state:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
