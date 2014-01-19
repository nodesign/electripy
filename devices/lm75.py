# LM75B thermometer driver

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

from fcntl import ioctl
import struct
import platform

class WeioLm75:

    # Kernel driver definition
    # SDA GPIO18
    # SCL GPIO19

    def __init__(self):
       
        if (platform.machine() == 'mips') :
                        
            # file path
            filePath = "/dev/i2c-0"

            # from i2c-dev.h
            I2C_SLAVE = 0x0703
            
            # open file
            self.f = open(filePath, "r+")

            # set device address
            ioctl(self.f, I2C_SLAVE, 0x4f)

            # i2c device address
            self.deviceAddress = 0x4f
            # set instruction to get temperature - 0x0 to get temperature
            self.inst = struct.pack('B', 0x0)
        
    def getTemperature(self):
        if (platform.machine() == 'mips') :
            # ask for a temperature
            self.f.write(self.inst)

            # get two bytes as result
            rcv = self.f.read(2)
        
            # do data conversion see LM75B datasheet
            temp  = struct.unpack('B', rcv[0])[0] << 8
            temp |= struct.unpack('B', rcv[1])[0]

            temp >>= 5
            return float(temp)*0.125
        else :
            print "This is fake temperature 25.123, testing purposes"
            return 25.123
