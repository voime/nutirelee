nutirelee
=========

Releede juhtimine Google kalendriga

# Kirjeldus
Releedega on võimalik juhtida erinevaid elektrilisi seademid. Releesi juhib Raspberry Pi. Raspperry PI-l on 8 digitalset väljundit, mille igale kontaktile saab panna relee.
Kasutatakse 8 releega valmis plokki. Igale releele saab määrata nimetuse.
Google kalendrisse koostad uue kalendri ja selle privaatse ical aadressi sisestad raspberrysse.
Kui kalenrdisse sisestad sündmuse siis pealkirjaks paned releele määratud nimetuse. See relee lülitatakse selleks ajaks sisse kui sündmus on aktiivne.
Programm töötleb iCal formaadis icl faili, seega on võimalik kasutada ükskõik millist muud kalendrit mis tunnistab ical formaati.

#Tarkvara
Programm koosneb kahest etapist.

1. tõmbab perioodiliselt google calendri faili

2. otsib välja sündmused ja lülitab releesi

Releed töötavad ka ilma internetiühendusta, lihtsalt ei saa uut programmi.


#Komponendid

*  Raspberry Pi
*  Releeplokk http://dx.com/p/8-channel-12v-relay-module-board-167491
*  SD kaart
*  Toiteadapter 5V (Raspberry jaoks)
*  Toiteadapter 12V (Releede jaoks)
*  USB Wifi moodul (Kui on vaja juhtmevaba ühendust)
*  Ühenduskaablid

#Skeem
 ![GPIO](http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout-rev2.jpg)



#Instaleerimine

Klooni repost kood. Lisa vajadusel vajalikud pythoni lisad GPIO ja icalendar ja pytz

#Konfiguratsioon

Releede nimetused ja kontaktide numbrid on failis run.py Kasutatakse plaadi numbreid.

pins={"relee1":7,"relee2":11,"relee3":13,"relee4":15,"relee5":12,"relee6":16,"relee7":18,"relee8":22}

iCalenderi faili seaded on kirjas start.sh 

Allalaaditud kalenrdi faili nimi peab olema basic.ics

Lisa root crontabi uus kirje

crontab -e

* * * * * /home/pi/relee/start.sh

#Käivitamine
Crontabis käivitatakse script automaatselt iga minuti järel.

Vaata et failidel oleks käivitusõigus. Käivitada tuleb root õigustes.