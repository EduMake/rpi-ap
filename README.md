# rpi-ap
RPi config for using rpi as an access point which uses capture portal techniques to give mobiles a web ui to physical computing projects. As setup it does not give internet access 

## Install the software

```
sudo aptitude install iw hostapd dnsmasq python-serial
```

* copy the files from the /file into the same position on the Pi (FIXME)
* Use wpa_cli  to add the networks you want (use 'save config' to store it)
* In /etc/hostapd/hostapd.conf set ssid=EduMakeRPi to whatever you want to call your network
* Set the SSIDs you would like it to try to connect to first in /etc/rc.local
* It will scan for the network names in ssids= () and attach to one those if it can
* If not it will setup an Access Point using 10.5.5.1 for the RPi and 10.5.5.100 -150 for the dhcp range

* To set up a way physically force own AP (so you can force that behaviour even when at home base):-
*	Wire GPIO 14 and 15 together 
*	use raspi-config -> Serial to Disable shell and kernel messages on the serial connection.
* the code will check if the GPIO 14 and 15 are linked together (with a jumper / wire) and skip the searching if they are


##Techniques based on

http://www.penguintutor.com/news/raspberrypi/wireless-hotspot

https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point/  using the dnsmasq version

