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


year_2023 = datetime(2023, 1, 1)

print_date(year_2023)