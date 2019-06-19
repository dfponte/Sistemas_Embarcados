#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Projeto 1 - Disciplina Sistemas Embarcados - IFPI
resumo: controle de ativação do Led inserido
na porta E da placa Mezzanine pelo terminal de
comando do linux.
Prof.Daniel Ferreira da Ponte
Data:13/05/2019 - 
"""

import time
from gpio_96boards import GPIO 

PortaLed = GPIO.gpio_id('GPIO_E')

pins = ((PortaLed, 'out'),)
valor = True
with GPIO(pins) as gpio:	
    while valor:
        gpio.digital_write(PortaLed, GPIO.LOW)	
        print('Led Turn Off')	
        print('Deseja ligar Led')	
        ligado = True
        while ligado:
           ligado = input('Digite True se sim ou False para não : ')
           print('Ligado no modo %s'%(ligado))
           time.sleep(1)
           if ligado:
                gpio.digital_write(PortaLed, GPIO.HIGH)
                print('Led Turn On')	
                time.sleep(0.5)


	
