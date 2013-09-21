nutirelee
=========

Releede juhtimine Google kalendriga

# Kirjeldus
Releedega on võimalik juhtida erinevaid elektrilisi seademid. Releesi juhib Raspberry Pi. Raspperry PI-l on 8 digitalset väljundit, mille igale kontaktile saab panna relee.
Kasutatakse 8 releega valmis plokki. Igale releele saab määrata nimetuse.
Google kalendrisse koostad uue kalendri ja selle privaatse ical aadressi sisestad raspberrysse.
Kui kalenrdisse sisestad sündmuse siis pealkirjaks paned releele määratud nimetuse. See relee lülitatakse selleks ajaks sisse kui sündmus on aktiivne.

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

#Skeem
 ![GPIO](http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout-rev2.jpg)



#Instaleerimine

#Konfiguratsioon

url = [google calender ical aadress]

pin7 = lamp

pin11 = pump

........

#Käivitamine
