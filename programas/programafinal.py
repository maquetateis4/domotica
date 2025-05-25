"""Alejandro Vázquez Iglesias | MAQUETA TEIS 4 | Sistema Integrado
Fecha: 05/05/25"""

from microbit import *
import neopixel
import music
import servo

# Configuración de pines
# Programa 1: Temperatura
np_temp = neopixel.NeoPixel(pin13, 1)  # 1 LED Neopixel para temperatura
rele_ventilador = pin16
sensor_temp = pin0  # Pin analógico

# Programa 2: Luz
sensor_luz = pin1
led_luz = pin14  # Compartido con otros programas

# Programa 3: Botón A
boton_a = pin5  # Ajustar según maqueta física

# Programa 4: Servo con botón B
boton_b = pin6  # Ajustar según maqueta física
servo_motor = servo.Servo(pin2)
angulo = 0

# Programa 5: Detección de movimiento
np_alarma = neopixel.NeoPixel(pin13, 6)  # 6 LEDs para alarma
sensor_pir = pin15
# led_blanco ya definido como pin14 (led_luz)

# Funciones del Programa 1: Temperatura
def actualizar_temperatura():
    temp_value = sensor_temp.read_analog()
    temp_celsius = (temp_value * 3.3 / 1024) * 100  # Conversión ejemplo (ajustar)
    
    if temp_celsius < 20:
        np_temp[0] = (0, 0, 255)     # Azul
    elif 20 <= temp_celsius < 22:
        np_temp[0] = (0, 255, 0)     # Verde
    elif 22 <= temp_celsius < 24:
        np_temp[0] = (255, 165, 0)  # Naranja
    else:
        np_temp[0] = (255, 0, 0)    # Rojo
        rele_ventilador.write_digital(1)  # Ventilador ON
    
    np_temp.show()
    
    if temp_celsius < 24:
        rele_ventilador.write_digital(0)  # Ventilador OFF

# Funciones del Programa 2: Luz
def control_luz():
    luz = sensor_luz.read_analog()
    if luz < 50:  # Ajustar valor según condiciones
        led_luz.write_digital(1)  # Encender
    else:
        led_luz.write_digital(0)  # Apagar

# Funciones del Programa 3: Botón A
def accion_boton():
    for _ in range(5):  # Parpadear 5 veces
        led_luz.write_digital(1)
        music.play(music.RINGTONE)
        sleep(500)
        led_luz.write_digital(0)
        sleep(500)

# Funciones del Programa 4: Servo
def control_servo():
    global angulo
    if boton_b.read_digital() == 1:
        angulo += 10
        if angulo > 90:
            angulo = 0
        servo_motor.write_angle(angulo)
        sleep(500)  # Evitar rebotes

# Funciones del Programa 5: Detección de movimiento (versión mejorada)
def modo_normal():
    display.show(Image.HOUSE)

def alerta():
    # Sonar alerta 2 veces
    music.play(music.BA_DING, wait=True)
    sleep(100)
    music.play(music.BA_DING, wait=True)

    for i in range(5):
        # Encender todos los neopixels en rojo
        for j in range(6):
            np_alarma[j] = (255, 0, 0)
        np_alarma.show()

        led_luz.write_digital(1)
        display.show(Image.ANGRY)
        sleep(500)

        # Apagar
        for j in range(6):
            np_alarma[j] = (0, 0, 0)
        np_alarma.show()

        led_luz.write_digital(0)
        display.clear()
        sleep(500)

# Inicialización
modo_normal()  # Mostrar estado normal al iniciar

# Bucle principal
while True:
    # Ejecutar todas las funcionalidades
    actualizar_temperatura()
    control_luz()
    
    if boton_a.read_digital() == 1:
        accion_boton()
    
    control_servo()
    
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
    
    sleep(100)
