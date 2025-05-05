"""Programa completo da fila 4 para a maqueta domótica. 
"Autores: Alejandro Vázquez, Mauro"
"Data: 28/4/25"

# -----------------------------------------------------------------------------------------------------------------------

from microbit import *

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)
        sleep(5000)
        music.play(music.RINGTONE)
        sleep
# -----------------------------------------------------------------------------------------------------------------------
