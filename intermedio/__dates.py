## Dates ##
from datetime import datetime
from datetime import time

now = datetime.now()

timestmap = now.timestamp()

print(timestmap)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2024 = datetime(2024,1,1)
print_date(year_2024)


current_time = time(21,6,0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

diff = year_2024 - now

print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 4)
end_timedelta = timedelta(300, 100, 100, weeks = 5)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)