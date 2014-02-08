from lib.electripy import *
from devices.servo import Servo

print "Board name : ", getBoardName()

print "SERVO TEST **************************"
servoPin = 19
potentiometerPin = 25

s = Servo(getBoard())
while True :
    val = analogRead(25) 
    angle = int(proportion(val, 0, 1023, 0,180))
    s.write(19,angle)
    delay(20)