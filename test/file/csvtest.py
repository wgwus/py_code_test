import csv


with open ('csvtest.csv','r') as f:
    data = csv.reader(f)
    for i in data:
        print (i)
    
    
with open ('csvtest.csv','w') as f:
    csv.writer(f).writerow(data)
    