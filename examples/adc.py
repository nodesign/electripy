from lib.electripy import *

print "Board name : ", getBoardName()

print "ADC TEST **************************"
pinMode(25,INPUT_PULLDOWN)
while True:
    print analogRead(25)
    delay(10)

