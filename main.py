from datetime import date
from datetime import datetime

a = datetime(2020, 11, 4, 14, 53)
print(a.strftime("%Y/%m/%d %H:%M:%S"))

b = datetime(2020, 11, 4, 14, 53)
print(b.strftime("%y/%B/%d %H:%M:%S %p"))

c = datetime(2020, 11, 4, 14, 53)
print(c.strftime("%a, %Y %b %d"))

d = datetime(2020, 11, 4, 14, 53)
print(d.strftime("%A, %Y %B %d"))

e = datetime(2020, 11, 4, 14, 53)
print(e.strftime("Weekday: %w"))

f = datetime(2020, 11, 4, 14, 53)
print(f.strftime("Day of the year: %j"))

g = datetime(2020, 11, 4, 14, 53)
print(g.strftime("Week number of the year: %U"))
