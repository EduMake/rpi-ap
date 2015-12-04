# rpi-ap
RPi config for using rpi as an access point which uses capture portal techniques to give mobiles a web ui to physical computing projects. As setup it does not give internet access 

sudo aptitude install iw hostapd dnsmasq



use wpa_cli  to add the networks you want (use 'save config' to store it)

in hostapd.conf set ssid=EduMakeRPi to whatever you want to call your network

All the config in rc.local  uses 10.5.5.1 for the RPi and 10.5.5.100 -150 for the dhcp range


techniques based on

http://www.penguintutor.com/news/raspberrypi/wireless-hotspot

https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point/  using the dnsmasq version

