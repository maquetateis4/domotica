"""Programa completo da fila 3 para a maqueta domótica."""
"Autor: Mauro"""
"Data: 5/5/25"""

# -----------------------------------------------------------------------------------------------------------------------

from microbit import *

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)
        sleep(500)
        music.play(music.RINGTONE)
        sleep
# -----------------------------------------------------------------------------------------------------------------------
