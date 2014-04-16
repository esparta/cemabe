from collections import namedtuple
from sqlalchemy import create_engine, Table
from business import Base, Entidad
import csv

engine = create_engine("sqlite:///data.db", echo=False)
conn = engine.connect()

Base.metadata.create_all(engine)

tables = (("entidades","municipios",))
for table in tables:
    e = Table(table, Base.metadata, autoload=True, autoload_with=engine)
    columns = [c.name for c in e.columns]
    record = namedtuple(table, ",".join(columns[1:]))
    print("Processing {e}".format(e=table))
    with open('{e}.csv'.format(e=table)) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(4086))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        next(reader)
        for line in map(record._make, reader):
             ins = e.insert().values(**line.__dict__)         
             engine.execute(ins)
