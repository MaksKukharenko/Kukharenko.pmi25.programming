from datetime import date
from datetime import time
from Class_file import JOURNEY
from Funky_file import read_journey_from_file

with open("Database.txt") as f:
    lines = int(len(f.read().splitlines())/9)

journey = JOURNEY(0,0,0,0,0)
mylist = []

for i in range(lines):
    read_journey_from_file("Database.txt", journey, i, mylist)
    print(mylist[i],"\n")

journey = JOURNEY("Chernigiv", 70, date(2024,5,2), date(2024,6,4), "Oleg")
f = open("Database.txt", "a")
f.write('\n')
f.write(journey["city"])
f.write('\n')
f.write(str(journey["budget"]))
f.write('\n')
f.write(str(journey["start_date"].year))
f.write('\n')
f.write(str(journey["start_date"].month))
f.write('\n')
f.write(str(journey["start_date"].day))
f.write('\n')
f.write(str(journey["end_date"].year))
f.write('\n')
f.write(str(journey["end_date"].month))
f.write('\n')
f.write(str(journey["end_date"].day))
f.write('\n')
f.write(journey["username"])
f.close()