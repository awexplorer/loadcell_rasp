
import RPi.GPIO as gpio
import threading
import time
DAT =13
CLK=8
num=0
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(CLK, gpio.OUT)
def weight():
  i=0
  num=0
  gpio.setup(DAT, gpio.OUT)
  gpio.output(DAT,1)
  gpio.output(CLK,0)
  gpio.setup(DAT, gpio.IN)

  while gpio.input(DAT) == 1:
      i=0
  for i in range(24):
        gpio.output(CLK,1)
        num=num<<1

        gpio.output(CLK,0)

        if gpio.input(DAT) == 0:
            num=num+1

  gpio.output(CLK,1)
  num=num^0x800000
  gpio.output(CLK,0)
  wei=0
  wei=((num)/1406)
  print ((wei-6020)-95),"g"
  time.sleep(0.5)

while True:
 weight()

