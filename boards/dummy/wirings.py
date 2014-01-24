#################################
# WeIO Pin and Global definitions
#################################
HIGH = 1
LOW = 0

INPUT_PULLUP = 4
INPUT_PULLDOWN = 2
INPUT_HIGHZ = 0
ADC_INPUT = 5
OUTPUT = 1
PWM0_OUTPUT = 6
PWM1_OUTPUT = 7
PWM_OUTPUT = 8

# This is remapping of uper pinouts to WeIO pinouts
#         UPER  FUNC   WEIO
pins = []
pins.append(20) #RX     0
pins.append(19) #TX     1

pins.append(13) #MOSI 0 2
pins.append(12) #MISO 0 3
pins.append(14) #SCK  0 4

pins.append(5)  #MOSI 1 5
pins.append(11) #MISO 1 6
pins.append(4)  #SCK  1 7

## !!!VERIFY i2c not correct!!!
pins.append(34)  #SDA    8
pins.append(35)  #SCL    9
##

pins.append(1)  #GPIO   10
pins.append(21) #GPIO   11
pins.append(0)  #GPIO   12
pins.append(18) #GPIO   13
pins.append(16) #GPIO   14
pins.append(27) #GPIO   15
pins.append(6)  #GPIO   16
pins.append(3)  #GPIO   17
pins.append(9)  #GPIO   18
pins.append(29) #PWM 0  19
pins.append(28) #PWM 0  20
pins.append(22) #PWM 0  21
pins.append(7)  #PWM 1  22
pins.append(17) #PWM 1  23
pins.append(2)  #PWM 1  24
pins.append(33) #AD0    25
pins.append(32) #AD1    26
pins.append(31) #AD2    27
pins.append(30) #AD3    28
pins.append(26) #AD4    29
pins.append(25) #AD5    30
pins.append(24) #AD6    31
pins.append(23) #AD7    32

# WeIO adc pins
adcs = []
adcs.append(25)
adcs.append(26)
adcs.append(27)
adcs.append(28)
adcs.append(29)
adcs.append(30)
adcs.append(31)
adcs.append(32)

# WeIO pwm pins
pwms = []
pwms.append(19)
pwms.append(20)
pwms.append(21)
pwms.append(22)
pwms.append(23)
pwms.append(24)

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
interruptType = []
interruptType.append("LOW")
interruptType.append("HIGH")
interruptType.append("CHANGE")
interruptType.append("RISING")
interruptType.append("FALLING")