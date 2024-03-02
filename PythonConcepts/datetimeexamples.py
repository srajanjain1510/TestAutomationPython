from datetime import datetime, date

import pytz

now = datetime.now()
print(now)

current_date = date.today()
print(current_date)

date_obj = date(2024, 4, 2)
print(date_obj)

# strftime usage
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(now)

# strptime usage
date_string = "25 December, 1988"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# handling timezones

local_date_time = datetime.today()
print("Local Date Time:",local_date_time)

#convert it to UTC time zone
tz_utc = pytz.timezone('UTC')
date_time_utc = datetime.now(tz_utc)
print("UTC time zone date time=",date_time_utc)
