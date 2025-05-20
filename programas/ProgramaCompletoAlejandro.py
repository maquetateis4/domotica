""" Programa de automatización dunha maqueta
Autor: Bernardo
Data 20/05/2025"""

from microbit import *
import neopixel
import music

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
            np[j] = (255, 0, 0)
        np.show()

        led_blanco.write_digital(1)
        display.show(Image.ANGRY)
        sleep(500)

        # Apagar
        for j in range(6):
            np[j] = (0, 0, 0)
        np.show()

        led_blanco.write_digital(0)
        display.clear()
        sleep(500)

modo_normal()  # Mostrar estado normal al iniciar
np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
np.clear()
rele = pin16  # relé conectado ao pin 16 
sensor_pir = pin15
led_blanco = pin14

while True:
    # Programa1 ilumina NP segundo a tª 
    temperatura = temperature()  # gardamos valor da temperatura

    if temperatura > 18:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(0)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(1)  # Apagar o LED normal

    # Programa 4 simula un timbre con luz e son
    if button_a.is_pressed():
        pin14.write_digital(1)  # Enciende el pin 14 (LED)
        music.play(music.RINGTONE)   # Reproduce el tono RINGTONE
        sleep(5000)   # Mantiene el LED encendido durante 5 segundos
        pin14.write_digital(0)   # Apaga el pin 14 (LED)
            
    # Programa 5 simula unha alarma con sensor PIR
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
   
    sleep(100)

