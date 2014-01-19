from lib.electripyIO import *
from lib.electripyGlobals import *

# GPIO TEST

# print "**************************"
digitalWrite(12,HIGH)
# print "**************************"
digitalWrite(12,LOW)
# print "**************************"
digitalWrite(12,HIGH)
# print "**************************"
digitalWrite(13,HIGH)
# print "**************************"
digitalWrite(13,LOW)
# print "**************************"
digitalRead(12)
# print "**************************"


# PWM test
# print "**************************"
pwmWrite(18, 255)
# print "**************************"
#a.pwmWrite(19, 255)
# print "**************************"
pwmWrite(22, 128)
# print "**************************"
pwmWrite(22, 15)
# print "**************************"
pwmWrite(23, 4000)
# print "**************************"
pwmWrite(24, -15)
# print "**************************"
setPwmPeriod(20000)
# print "fade out"
# for i in xrange(0,256):
#     a.pwmWrite(19,i)
#     print "**************************"
# print "fade in"
# for i in xrange(0,256):
#     a.pwmWrite(19,255-i)
#     print "**************************"
# print "fade out"
# for i in xrange(0,256):
#     a.pwmWrite(19,i)
#     print "**************************"


