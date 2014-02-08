from lib.electripy import *

print "Board name : ", getBoardName()

print "PWM TEST **************************"
rng = 255
setPwmLimit(rng)
for i in range(0,10) :
    for a in range(0,rng):
        pwmWrite(19, a)
        delay(10)
        print a
    
    for a in range(0,rng):
        pwmWrite(19, rng-a)
        delay(10)
        print rng-a
        
        
stop()