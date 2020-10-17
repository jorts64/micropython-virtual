import time
import requests
import json

baseurl = "http://localhost:5000/"

class DHTBaseI2C:
    def __init__(self):
        self.foo = 1
    def measure(self):
        foo = self.foo

class DHT12(DHTBaseI2C):
    def humidity(self):
        res = requests.get (baseurl+'dhtHread')
        return res.text

    def temperature(self):
        res = requests.get (baseurl+'dhtTread')
        return res.text

sensor = DHT12()

def toca(nota):
    res = requests.get (baseurl+'buzzerwrite/'+nota)
    return

def polsador():
    res = requests.get (baseurl+'switchread')
    return (res.text=="1")

class oled(DHTBaseI2C):
    def text(self,text,x,y):
        myobj = {"x": x,"y": y, "text": text}
        myjson = json.dumps(myobj)
        res = requests.get (baseurl+'oledwrite/'+myjson)
        time.sleep(1)
        return 

    def fill(self,color):
        myobj = {"x": -2,"y": -2, "text": 'VOID'}
        myjson = json.dumps(myobj)
        res = requests.get (baseurl+'oledwrite/'+myjson)
        time.sleep(1)
        return 
    def show(self):
        return

display = oled()

class NeoPixel:
    ORDER = (1, 0, 2, 3)

    def __init__(self, pin, n, bpp=3):
        self.n = n
        self.bpp = bpp
        self.buf = bytearray(n * bpp)
        

    def __setitem__(self, index, val):
        offset = index * self.bpp
        for i in range(self.bpp):
            self.buf[offset + self.ORDER[i]] = val[i]

    def __getitem__(self, index):
        offset = index * self.bpp
        return tuple(self.buf[offset + self.ORDER[i]] for i in range(self.bpp))

    def fill(self, color):
        for i in range(self.n):
            self[i] = color

    def write(self):
        RGBwrite()

led = NeoPixel(0, 7)

pep = ["off", "off", "off", "off", "off", "off", "off"]

def RGBwrite():
    for i in range (7):
        if (led[i][0]==1):
            pep[i]="red"  
        if (led[i][0]==2):
            pep[i]="yellow"  
        if (led[i][0]==3):
            pep[i]="green"  
        if (led[i][0]==4):
            pep[i]="cyan"  
        if (led[i][0]==5):
            pep[i]="blue"  
        if (led[i][0]==6):
            pep[i]="magenta"  
        if (led[i][0]==7):
            pep[i]="white"  
        if (led[i][0]==8):
            pep[i]="off"
    myobj = {"led0": pep[0],"led1": pep[1],"led2": pep[2],"led3": pep[3],"led4": pep[4],"led5": pep[5],"led6": pep[6]}
    myjson = json.dumps(myobj)
    res = requests.get (baseurl+'rgbwrite/'+myjson)
    return

color = {'vermell' : (1,0,0) , 'groc' : (2,0,0), 'verd' : (3,0,0), 'cyan' : (4,0,0), 'blau' : (5,0,0),  'magenta' : (6,0,0),'blanc' : (7,0,0), 'apagat' : (8,0,0)}

