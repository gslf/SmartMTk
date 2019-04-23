# SmartMTk
A smart Monster Truck powered by Raspberry PI3 B+ - WIP project for a Wifi controlled Monster Truck with Camera, Sensors and AI features.

### Components:
* Raspberry PI3 B+
* MicroSD card (8 GB at least)
* TB6612 Motor Driver
* Cheap RC Monster Truck

### HowTo
1. [Raspberry setup](#raspberry-headless-setup)

2. [Wiring](#wiring-diagram)

3. Test wiring & controls
    * Clone this repository on Raspberry:
    ```
    git clone https://github.com/Promezio/SmartMTk.git
    ```
    * Run test routine:
    ```python
    python3 SmartMTk/src/test.py
    ```
    
4. Run server
    * ToDo . . .

### Raspberry Headless Setup
* Download Rasbian Strech Lite [FROM THE OFFICIAL WEBSITE](https://www.raspberrypi.org/downloads/raspbian/)
* Download Etcher [FROM OFFICIAL WEBSITE](https://www.balena.io/etcher/)
* Flash rasbian image on MicroSd card
* Enable SSH by placing a file named "ssh" (without any extension) onto the boot partition of the MicroSD card.
* Enable WiFi connection by placing a file "wpa_supplicant.conf" onto the boot partition. A typical file is like this:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«your_ISO-3166-1_two-letter_country_code»

network={
    ssid="«your_SSID»"
    psk="«your_PSK»"
    key_mgmt=WPA-PSK
}
```
* Turn on the Raspberry
* Use your favourite SSH client (Terminal, PowerShell, PUTTY, ...)  to access the Pi. 

### Wiring diagram
![SmartMTk wiring diagram](https://github.com/Promezio/SmartMTk/blob/master/SmartMTk_wiring.png)


