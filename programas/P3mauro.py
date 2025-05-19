"""Programa completo da fila 4 para a maqueta domótica."""
"Autor: Mauro"""
"Data: 5/5/25"""

# -----------------------------------------------------------------------------------------------------------------------

from microbit import *
import music

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)  # Enciende el pin 14 (LED)
        music.play(music.RINGTONE)   # Reproduce el tono RINGTONE
        sleep(5000)   # Mantiene el LED encendido durante 5 segundos
        pin14.write_digital(0)   # Apaga el pin 14 (LED)
# -----------------------------------------------------------------------------------------------------------------------
