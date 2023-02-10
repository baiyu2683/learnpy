#!/usr/bin/env python3
from datetime import date

now = date.today()
print(now, type(now))

x = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B")
print(x)

birthday = date(1964, 7, 31)
age = now - birthday
print(age)
print(age.days)
