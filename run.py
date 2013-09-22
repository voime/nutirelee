#!/usr/bin/env python
from icalendar import Calendar, Event
from datetime import datetime, tzinfo
import pytz
from RPi import GPIO

# TODO: Move to configuration file

pins={"relee1":7,"relee2":11,"relee3":13,"relee4":15,"relee5":12,"relee6":16,"relee7":18,"relee8":22}

# set pinmode and pins
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) #use board pin numbers
for pin in pins.values():
  GPIO.setup(pin, GPIO.OUT)

# reading calendar file
cal = Calendar.from_ical(open('basic.ics','rb').read())

# parsing calendar and insert active evens to events list
events = []
for component in cal.walk():
  if isinstance(component, Event):
    #FIXME: Check that STATUS is CONFIRMED
    summary = component.decoded('SUMMARY')
    start = component.decoded('DTSTART')
    end = component.decoded('DTEND')
    now = datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)
    active = (now >= start and now < end)
    print "Event %s start at %s, end at %s and is currently %s" % (summary, start, end, "ACTIVE" if active else "DISABLED")
    if active:
    	events.append(summary)

# switch relay
for name in pins:
	if name in events:
		GPIO.output(pins[name], 1)
	else:
		GPIO.output(pins[name], 0)
        