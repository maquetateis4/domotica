"""P1 maqueta. Sensor de temperatura
Autor: Bernardo Álvarez
5/4/25"""

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
np.clear()
rele = pin16  # relé conectado ao pin 16

while True:
    temperatura = temperature()  # gardamos valor da temperatura

    if temperatura > 18:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(1)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(0)  # Apagar o LED normal

    sleep(1000)  # Esperar 1 segundo


