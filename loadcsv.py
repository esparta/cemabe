from sqlalchemy import create_engine, Table
from business import Base
import csv

engine = create_engine("sqlite:///data.db", echo=False)
conn = engine.connect()

Base.metadata.create_all(engine)

def genvalues(columns, iterator, limit=50000):
    """ Given an iterator, return a list of dictionaries
        mixing the columns with the iterator values """
    results = []
    for num_rows, row in enumerate(iterator, start=1):
        results.append(dict(zip(columns, row)))
        if num_rows % limit == 0:
            yield results
            results = []
    yield results

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
            for values in genvalues(columns, reader):
                engine.execute(entity.insert(), values)

if __name__ == "__main__":
    main()

