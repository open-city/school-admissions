import csv

address_parts = ('Street Number', 'Street Direction', 
                 'Street Name', 'City', 'State', 'ZIP')

schools = {}

with open('../raw_data/CPS_Schools_2013-2014_Academic_Year_HS.csv') as infile :
    reader = csv.DictReader(infile) 
    for row in reader :
        schools[row['SchoolID']] = ' '.join([row[part] for part 
                                             in address_parts])

print schools
