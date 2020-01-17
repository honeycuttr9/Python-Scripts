#!/usr/bin/env python

from datetime import datetime, time
from time import sleep

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

gradDate = datetime.strptime('2020-05-09 08:00:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print("Countdown to Graduation May 2020")
print("--------------------------------")
while gradDate>now:
    print("%d Days %d Hours %d Minutes %d Seconds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, gradDate)))
    sleep(1)
    now = datetime.now()

print("Done")







