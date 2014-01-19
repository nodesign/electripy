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
    if (electripyBoard.mainInterrupt != None):
        result = electripyBoard.mainInterrupt(data)
    
    # do some post-init
    
    return result

def inputMode(pin, mode):
    result = None
    if (electripyBoard.inputMode != None):
        result = electripyBoard.inputMode(pin, mode)
    return result
            
def digitalWrite(pin, state):
    res = None
    if (electripyBoard.digitalWrite != None):
        res = electripyBoard.digitalWrite(pin, state)
    return res
    
def digitalRead(pin):
    res = None
    if (electripyBoard.digitalRead != None):
        res = electripyBoard.digitalRead(pin)
    return res
    
def analogRead(pin):
    res = None
    if (electripyBoard.analogRead != None):
        res = electripyBoard.analogRead(pin)
    return res
    
def pwmWrite(pin, value):
    res = None
    if (electripyBoard.pwmWrite != None):
        res = electripyBoard.pwmWrite(pin, value)
    return res

def analogWrite(pin, value):
    """Defining synonime of pwmWrite to match arduino syntax"""
    res = None
    if (electripyBoard.pwmWrite != None):
        res = electripyBoard.pwmWrite(pin, value)

def proportion(value, istart, istop, ostart, ostop):
    res = None
    if (electripyBoard.proportion != None):
        res = electripyBoard.proportion(value, istart, istop, ostart, ostop)
    return res
    
def setPwm0PortPeriod(period):
    res = None
    if (electripyBoard.setPwm0PortPeriod != None):
        res = electripyBoard.setPwm0PortPeriod(period)
    return res

def setPwm1PortPeriod(period):
    res = None
    if (electripyBoard.setPwm1PortPeriod != None):
        res = electripyBoard.setPwm1PortPeriod(period)
    return res

def setPwmPeriod(period):
    res = None
    if (electripyBoard.setPwmPeriod):
        res = electripyBoard.setPwmPeriod(period)
    return res

def setPwm0Limit(limit):
    res = None
    if (electripyBoard.setPwm0Limit != None):
        res = electripyBoard.setPwm0Limit(limit)
    return res

def setPwm1Limit(limit):
    res = None
    if (electripyBoard.setPwm1Limit):
        res = electripyBoard.setPwm1Limit(limit)
    return res

def setPwmLimit(limit):
    res = None
    if (electripyBoard.setPwmLimit):
        res = electripyBoard.setPwmLimit(limit)
    return res

def attachInterrupt(pin, mode, callback):
    res = None
    if (electripyBoard.attachInterrupt != None):
        res = electripyBoard.attachInterrupt(pin, mode, callback)
    return res

def detachInterrupt(pin):
    res = None
    if (electripyBoard.detachInterrupt != None):
        res = electripyBoard.detachInterrupt(pin)
    return res

def getAvailableInterruptId():
    res = None
    if (electripyBoard.getAvailableInterruptId):
        res = electripyBoard.getAvailableInterruptId()
    return res

def delay(period):
    """Delay expressed in milliseconds. Delay will block current process. Delay can be evil"""
    time.sleep(period/1000.0)

