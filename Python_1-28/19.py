from datetime import date,timedelta
start = date(1901,1,1)
end = date(2000,12,31)
a = timedelta(days = 1)
x = 0
while start<=end:
    if start.isoweekday() == 7 and start.day == 1:
        x+=1
    start = start+a
print(x)
