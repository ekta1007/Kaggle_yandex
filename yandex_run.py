# rough notes will path things up after the project is complete


#executing & running the file for the session objects parsed
import gzip, yandex_parse
f = gzip.open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/train.gz', 'rb') 
sp = yandex_parse.parse_sessions(f)
sessions = [sp.next() for i in range(10)]

#note that "sessions" is list - so I am reading the "items" stored in each session
import csv
w = csv.writer(open("C:/Users/Ekta.Grover/Desktop/Downloads/yandex/output1.csv", "w"))
for x in range(0,len(sessions)):
  for key, val in sessions[x].items():
    w.writerow([key, val])
print "success"

  
# reading part of the gzip file 
import gzip
f = gzip.GzipFile(fileobj=open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/train.gz', 'rb'))
#number of lines in a file len(f.readlines())
data = f.read(4000)
print data
print "done"

# process N lines at a time using islice 
#fetching & printing 1st N lines from a gz file 
import gzip
from itertools import islice
N = 20
infile = gzip.GzipFile(fileobj=open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/train.gz', 'rb'))
next_n_lines = islice(infile, N)
i=1
for lines in next_n_lines:
     print lines



#or printing the entire file iteratively - note this will print all, and we have explictly put a wait for see the next "N" records
import gzip,time
N=20
infile = gzip.GzipFile(fileobj=open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/train.gz', 'rb'))
with infile as f:
    while True:
        next_n_lines = islice(f, N)
        for lines in next_n_lines:
            print lines
        time.sleep(5) 
        if not next_n_lines:
            break
  
# Searching for userid's within the data - we observe that userids just occur within rows with session metadata , ie. with "M"
# The assumption will be - we will either work on a sampled file, or just use this to validate a hypothesis
import gzip 
from itertools import islice
N = 200
userid=[]
searchphrase ='M'
infile = gzip.GzipFile(fileobj=open('C:/Users/Ekta.Grover/Desktop/Downloads/yandex/test.gz', 'rb'))
with infile as f:
    while True:
        next_n_lines = islice(f, N)
        for lines in next_n_lines:
            if searchphrase in lines:
                userid.append(lines.split()[-1])
        if not next_n_lines:
            break
print "Total userid records (with session metadata) in train file %d " %len(userid)
print "Total unique userids records in train file %d" %len(set(userid))  # doing a set to just get the unique set of users in the userid list



          
