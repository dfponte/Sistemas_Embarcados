import time
from gpio_96boards import GPIO


PortaLed = GPIO.gpio_id('GPIO_E')

pins = ((PortaLed, 'out'),)


def piscaled(gpio):
	gpio.digital_write(PortaLed, GPIO.HIGH)
        print('Led Turn Off')
        time.sleep(1)
        gpio.digital_write(PortaLed, GPIO.LOW)	
        print('Led Turn On')	
        time.sleep(1)
	
while True:
    with GPIO(pins) as gpio:
        piscaled(gpio)
        


	
