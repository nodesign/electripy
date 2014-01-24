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
from lib.electripyGlobals import *
import time

###
# User API functions for GPIO
###

class ElectripyIO():
    
    def __init__(self):
        self.board = targetBoard.Board(self.mainInterrupt)
            
        self.declaredPins = []
        for i in range(0,len(pins)):
            self.declaredPins.append(-1)
            
        self.interrupts = []
        for i in range(0, HARD_INTERRUPTS):
            # 1 is available
            self.interrupts.append(None)

    def mainInterrupt(self, data):
        myid = data[1][0]
        for inter in self.interrupts:
            if inter.myid == myid:
                inter.callback(data[1][1])
                break
    # 
    # def mainInterrupt(self, data):
    #     """ Do following stuff:
    #     1) mainInterrupt pre-call generic stuff (generic stuff before calling board's driver IO)
    #     2) call board driver's IO function (custom for every board)
    #     3) mainInterrupt post-call generic stuff
    #     """
    #     result = None
    #     
    #     #do some pre-init
    # 
    #     #Check if the board implements this function
    #        
    #     myid = data[1][0]
    #     for inter in self.interrupts:
    #        if inter.myid == myid:
    #            inter.callback(data[1][1])
    #            break
    # 
    #     #do some post-init
    # 
    #     return result
        
    def getBoardName(self):
        return self.board.getBoardName()

    def pinMode(self, pin, mode):
        result = None
        if hasattr(self.board, 'pinMode'):
            result = self.board.pinMode(pin, mode)
            self.declaredPins[pin] = mode
        return result
            
    def digitalWrite(self, pin, state):
        res = None
        if hasattr(self.board, 'digitalWrite'):
            if self.declaredPins[pin] != OUTPUT:
                self.board.pinMode(pin, OUTPUT)
                self.declaredPins[pin] = OUTPUT
    
            res = self.board.digitalWrite(pin, state)
        return res
    
    def digitalRead(self, pin):
        res = None
        if hasattr(self.board, 'digitalRead'):
            # Force input mode (High Impedance) if input was not declared
            if (self.declaredPins[pin] != INPUT_HIGHZ) and (self.declaredPins[pin] != INPUT_PULLUP) and (self.declaredPins[pin] != INPUT_PULLDOWN) :
                self.board.pinMode(pin, INPUT_HIGHZ)
                self.declaredPins[pin] = INPUT_HIGHZ
            res = self.board.digitalRead(pin)
        return res
    
    def analogRead(self, pin):
        res = None
        if hasattr(self.board, 'analogRead'):
            if ((pin >= adcs[0]) and (pin <= adcs[-1])):
                if self.declaredPins[pin] != INPUT_ADC:
                    self.declaredPins[pin] = INPUT_ADC
                    self.board.pinMode(pin, INPUT_ADC)
                res = self.board.analogRead(pin)    
            else:
                print "Pin %d is not ADC pin" % pin           
        return res
    
    def pwmWrite(self, pin, value):
        res = None
        if hasattr(self.board, 'pwmWrite'):
            if (pin >= pwms[0]) and (pin <= pwms[-1]):
                if self.declaredPins[pin] != OUTPUT_PWM:
                    self.declaredPins[pin] = OUTPUT_PWM
                    self.board.pinMode(pin, OUTPUT_PWM)
                
                # value limiters
                if (value < 0) :
                    value = 0
                if (value > PWM_LIMIT):
                    value = PWM_LIMIT
                
                # do proportion calculus
                # People think in bit precision rather in microseconds. It's common to connect sensor outputs to pwm
                # so we have to make a small proportion calculus here to make interface more friendly
                # for example if period is 1000us and limit 255 (8bit), 1000 will be divided to 255 steps to drive pwm
                out = self.proportion(value, 0, PWM_LIMIT, 0, PWM_PERIOD)
                res = self.board.pwmWrite(pin, int(out))
            else :
                print "Pin %d is not PWM pin" % pin
        else:
            print "electripyError: Board %s has no function pwmWrite()" % self.board.name
        return res
    
    def analogWrite(self, pin, value):
        """Defining synonime of pwmWrite to match arduino syntax"""
        res = None
        if hasattr(self.board, 'pwmWrite'):
            res = self.board.pwmWrite(pin, value)
    
    def setPwmPeriod(self, period):
        res = None
        if hasattr(self.board, 'setPwmPeriod'):
            if ((period >= 0) and (period <= PWM_PERIOD_LIMIT_CONST)): 
                PWM_PERIOD = int(period)
                res = self.board.setPwmPeriod(period)
            else :
                print "electripyError: PWM period can be only between 0-" % PWM_PERIOD_LIMIT_CONST
                
        print "electripyError: Board %s has no function setPwmPeriod()" % self.board.name
        return res
        
    def setPwmLimit(self, limit):
        res = None
        if hasattr(self.board, 'setPwmPeriod'):
            if ((limit > 0) and (limit <= PWM_LIMIT)):
                PWM_LIMIT = int(limit)
            else :
                print "electripyError: PWM period can be only between 1-" % PWM_PERIOD_LIMIT_CONST
        print "electripyError: Board %s has no function setPwmLimit()" % self.board.name
        return res

    def setPwmPeriod(self, period):
        res = None
        if hasattr(self.board, 'setPwmPeriod'):
            res = self.board.setPwmPeriod(period)
        return res

    def setPwmLimit(self, limit):
        res = None
        if hasattr(self.board, 'setPwmLimit'):
            res = self.board.setPwmLimit(limit)
        return res

    def getAvailableInterruptId(self) :
        for i in range(0,HARD_INTERRUPTS):
            if self.interrupts[i] == None:
                return i
        print "weioBoard.getAvailableInterruptId, there is only %s interrupts available" % HARD_INTERRUPTS 
        return None

    def attachInterrupt(self, pin, mode, callback):
        res = None
        if hasattr(self.board, 'attachInterrupt'):
            myid = self.getAvailableInterruptId()
            if not(myid is None) :
                inter = Interrupt(myid, pin, mode, callback)
                self.interrupts[myid] = inter
                res = self.board.attachInterrupt(inter)
        return res

    def detachInterrupt(self, pin):
        res = None
        if hasattr(self.board, 'detachInterrupt'):
            for m in self.interrupts:
                if not(m is None):
                    if (m.pin==pin):
                        #print "pin to be detached ", m.pin
                        res = self.board.detachInterrupt(m)
        return res

    def delay(self, period):
        """Delay expressed in milliseconds. Delay can be evil because is blocking function"""
        time.sleep(period/1000.0)
        
    def proportion(self, value,istart,istop,ostart,ostop) :
        """This is port of Processing map function. It's useful to make proportion calculation"""
        return float(ostart) + (float(ostop) - float(ostart)) * ((float(value) - float(istart)) / (float(istop) - float(istart)))

# This is class that stores all data regarding interrupt events
class Interrupt():
    def __init__(self, myid, pin, mode, callback):
        self.myid = myid
        self.pin = pin
        self.mode = mode
        self.callback = callback

