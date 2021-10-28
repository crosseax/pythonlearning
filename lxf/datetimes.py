# datetime module

# do not name the file datetime.py

# DO NOT NAME THE .py FILE SAME AS YOUR MODULE

from datetime import datetime
    # module{}        # datetime

now = datetime.now()
print (now)

dt = datetime(2015, 4, 19, 12, 20)
print (dt)

# timestamp, its the 1970-01-01 stuff
# watch tom scott https://www.youtube.com/watch?v=-5wpm-gesOY

tsdt = dt.timestamp() # datetime to timestamp
print (tsdt)

rdt = datetime.fromtimestamp(tsdt) # timestamp to datetime, local
print (rdt)

utcdt = datetime.utcfromtimestamp(tsdt) # timestamp to datetime, utc
print (utcdt)

print ('strptime and strftime')
# strptime, string parser, which convert string to datetime
# https://strftime.org/

dt2 = datetime(2020,1,4,4,50)
print (dt2)
sdt2 = datetime.strptime(str(dt2), '%Y-%m-%d %H:%M:%S') # argument 1 must be str, 
                                                        # and the format after matches the str format
print (sdt2)

# strftime, string formatter, which format a datetime object to string format
# https://strftime.org/

now = datetime.now()

fnow = now.strftime('%a, %b %d %H:%M')
print (fnow)

fnow2 = now.strftime('%Y-%d-%m %H:%M:%S')
print (fnow2)

fnow3 = datetime.strftime(now, '%m-%d-%Y %I:%M:%S %p, US way')
print (fnow3)

sdt3 = datetime.strptime(str(fnow3), '%m-%d-%Y %I:%M:%S %p, US way')
print (sdt3)

# modern way of doing this
# from youtube
message = 'GVR was born on {:%A, %B %d, %Y}.'
gvr = datetime(1956,1,31)
gvrf = message.format(gvr)
print ('GVRF:', gvrf)





# datetime calculations
print ('datetime calculations')

from datetime import datetime, timedelta

tc1 = now + timedelta(hours=10)
tc2 = now - timedelta(days = 5)
tc3 = now + timedelta(days = 12, hours = 14)
tc4 = now - timedelta(30, 3600, 1500) # days, seconds, microseconds

print (tc1,
       tc2,
       tc3,
       tc4, sep = '\n')



# time zone info
print('timezone infos')

from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8)) # create timezone UCT+8
now = datetime.now()
print (now, 'now')

utcn = now.replace(tzinfo=tz_utc_8) # force time to be UTC+8
print (utcn, 'utc+8 now')


# get UTC then set time to be UTC+0
utcdt = datetime.utcnow().replace(tzinfo=timezone.utc) 
print (utcdt, 'utc time')

# use astimezone()to change timezone
bjdt = utcdt.astimezone(timezone(timedelta(hours = 8)))
print (bjdt, 'beijing time')

# same, to tokyo time
tkdt = utcdt.astimezone(timezone(timedelta(hours = 9)))
print (tkdt, 'tokyo time')

# you can also do bjt to tkt
tkdt2 = bjdt.astimezone(timezone(timedelta(hours = 9)))
print (tkdt2, 'tokyo time')
uswdt = bjdt.astimezone(timezone(timedelta(hours = -8)))
print (uswdt,'us west times')



# HW

import re

def to_timestamp (dt_str, tz_str):
    dt = datetime.strptime(str(dt_str), '%Y-%m-%d %H:%M:%S')
    # tz = datetime.strptime(str(tz_str), '%Z %-H')
    tz_utc=timezone(timedelta(hours=int(tz_str[3:-3])))
    dt = dt.replace(tzinfo = tz_utc)
    return dt.timestamp()
    
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print (t1,
       t2, sep='\n')

assert t1 == 1433121030.0, t1
assert t2 == 1433121030.0, t1
print ('Runs, good')