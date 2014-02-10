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

class Wirings():
    #################################
    # Pins and Global definitions
    #################################
    HIGH = 1
    LOW = 0

    INPUT_PULLUP = 4
    INPUT_PULLDOWN = 2
    INPUT_HIGHZ = 0
    INPUT_ADC = 5
    OUTPUT = 1
    PWM0_OUTPUT = 6
    PWM1_OUTPUT = 7
    OUTPUT_PWM = 8

    # This is remapping of uper pinouts to WeIO pinouts
    #         UPER  FUNC   WEIO
    PINS = []
    PINS.append(20) #RX     0
    PINS.append(19) #TX     1

    PINS.append(13) #MOSI 0 2
    PINS.append(12) #MISO 0 3
    PINS.append(14) #SCK  0 4

    PINS.append(5)  #MOSI 1 5
    PINS.append(11) #MISO 1 6
    PINS.append(4)  #SCK  1 7

    ## !!!VERIFY i2c not correct!!!
    PINS.append(34)  #SDA    8
    PINS.append(35)  #SCL    9
    ##

    PINS.append(1)  #GPIO   10
    PINS.append(21) #GPIO   11
    PINS.append(0)  #GPIO   12
    PINS.append(18) #GPIO   13
    PINS.append(16) #GPIO   14
    PINS.append(27) #GPIO   15
    PINS.append(6)  #GPIO   16
    PINS.append(3)  #GPIO   17
    PINS.append(9)  #GPIO   18
    PINS.append(29) #PWM 0  19
    PINS.append(28) #PWM 0  20
    PINS.append(22) #PWM 0  21
    PINS.append(7)  #PWM 1  22
    PINS.append(17) #PWM 1  23
    PINS.append(2)  #PWM 1  24
    PINS.append(33) #AD0    25
    PINS.append(32) #AD1    26
    PINS.append(31) #AD2    27
    PINS.append(30) #AD3    28
    PINS.append(26) #AD4    29
    PINS.append(25) #AD5    30
    PINS.append(24) #AD6    31
    PINS.append(23) #AD7    32

    # WeIO adc pins
    ADCS = []
    ADCS.append(25)
    ADCS.append(26)
    ADCS.append(27)
    ADCS.append(28)
    ADCS.append(29)
    ADCS.append(30)
    ADCS.append(31)
    ADCS.append(32)

    # WeIO pwm pins
    PWMS = []
    PWMS.append(19)
    PWMS.append(20)
    PWMS.append(21)
    PWMS.append(22)
    PWMS.append(23)
    PWMS.append(24)

    # Value is in microseconds
    PWM_PERIOD = 1000
    # This is constant of maximum PXM period limit
    PWM_PERIOD_LIMIT_CONST = 65535
    # make sure that this value is always inferior to PWM_PERIOD
    PWM_LIMIT = 255

    # Interrupt modes
    # HIGH and LOW were already declared
    # LOW 0 
    # HIGH 1
    CHANGE = 2
    RISING = 3
    FALLING = 4

    # number of hard interrupts
    HARD_INTERRUPTS = 8

    # interrupt types
    INTERRUPT_TYPE = []
    INTERRUPT_TYPE.append("LOW")
    INTERRUPT_TYPE.append("HIGH")
    INTERRUPT_TYPE.append("CHANGE")
    INTERRUPT_TYPE.append("RISING")
    INTERRUPT_TYPE.append("FALLING")
