from flask import Flask, render_template
app = Flask(__name__)

dhtT = 25
dhtH = 33
rgbval={"led0":"blue","led1":"blue","led2":"off","led3":"off","led4":"blue","led5":"off","led6":"off"}
switchval = 0
nota = 'off'
oledval={"x": -1, "y": -1, "text": "VOID"}

@app.route('/')
def lab():
   return render_template("index.html")


@app.route('/dht')
def dht():
   return render_template("dht.html")


@app.route('/dhtTdec')
def dhtTdec():
   global dhtT
   dhtT = dhtT - 1
   return str(dhtT)

@app.route('/dhtTinc')
def dhtTinc():
   global dhtT
   dhtT = dhtT + 1
   return str(dhtT)

@app.route('/dhtTread')
def dhtTread():
   global dhtT
   return str(dhtT)

@app.route('/dhtHdec')
def dhtHdec():
   global dhtH
   dhtH = dhtH - 1
   return str(dhtH)

@app.route('/dhtHinc')
def dhtHinc():
   global dhtH
   dhtH = dhtH + 1
   return str(dhtH)

@app.route('/dhtHread')
def dhtHread():
   global dhtH
   return str(dhtH)


@app.route('/rgb')
def rgb():
   return render_template("rgb.html")

@app.route('/rgbread')
def rgbread():
   global rgbval
   return rgbval

@app.route('/rgbwrite/<rgbnew>')
def rgbwrite(rgbnew):
   global rgbval
   rgbval = rgbnew
   return rgbval


@app.route('/switch')
def switch():
   return render_template("switch.html")

@app.route('/switchread')
def switchread():
   global switchval
   return str(switchval)

@app.route('/on')
def on():
   global switchval
   switchval = 1
   return str(switchval)

@app.route('/off')
def off():
   global switchval
   switchval = 0
   return str(switchval)


@app.route('/buzzer')
def buzzer():
   return render_template("buzzer.html")

@app.route('/buzzerread')
def buzzerread():
   global nota
   return nota

@app.route('/buzzerwrite/<notanew>')
def buzzerwrite(notanew):
   global nota
   nota = notanew
   return nota

@app.route('/oled')
def oled():
   return render_template("oled.html")

@app.route('/oledread')
def oledread():
   global oledval
   return oledval

@app.route('/oledwrite/<olednew>')
def oledwrite(olednew):
   global oledval
   oledval = olednew
   return oledval




if __name__ == '__main__':
   app.run(debug = True)
