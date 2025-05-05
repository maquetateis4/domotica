"""Alejandro Vázquez Iglesias"""
"""5/05/25"""
"""Programa 5"""

# -----------------------------------------------------------------------------------------------------------------------

from microbit import *
import neopixel
import music

# Configuración de pins
np = neopixel.NeoPixel(pin13, 1) 
led_blanco = pin14
sensor_pir = pin15

def alerta():
    # Sonar ring 2 veces
    music.play(music.RINGTONE, wait=True)
    sleep(100)
    music.play(music.RINGTONE, wait=True)

    # Alerta visual y LED blanco
    for i in range(5):
        # color rojo
        np[0] = (255, 0, 0)
        np.show()
        led_blanco.write_digital(1)
        display.show(Image.ANGRY)
        sleep(500)

        # Apagar todo
        np[0] = (0, 0, 0)
        np.show()
        led_blanco.write_digital(0)
        display.clear()
        sleep(500)

def modo_normal():
    # Mostrar casa matriz LEDs
    display.show(Image.HOUSE)

# loop principal
while True:
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
    sleep(100)
