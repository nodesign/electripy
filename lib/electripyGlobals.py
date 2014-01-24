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
    This module holds all global variable definitions.
    These globals can be imported, used and shared between all the modules of the library
"""

###
# Global board
###
from boards.weio import weio
from boards.weio import wirings
#from boards.uper import uper

#board = dummy.Board("/dev/ttyACM0")
targetBoard = weio

#board = uper.Board()

###
# Global Macros
###
HIGH = wirings.HIGH
LOW = wirings.LOW

INPUT_PULLUP = wirings.INPUT_PULLUP
INPUT_PULLDOWN = wirings.INPUT_PULLDOWN 
INPUT_HIGHZ = wirings.INPUT_HIGHZ
INPUT_ADC = wirings.INPUT_ADC
OUTPUT = wirings.OUTPUT
OUTPUT_PWM = wirings.OUTPUT_PWM

# Value is in microseconds
PWM_PERIOD = wirings.PWM_PERIOD
# This is constant of maximum PXM period limit
PWM_PERIOD_LIMIT_CONST = wirings.PWM_PERIOD_LIMIT_CONST
# make sure that this value is always inferior to PWM_PERIOD
PWM_LIMIT = wirings.PWM_LIMIT


# GPIOs, all pins go here
pins = wirings.pins

# ADC pins
adcs = wirings.adcs

# PWM pins
pwms = wirings.pwms

# Interrupt modes
# HIGH and LOW were already declared
# LOW 0 
# HIGH 1
CHANGE = wirings.CHANGE
RISING = wirings.RISING
FALLING = wirings.FALLING

# number of hard interrupts
HARD_INTERRUPTS = wirings.HARD_INTERRUPTS

# String as response from controler
interruptType = wirings.interruptType