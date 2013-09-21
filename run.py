#!/usr/bin/env python
from icalendar import Calendar, Event
from datetime import datetime, tzinfo
import pytz

from RPi import GPIO
import time

# TODO: Move to configuration file
pin_relee=18
pin_pump=16
pin_lamp=7

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
for pin in [pin_relee, pin_pump, pin_lamp]:
  GPIO.setup(pin, GPIO.OUT)

cal = Calendar.from_ical(open('basic.ics','rb').read())

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
    if summary == "relee":
      GPIO.output(pin_relee, 1 if active else 0)
    if summary == "pump":
      GPIO.output(pin_pump, 1 if active else 0)
    if summary == "lamp":
      GPIO.output(pin_lamp, 1 if active else 0)
