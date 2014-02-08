from lib.electripy import *

print "Board name : ", getBoardName()


print "INTERRUPTS TEST **************************"
def hello(data):
    print "interrupt ", INTERRUPT_TYPE[data]

attachInterrupt(25, CHANGE, hello)

for a in range(0,15):
    delay(1000)
    print a
    
detachInterrupt(25)
stop()