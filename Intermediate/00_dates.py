### Dates ###

import datetime as dt
from datetime import datetime
now  = datetime.now()

# print(now)
# print(now.year)
# print(now.hour)
# print(now.day)
# print(now.month)
# print(now.minute)
# print(now.second)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.month)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)  
timestamp = now.timestamp()


year_2023 = datetime(2023, 11, 1)

print_date(year_2023)

from datetime import time

current_time = time(21, 6, 55)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(1995, 2, 28)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month, current_date.day)

print(current_date.year)


from datetime import timedelta

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)



start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)