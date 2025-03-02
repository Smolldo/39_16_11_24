# len()
a = [1,2,3,4,5,6,7,8,9]
b = 'dfgbhghdsufaighdsuifg'

print(len(b))


# min()  max()
print(max(a))
print(min(a))

print(max(b))
print(min(b))


# abs() 

c = -20
print(abs(c))


# sum()

print(sum(a))


from datetime import date, time, datetime, timedelta

today = date.today()

print(today)

print(today.year)
print(today.month)

lunch_time = time(12, 30, 45, 2)
print(lunch_time)


now = datetime.now()
print(now)
print(now.time())
print(now.date())


duration = timedelta(days=2, hours=3)
print(duration)

future_date = now + duration
print(future_date)

weeks = timedelta(weeks= 13)

endOfschool = now + weeks
print(endOfschool)

delta = datetime(2025, 2, 23) - datetime(1999, 2, 22)

print(delta.days)

d = date(2025, 2, 23)
formated_date = d.strftime('%d %B, %Y')
print(formated_date)

t = time(12, 30)

form_time = t.strftime('%H hours %M minutes')
print(form_time)
dt = datetime(2025, 2, 23, 10, 10, 30)
form = dt.strftime('%d, %B, %Y.  %H:%M')
print(form)


import time

# start_time = time.perf_counter()

# for i in range(100000000):
#     pass

# end_time = time.perf_counter()

# total_time = end_time - start_time
# print(total_time)


utc_time = time.gmtime()
print(time.strftime('%Y, %B, %d. %H:%M', utc_time))


local_time = time.localtime()
print(time.strftime('%Y, %B, %d. %H:%M', local_time))



import math

# sqrt()

print(math.sqrt(225))
print(math.sqrt(476))

#log()
natur_log = math.log(2.7183)
print(natur_log)


# ceil()  floor()

print(math.ceil(2.1))
print(math.floor(2.99))

import os

curr_dir = os.getcwd()
print(curr_dir)

# os.chdir('/dfasd/asdasd/asdasd')

print(os.listdir('.'))


import sys

print(sys.argv)

print(sys.version)

# sys.exit(1)

import random

m = random.randint(-10, 10)
print(m)

a = {
    'name': 'John'
}

