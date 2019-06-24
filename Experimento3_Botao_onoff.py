import time
from gpio_96boards import GPIO


PortaLed = GPIO.gpio_id('GPIO_E')
Btn = GPIO.gpio_id('GPIO_A')

pins = ((PortaLed, 'out'),(Btn, 'in'),)


def readDigital(gpio):
	digital = [0,0]
	digital[0] = gpio.digital_read(PortaLed)
        digital[1] = gpio.digital_read(Btn)
	return digital

def piscaled(gpio):
	gpio.digital_write(PortaLed, GPIO.HIGH)
        print('Led Turn Off')
        time.sleep(1)
        gpio.digital_write(PortaLed, GPIO.LOW)	
        print('Led Turn On')	
        time.sleep(1)
	
while True:
    with GPIO(pins) as gpio:
        digital = readDigital(gpio)
        if digital[1]==1:
            print('Pisca led acionado')
            piscaled(gpio)  
            time.sleep(1)
        else:
            print('Pisca led nao acionado')
            time.sleep(1)
        


	
