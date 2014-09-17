import csv
from os.path import join, abspath
import os
from api.database import engine
from api.models import SourceDest

data_dir = abspath(join('data', 'raw_data', 'transitskims100'))

if __name__ == "__main__":
    fpath = join(data_dir, 'mf22.txt')
    table = SourceDest.__table__
    conn = engine.connect()
    fields = ['source', 'dest', 'travel_time']
    with open(fpath, 'rU') as f:
        [f.next() for i in range(4)]
        for line in f:
            parts = line.strip().split(' ')
            source = parts[0]
            destinations = [i.split(':') for i in parts[1:]]
            vals = []
            for dest in destinations:
                vals.append({k:v for k,v in zip(fields,(source, dest[0], dest[1],))})
            ins = table.insert()
            conn.execute(ins, vals)
