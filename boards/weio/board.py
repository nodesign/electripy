### 
#
# Electripy, HAL library for Python
#
# Library was originally created for WeIO, www.we-io.net and than forked as a
# separate project in order to promote concept of using interpreted languages
# in microcontrolers.
# 
# This library is common effort of their original creators
# Uros PETREVSKI, Drasko DRASKOVIC and 8devices team
#
#         ___       ___  __  ___  __     __      
#        |__  |    |__  /  `  |  |__) | |__) \ / 
#        |___ |___ |___ \__,  |  |  \ | |     |  
#
#          Hardware Abstraction Layer Library
#                       for Python
#
# The MIT License (MIT)
# 
# Copyright (c) 2014 Nodesign.net, Uros PETREVSKI, Drasko DRASKOVIC
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Authors : 
# Uros PETREVSKI <uros@nodesign.net>
# Drasko DRASKOVIC <drasko.draskovic@gmail.com>
#
###

import wirings
import uperDriver

""" weio board for testing purposes """
class Board():
    def __init__(self, internalCallBack, serial = "/dev/ttyACM0"):
        """Init coresponding wirings file"""
        self.wirings = wirings.Wirings()
        self.name = 'weio'
        #print serial
        self.uper = uperDriver.UPER(internalCallBack, serial_port=serial)
        
        self.pwmBeginCalled = False
        
    def getBoardName(self):
        return self.name
        
    def getWirings(self):
        return self.wirings

    def digitalWrite(self, pin, state):
        #print "weioBoard.digitalWrite(pin, state) has been called with parameters: %d, %d" % (pin, state)
        self.uper.digitalWrite(self.wirings.PINS[pin], state)
        
    def pinMode(self, pin, mode) :
        """Sets io mode for pin. Available modes are : INPUT_HIGHZ, INPUT_PULLDOWN, INPUT_PULLUP, INPUT_ADC, OUTPUT, OUTPUT_PWM"""
        if (mode == self.wirings.INPUT_ADC) or (mode == self.wirings.OUTPUT_PWM):
            self.uper.setSecondary(self.wirings.PINS[pin])
            #print "Setting secondary interface on %d pin" % (pin)
            if (mode == self.wirings.OUTPUT_PWM):
                self.pwmBegin(pin)
                #print "init pwm"
        else :
            self.uper.setPrimary(self.wirings.PINS[pin])
            #print "weioBoard.setPrimary(pin, mode) has been called with parameters: %d" % (pin)
            self.uper.pinMode(self.wirings.PINS[pin], mode)
            #print "weioBoard.pinMode(pin, mode) has been called with parameters: %d, %d" % (pin, mode)
        
    def digitalRead(self, pin):
        #print "weioBoard.digitalRead(pin) has been called with parameter: %d" % pin
        return self.uper.digitalRead(self.wirings.PINS[pin])
        
    def analogRead(self, pin):
        #print "weioBoard.analogRead(pin) has been called with parameter: %d" % pin
        adcPin = self.wirings.ADCS.index(pin)
        return self.uper.analogRead(adcPin)
        
    def pwmWrite(self,pin, value):
        if ((pin >= self.wirings.PWMS[0]) and (pin <= self.wirings.PWMS[2])):
            pwmPin = self.wirings.PWMS.index(pin)
            if (self.pwmBeginCalled is False):
                self.setPwmPeriod(self.wirings.PWM_PERIOD)
            self.uper.pwm0_set(pwmPin, value)
        elif ((pin >= self.wirings.PWMS[3]) and (pin <= self.wirings.PWMS[-1])):
            pwmPin = abs(3-self.wirings.PWMS.index(pin))
            if (self.pwmBeginCalled is False):
                self.setPwmPeriod(self.wirings.PWM_PERIOD)
            self.uper.pwm1_set(pwmPin, value)
            
    def setPwmPeriod(self, period):
        # UPER has 2 banks, activate all banks. Use board specific functions to call specific banks
        print "PERIOD ", period
        self.uper.pwm0_begin(period)
        self.uper.pwm1_begin(period)
        self.pwmBeginCalled = True
        
    def attachInterrupt(self, interrupt):
        #print "Interrupt attached on %d %d %d" % (interrupt.myid, self.wirings.PINS[interrupt.pin], interrupt.mode)
        self.uper.attachInterrupt(interrupt.myid, self.wirings.PINS[interrupt.pin], interrupt.mode)
    
    def detachInterrupt(self, interrupt):
        self.uper.detachInterrupt(interrupt.myid)

    def getAvailableInterruptId(self) :
        for i in range(0,self.wirings.HARD_INTERRUPTS):
            if self.interrupts[i] == None:
                return i
        print "weioBoard.getAvailableInterruptId, there is only %s interrupts available" % self.wirings.HARD_INTERRUPTS 
        return None
    
    def stop(self):
        self.uper.stop()

####################################################### SPECIFIC BOARD FUNCTIONS
    def pwmBegin(self, pin):
        if ((pin >= self.wirings.PWMS[0]) and (pin <= self.wirings.PWMS[2])):
            self.uper.pwm0_begin(self.wirings.PWM_PERIOD)
        elif ((pin >= self.wirings.PWMS[3]) and (pin <= self.wirings.PWMS[-1])):
            self.uper.pwm1_begin(self.wirings.PWM_PERIOD)

            
