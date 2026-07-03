import time
import plyer
from plyer import notification
import pymsgbox as msg
while True:
    time.sleep(1800)
    notification.notify(
        title='Drink some water.',
        message='Drink some water you might be thirsty.',
        app_name='Python',
        timeout=60
    )
    msg.alert("Drink some water you might be thirsty.", "Remember!", button="I did")
    time.sleep(900)
    notification.notify(
        title='Give a break!',
        message='Give a break for 5 minutes! You are working on pc for 45 minutes without a break.',
        app_name='Python',
        timeout=300
    )
    msg.alert("Give a break right now!", "Remember!", button="I did")
