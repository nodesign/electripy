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

"""
    A BIG FAT WARNING:
    electripy.py is kind of synthetic sugar, a wrapper around electripyIO.py class.

    This allows us to use:
    form electripy import *
    construct in user programs, which in effect allows using simple methods
    like digitalWrite() in these user programs directly, since they become global functions.

    However, "import *" is dangerous in many ways, so use it with conscious!

    Note well in the documentation to your users that all the varaibles and functions
    listed here become globals in their programs, so take a reserved namespace.
    Addressing these globals from user functions must be pre-declared with 'global' keyword.
    Otherwise user will address/create local object thinking that he/she modifies global variable from the library.

    As a bootom line:
    1) all keywords below are reserved and not to be used as local variable names in user programs
    2) they are exposed as globals in user program
    3) when modifying them from user program function user 'global' keyword to notify Python that you want to modify
        global variable. For example:
        function f():
            global HIGH
            HIGH = 30
"""

from lib.electripyIO import ElectripyIO

###
# User GLOBALS
###

# Define board here
epyIO = ElectripyIO("boards.weio.board")

HIGH = epyIO.wirings.HIGH
LOW = epyIO.wirings.LOW

INPUT_PULLUP = epyIO.wirings.INPUT_PULLUP
INPUT_PULLDOWN = epyIO.wirings.INPUT_PULLDOWN
INPUT_HIGHZ = epyIO.wirings.INPUT_HIGHZ
INPUT_ADC = epyIO.wirings.INPUT_ADC
OUTPUT = epyIO.wirings.OUTPUT
OUTPUT_PWM = epyIO.wirings.OUTPUT_PWM

# Interrupt modes
# HIGH and LOW were already declared
# LOW 0 
# HIGH 1
CHANGE = epyIO.wirings.CHANGE
RISING = epyIO.wirings.RISING
FALLING = epyIO.wirings.FALLING

INTERRUPT_TYPE = epyIO.wirings.INTERRUPT_TYPE

###
# User API functions for GPIO
###

def getBoardName():
    return epyIO.getBoardName()
    
def getBoard():
    return epyIO

def pinMode(pin, mode):
    return epyIO.pinMode(pin,mode)
        
def digitalWrite(pin, state):
    return epyIO.digitalWrite(pin, state)

def digitalRead(pin):
    return epyIO.digitalRead(pin)

def analogRead(pin):
    return epyIO.analogRead(pin)

def pwmWrite(pin, value):
    return epyIO.pwmWrite(pin,value)

def analogWrite(pin, value):
    """Defining synonime of pwmWrite to match arduino syntax"""
    return epyIO.pwmWrite(pin,value)
    
def setPwmPeriod(period):
    return epyIO.setPwmPeriod(period)
    
def setPwmLimit(limit):
    print "SETTING LIM1", limit
    return epyIO.setPwmLimit(limit)

def setPwmPeriod(period):
    return epyIO.setPwmPeriod(period)

def attachInterrupt(pin, mode, callback):
    return epyIO.attachInterrupt(pin, mode, callback)
    
def detachInterrupt(pin):
    return epyIO.detachInterrupt(pin)
    
def delay(period):
    return epyIO.delay(period)
    
def proportion(value,istart,istop,ostart,ostop) :
    return epyIO.proportion(value,istart,istop,ostart,ostop)
    
def stop(): 
    return epyIO.stop()
