# Google Assistant Led
Smart Home Automation to control the light using Google Assistant

The idea behind Google assistant-controlled Home automation is to control home devices with voice. On the market there are many devices available to do that, but making our own is awesome. In this project, the Google assistant requires voice commands. Adafruit account which is a cloud based free IoT web server used to create virtual switches, is linking to IFTTT website abbreviated as “If This Then That” which is used to create if-else conditional statements. The voice commands for Google assistant have been added through IFTTT website. In this home automation, as the user gives commands to the Google assistant, LEDs can be controlled accordingly. The commands given through the Google assistant are decoded and then sent to the microcontroller, the microcontroller in turn controls the relays connected to it. The device connected to the respective relay can be turned On or OFF as per the users request to the Google Assistant. The microcontroller used is Raspberry Pi and the communication between the microcontroller and the application is established via Wi-Fi (Internet).

#Requirements

Hardware requirements:

1.Raspberry Pi  

2.Grove PI Kit   

3.LEDs


Software and protocol requirements:

1.Adafruit IO

2.VNC viewer

3.PuTTY for connection to the raspberry

4.IFTTT protocol
