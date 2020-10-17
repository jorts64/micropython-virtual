
from D1mini import *
while True:
	sensor.measure()
	print("La temperatura ambiental es de", sensor.temperature(), "graus Celsius")
	print("Hi ha un", sensor.humidity(), "% d'humitat relativa")
	time.sleep(4)
	
