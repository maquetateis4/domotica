"""Alejandro Vázquez Iglesias | MAQUETA TEIS 4"""
"""Fecha: 5/05/25"""

"""Programa 5"""
"""Simula un sistema de alarma con detección de movimiento"""
"""Pin 13 para un led neopixel"""
"""Pin 14 para un led blanco"""
"""Pin 15 digital para sensor PIR"""
"""Hay una cara enfadada  cuando hay presencia"""
"""Muestra una casa si no hay presencia"""

# -----------------------------------------------------------------------------------------------------------------------

from microbit import*
import neopixel
import music

# Configuración de pins
np = neopixel.NeoPixel(pin13, 1) 
sensor_pir = pin15
led_blanco = pin14

if alerta():
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

if modo_normal():
    # Mostrar casa matriz LEDs
    display.show(Image.HOUSE)

# loop principal
while True:
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
    sleep(100)

# -----------------------------------------------------------------------------------------------------------------------

