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

def mainInterrupt(data):
    """ Do following stuff:
    1) mainInterrupt pre-call generic stuff (generic stuff before calling board's driver IO)
    2) call board driver's IO function (custom for every board)
    3) mainInterrupt post-call generic stuff
    """
    result = None
    
    # do some pre-init

    # Check if the board implements this function
    if hasattr(board, 'mainInterrupt'):
        result = board.mainInterrupt(data)
    else:
        print "electripyError: Board %s has no function mainInterrupt()" % board.name
    
    # do some post-init
    
    return result

def inputMode(pin, mode):
    result = None
    if hasattr(board, 'inputMode'):
        result = board.inputMode(pin, mode)
    return result
            
def digitalWrite(pin, state):
    res = None
    if hasattr(board, 'digitalWrite'):
        res = board.digitalWrite(pin, state)
    return res
    
def digitalRead(pin):
    res = None
    if hasattr(board, 'digitalRead'):
        res = board.digitalRead(pin)
    return res
    
def analogRead(pin):
    res = None
    if hasattr(board, 'analogRead'):
        res = board.analogRead(pin)
    return res
    
def pwmWrite(pin, value):
    res = None
    if hasattr(board, 'pwmWrite'):
        res = board.pwmWrite(pin, value)
    else:
        print "electripyError: Board %s has no function pwmWrite()" % board.name
    return res

def analogWrite(pin, value):
    """Defining synonime of pwmWrite to match arduino syntax"""
    res = None
    if hasattr(board, 'pwmWrite'):
        res = board.pwmWrite(pin, value)

def proportion(value, istart, istop, ostart, ostop):
    res = None
    if hasattr(board, 'proportion'):
        res = board.proportion(value, istart, istop, ostart, ostop)
    return res
    
def setPwm0PortPeriod(period):
    res = None
    if hasattr(board, 'setPwm0PortPeriod'):
        res = board.setPwm0PortPeriod(period)
    return res

def setPwm1PortPeriod(period):
    res = None
    if hasattr(board, 'setPwm1PortPeriod'):
        res = board.setPwm1PortPeriod(period)
    return res

def setPwmPeriod(period):
    res = None
    if hasattr(board, 'setPwmPeriod'):
        res = board.setPwmPeriod(period)
    return res

def setPwm0Limit(limit):
    res = None
    if hasattr(board, 'setPwm0Limit'):
        res = board.setPwm0Limit(limit)
    return res

def setPwm1Limit(limit):
    res = None
    if hasattr(board, 'setPwm1Limit'):
        res = board.setPwm1Limit(limit)
    return res

def setPwmLimit(limit):
    res = None
    if hasattr(board, 'setPwmLimit'):
        res = board.setPwmLimit(limit)
    return res

def attachInterrupt(pin, mode, callback):
    res = None
    if hasattr(board, 'attachInterrupt'):
        res = board.attachInterrupt(pin, mode, callback)
    return res

def detachInterrupt(pin):
    res = None
    if hasattr(board, 'detachInterrupt'):
        res = board.detachInterrupt(pin)
    return res

def getAvailableInterruptId():
    res = None
    if hasattr(board, 'getAvailableInterruptId'):
        res = board.getAvailableInterruptId()
    return res

def delay(period):
    """Delay expressed in milliseconds. Delay will block current process. Delay can be evil"""
    time.sleep(period/1000.0)

