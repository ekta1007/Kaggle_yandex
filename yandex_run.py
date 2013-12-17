#executing & running the file for the session objects parsed

import gzip, yandex_parse
f = gzip.open('train.gz', 'rb') #assuming train.gz is located in data/
sp = yandex_parse.parse_sessions(f)
sessions = [sp.next() for i in range(10)]

import csv
w = csv.writer(open("/yandex/output.csv", "w"))
for x in range(0,len(sessions)):
  for key, val in sessions[x].items():
    w.writerow([key, val])
