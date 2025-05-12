"""Programa completo da fila 4 para a maqueta domótica.""" 
"""Autores: Alejandro Vázquez, Mauro"""
"""Data: 28/4/25"""

# -----------------------------------------------------------------------------------------------------------------------

from microbit import *
import machine

# Configura pin para P2
servo = machine.PWM(machine.Pin(2))
servo.freq(50)

# mover servo ángulo dado (0º a 180º)
def set_angle(angle):
    duty = int(26 + (angle / 180) * 102)  # mapeo del ángulo al duty (26-128 aprox)
    servo.duty(duty)

# Estado inicial
angle = 0
set_angle(angle)

while True:
    if button_b.was_pressed():
        if angle == 0:
            angle = 90
        else:
            angle = 0
        set_angle(angle)
        sleep(200)  # anti-loop

# -----------------------------------------------------------------------------------------------------------------------
