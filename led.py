import time
from grovepi import *
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'aio_MLoQ43SlhGi7Jr7v94X5ky7x26Zr'
ADAFRUIT_IO_USERNAME = 'mr_rsr'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#feed=aio.feeds()
ledRed=3
ledGreen=4
pinMode(ledRed,'OUTPUT')
pinMode(ledGreen,'OUTPUT')
digitalGreen = aio.feeds('greenled')
digitalRed =   aio.feeds('redled')


while True:
    datagreen = aio.receive(digitalGreen.key)
    #time.sleep(0.5)
    datared= aio.receive(digitalRed.key)
    #print(int(datared.value))
    digitalWrite(3,1) if int(datared.value)==1 else digitalWrite(3,0)
    digitalWrite(4,1) if int(datagreen.value)==1 else digitalWrite(4,0)
    
    time.sleep(0.5)