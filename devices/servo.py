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

###
# Controling servo motor with PWM signal
# Pulse length is constant of 20ms, variate impulse from 1ms to 2ms
#
#   +---+                +---+
#   |   |                |   |
#   |   |                |   |
#   |   |                |   |
#---+   +----------------+   +------
# -->   <--1 ms = 5%
#   <-------- 20 ms ----> 
#
#
#   +------+            +------+
#   |      |            |      |
#   |      |            |      |
#   |      |            |      |
#---+      +------------+      +------
# -->      <--2 ms = 10%
#   <------- 20 ms ----->
###

###
# Controling servo motor with PWM signal
# Pulse length is constant of 20ms, variate impulse from 1ms to 2ms
#
#   +---+                +---+
#   |   |                |   |
#   |   |                |   |
#   |   |                |   |
#---+   +----------------+   +------
# -->   <--1 ms = 5%
#   <-------- 20 ms ----> 
#
#
#   +------+            +------+
#   |      |            |      |
#   |      |            |      |
#   |      |            |      |
#---+      +------------+      +------
# -->      <--2 ms = 10%
#   <------- 20 ms ----->
###

class Servo:
    
    def __init__(self, myboard):
        # Set 20ms signal length for PWM
        self.board = myboard
        self.board.setPwmPeriod(20000)
        # Set maximum precision for this freq
        self.board.setPwmLimit(19999)
        # Down limit frequency expressed in uS
        self.downLimit = 1000 # 5% of 20000
        self.upLimit = self.downLimit*2 # 10% of 20000
        self.minAngle = 0
        self.maxAngle = 180
        self.angle = None
        self.readuS = None

    def write(self, pin, data):
        # Write to coresponding servo motor
        val = int(self.board.proportion(data, self.minAngle, self.maxAngle, self.downLimit, self.upLimit))
        self.readuS = val
        self.angle = data
        self.board.pwmWrite(pin, self.readuS)
        
    def setMinLimit(self, val):
        self.downLimit = val
        
    def setMaxLimit(self, val):
        self.upLimit = val
    
    def setMinAngle(self, val):
        self.minAngle = val
        
    def setMaxAngle(self, val):
        self.maxAngle = val    
    
    def read(self):
        return self.angle
        
    def readuS(self):
        return self.readuS