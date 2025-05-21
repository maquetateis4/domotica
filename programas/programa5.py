"""𝔸𝕝𝕖𝕛𝕒𝕟𝕕𝕣𝕠 𝕍á𝕫𝕢𝕦𝕖𝕫 𝕀𝕘𝕝𝕖𝕤𝕚𝕒𝕤 | 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 | S𝕚𝕤𝕥𝕖𝕞𝕒 𝕕𝕖 𝕒𝕝𝕒𝕣𝕞𝕒 𝕔𝕠𝕟 𝕕𝕖𝕥𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕞𝕠𝕧𝕚𝕞𝕚𝕖𝕟𝕥𝕠
𝔽𝕖𝕔𝕙𝕒: 𝟝/𝟘𝟝/𝟚𝟝"""

#--------------------------------------------------------------------------------------------------------------

from microbit import *
import neopixel
import music

# Configuración de pins
np = neopixel.NeoPixel(pin13, 6) 
sensor_pir = pin15
led_blanco = pin14

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

# Loop principal
while True:
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
    sleep(100)


#--------------------------------------------------------------------------------------------------------------
