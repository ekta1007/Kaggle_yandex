#executing & running the file for the session objects parsed
# rough notes will path things up after the project is complete

import gzip, yandex_parse
f = gzip.open('train.gz', 'rb') #assuming train.gz is located in same base location
sp = yandex_parse.parse_sessions(f)
sessions = [sp.next() for i in range(10)]

import csv
w = csv.writer(open("/yandex/output.csv", "w"))
for x in range(0,len(sessions)):
  for key, val in sessions[x].items():
    w.writerow([key, val])
  
# reading part of the gzip file 
import gzip
f = gzip.GzipFile(fileobj=open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/train.gz', 'rb'))
data = f.read(4000)
print data
print "done"
