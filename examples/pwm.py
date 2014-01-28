from lib.electripy import *

print "Board name : ", getBoardName()

print "PWM TEST **************************"
for i in range(0,10) :
    for a in range(0,255):
        pwmWrite(19, a)
        delay(10)
        print a
    
    for a in range(0,255):
        pwmWrite(19, 255-a)
        delay(10)
        print 255-a
        
        
stop()