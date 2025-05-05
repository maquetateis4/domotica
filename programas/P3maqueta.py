from microbit import *

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)
        sleep(5000)
        music.play(music.RINGTONE)
        sleep
