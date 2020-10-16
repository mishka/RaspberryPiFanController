from gpiozero import OutputDevice
from datetime import date, datetime
from time import sleep
from os import popen

PIN = 12
THRESHOLD = 43

def log(text):
    current_date = date.today().strftime('%d/%m%y')
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f'| {current_date} {current_time} | {text}')

def get_temp():
    temp_data = popen('vcgencmd measure_temp').readline()
    return int(temp_data[5:-5])

print('Setting up the GPIO pin:', PIN)
fan = OutputDevice(PIN)

while 1:
    temperature = get_temp()

    if temperature > THRESHOLD and not fan.value:
        fan.on()
        log('Turning on the fan.')
    elif fan.value and temperature < THRESHOLD:
        fan.off()
        log('Turning off the fan.')

    sleep(5)
