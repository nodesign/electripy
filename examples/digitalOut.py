from lib.electripy import *

print "Board name : ", getBoardName()

print "DIGITAL TEST **************************"
for a in range(0,10):
    digitalWrite(19,HIGH)
    print a, "HIGH"
    delay(400)
    digitalWrite(19,LOW)
    print a, "LOW"
    delay(400)
    
    
stop()