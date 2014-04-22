from sqlalchemy import create_engine, Table
from sqlalchemy.orm import scoped_session, sessionmaker
from business import Base, Entidad
import csv

engine = create_engine("sqlite:///data.db", echo=False)
conn = engine.connect()

DBSession = scoped_session(sessionmaker())
DBSession.remove()
DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
Base.metadata.create_all(engine)

def genvalues(columns, values):
    for row in values:
        yield dict(zip(columns, row))

def main():
    tables = (("entidades","municipios",))

    for table in tables:
        entity = Table(table, Base.metadata, autoload=True,
                       autoload_with=engine)
        columns = ([c.name for c in entity.columns])[1:]
        print("Processing {e}".format(e=table))
        with open('{e}.csv'.format(e=table)) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(8096))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            next(reader)
            values = genvalues(columns, reader)
            engine.execute(entity.insert(), list(values))

if __name__ == "__main__":
    main()

