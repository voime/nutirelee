#!/bin/sh
cd /home/pi/relee/
rm -f basic.ics
wget https://www.google.com/calendar/ical/5d1ifn678ak5ln3s2po1ogaqng%40group.calendar.google.com/private-a9be2f5a03702415524ba2fd30ea5394/basic.ics
python run.py
