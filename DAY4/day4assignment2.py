import pkg as p
from datetime import datetime, date
file=p.File('.')
max_size=file.getMaxSizeFile(2)
print("print max size")
for i in max_size:
    print(i)
print("print latest date")
latest_files=file.getLatestFiles(datetime(2018,2,1).date())
for i in latest_files:
    print(f"name:{i[0]} date={i[1]}")
