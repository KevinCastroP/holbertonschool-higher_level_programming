#!/usr/bin/python3
"""
Listing all objects from State table
"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    louis = State(name='Louisiana')
    session.add(louis)
    session.commit()
    print(louis.id)
    session.close()
