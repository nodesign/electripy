from lib.electripy import *

print "Board name : ", getBoardName()

print "DIGITAL INPUT TEST **************************"
#pinMode(25,INPUT_PULLDOWN)
while True:
    print digitalRead(25)
    delay(10)

