from lib.electripyIO import ElectripyIO
from lib.electripyGlobals import *

# GPIO TEST

epy = ElectripyIO()

print "Board name : ", epy.getBoardName()

print "PWM TEST **************************"
while True :
    for a in range(0,255):
        epy.pwmWrite(19, a)
        epy.delay(20)
        print a
    
    for a in range(0,255):
        epy.pwmWrite(19, 255-a)
        epy.delay(20)
        print 255-a

# print "DIGITAL TEST **************************"
# for a in range(0,10):
#     epy.digitalWrite(19,HIGH)
#     print a, "HIGH"
#     epy.delay(400)
#     epy.digitalWrite(19,LOW)
#     print a, "LOW"
#     epy.delay(400)
#     
# print "**************************"

# print "ADC TEST **************************"
# epy.pinMode(25,INPUT_PULLDOWN)
# while True:
#     print epy.analogRead(25)
#     epy.delay(500)
# 

#epy.digitalWrite(19,LOW)
#epy.delay(1000)

#epy.digitalWrite(19,HIGH)
#epy.delay(1000)
# 
# # print "**************************"
# digitalWrite(12,HIGH)
# # print "**************************"
# digitalWrite(13,HIGH)
# # print "**************************"
# digitalWrite(13,LOW)
# # print "**************************"
# digitalRead(12)
# # print "**************************"
# 
# 
# # PWM test
# # print "**************************"
# pwmWrite(18, 255)
# # print "**************************"
# #a.pwmWrite(19, 255)
# # print "**************************"
# pwmWrite(22, 128)
# # print "**************************"
# pwmWrite(22, 15)
# # print "**************************"
# pwmWrite(23, 4000)
# # print "**************************"
# pwmWrite(24, -15)
# # print "**************************"
# setPwmPeriod(20000)
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


