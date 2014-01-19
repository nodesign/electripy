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
    if (board.mainInterrupt != None):
        result = board.mainInterrupt(data)
    
    # do some post-init
    
    return result

def inputMode(pin, mode):
    result = None
    if (board.inputMode != None):
        result = board.inputMode(pin, mode)
    return result
            
def digitalWrite(pin, state):
    res = None
    if (board.digitalWrite != None):
        res = board.digitalWrite(pin, state)
    return res
    
def digitalRead(pin):
    res = None
    if (board.digitalRead != None):
        res = board.digitalRead(pin)
    return res
    
def analogRead(pin):
    res = None
    if (board.analogRead != None):
        res = board.analogRead(pin)
    return res
    
def pwmWrite(pin, value):
    res = None
    if (board.pwmWrite != None):
        res = board.pwmWrite(pin, value)
    return res

def analogWrite(pin, value):
    """Defining synonime of pwmWrite to match arduino syntax"""
    res = None
    if (board.pwmWrite != None):
        res = board.pwmWrite(pin, value)

def proportion(value, istart, istop, ostart, ostop):
    res = None
    if (board.proportion != None):
        res = board.proportion(value, istart, istop, ostart, ostop)
    return res
    
def setPwm0PortPeriod(period):
    res = None
    if (board.setPwm0PortPeriod != None):
        res = board.setPwm0PortPeriod(period)
    return res

def setPwm1PortPeriod(period):
    res = None
    if (board.setPwm1PortPeriod != None):
        res = board.setPwm1PortPeriod(period)
    return res

def setPwmPeriod(period):
    res = None
    if (board.setPwmPeriod):
        res = board.setPwmPeriod(period)
    return res

def setPwm0Limit(limit):
    res = None
    if (board.setPwm0Limit != None):
        res = board.setPwm0Limit(limit)
    return res

def setPwm1Limit(limit):
    res = None
    if (board.setPwm1Limit):
        res = board.setPwm1Limit(limit)
    return res

def setPwmLimit(limit):
    res = None
    if (board.setPwmLimit):
        res = board.setPwmLimit(limit)
    return res

def attachInterrupt(pin, mode, callback):
    res = None
    if (board.attachInterrupt != None):
        res = board.attachInterrupt(pin, mode, callback)
    return res

def detachInterrupt(pin):
    res = None
    if (board.detachInterrupt != None):
        res = board.detachInterrupt(pin)
    return res

def getAvailableInterruptId():
    res = None
    if (board.getAvailableInterruptId):
        res = board.getAvailableInterruptId()
    return res

def delay(period):
    """Delay expressed in milliseconds. Delay will block current process. Delay can be evil"""
    time.sleep(period/1000.0)

