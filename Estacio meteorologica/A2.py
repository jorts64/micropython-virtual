from D1mini import *

led[0] = color['blanc']
led[1] = color['vermell']
led[2] = color['groc']
led[3] = color['verd']
led[4] = color['cyan']
led[5] = color['blau']
led[6] = color['magenta']
led.write()

while True:
    time.sleep(1)
    led[0] = color['apagat']
    led.write()
    time.sleep(1)
    led[0] = color['blanc']
    led.write()
 