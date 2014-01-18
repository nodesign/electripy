#!/usr/bin/env python
# encoding: utf-8

__version__ = "0.02"

import struct, serial, threading, Queue, time, types, os, glob, urllib, urllib2

class Readers:
    def __init__(self, serial, outq, callback, decodefun):
        self.serial = serial
        self.outq = outq
        self.callback = callback
        self.alive = True
        # self.thread_read = threading.Thread(target=self.reader)
        #         self.thread_read.setDaemon(1)
        #         self.thread_read.start()
        #         self.decodefun = decodefun
        
    def reader(self):
        while self.alive:
            try:
                data = self.serial.read(1)            #read one, blocking
                n = self.serial.inWaiting()            #look if there is more
                if n:
                    data = data + self.serial.read(n)    #and get as much as possible
                if data:
                    if data[3] == '\x09':
                        interrupt = self.decodefun(data)
                        self.callback(interrupt)
                    else:
                        #print ":".join("{:02x}".format(ord(c)) for c in data)
                        self.outq.put(data)
            except RuntimeError:
                print "UPER API: serial port reading error!!!"
                break
        self.alive = False
    
    def stop(self):
        if self.alive:
            self.alive = False
            self.thread_read.join()

class UPER:       
    def stop(self):
        for i in range(7):
            self.detachInterrupt(i)
        self.reader.stop()
        self.ser.close()

    def encodeINT(self, intarg):
        if intarg < 64:
            return(chr(intarg))
        packedint = struct.pack( '>I', intarg ).lstrip('\x00')
        return(chr(0xc0 | (len(packedint) -1)) + packedint)

    def encodeBYTES(self, bytestr):
        if len( bytestr ) < 64:
            return (chr(0x40 | len(packedint)) + bytestr)
        packedlen = struct.pack( '>I', len(bytestr)).lstrip('\x00')
        if len(packedlen) == 1:
            return('\xc4'+packedlen+bytestr)
        elif len(pakedlen) == 2:
            return('\xc5' + packedlen + bytestr)
        else:
            print "UPER API: error - too long string"

    def encodeSFP(self, command, args):
        functions = { types.StringType : self.encodeBYTES, types.IntType : self.encodeINT }
        SFPcommand = chr(command) + ''.join(functions[ type(arg) ]( arg ) for arg in args)
        SFPcommand = '\xd4' + struct.pack('>H', len(SFPcommand)) + SFPcommand
        return(SFPcommand)

    def decodeSFP(self, buffer):
        result = []
        if buffer[0:1] != '\xd4':
            return( result )
        buflen = struct.unpack('>H', buffer[1:3])[0] + 3
        result.append( struct.unpack('b', buffer[3:4])[0] )
        pointer = 4
        args = []
        while pointer < buflen:
            argtype = ord(buffer[pointer:pointer+1])
            pointer +=1
            if argtype < 64:                    #short int
                args.append(argtype)
            elif argtype < 128:                    #short str
                arglen = argtype & 0x3f
                args.append(buffer[pointer:pointer+arglen])
                pointer += arglen
            else:
                arglen = argtype & 0x0f            #decoding integers
                if arglen == 0:
                    args.append(ord(buffer[pointer:pointer+1]))
                elif arglen == 1:
                    args.append(struct.unpack('>H', buffer[pointer:pointer+2])[0])
                elif arglen == 2:
                    args.append(struct.unpack('>I', '\x00' + buffer[pointer:pointer+3])[0])
                elif arglen == 3:
                    args.append(struct.unpack('>I', buffer[pointer:pointer+4])[0])
                pointer += arglen + 1

                if arglen == 4:
                    arglen = ord(buffer[pointer:pointer+1])
                    pointer += 1
                    args.append(buffer[pointer:pointer+arglen])
                    pointer += arglen
                elif arglen == 5:
                    arglen = struct.unpack('>H', buffer[pointer:pointer+2])[0]
                    pointer += 2
                    args.append(buffer[pointer:pointer+arglen])
                    pointer += arglen
        result.append(args)
        return(result)

    def UPER_IO(self, ret, buf):
        self.ser.write(buf)
        if ret == 0:
            return
        data = self.outq.get()
        return(data)

    def setPrimary(self, pinID):
        print "setPrimary", pinID 

    def setSecondary(self, pinID):
        print "setSecondary", pinID 

    def pinMode(self, pinID, pinMode):
        print "pinMode", pinID, " ", pinMode

    def digitalWrite(self, pinID, value):
        print "digitalWrite", pinID, " ", value

    def digitalRead(self, pinID):
        print "digitalRead", pinID

    def attachInterrupt(self, interruptID, pinID, mode):
        print "attachInterrupt", interruptID, " ", pinID, " ", mode
        
    def detachInterrupt(self, interruptID):
        print "detachInterrupt", interruptID
        
    def analogRead(self, analogPinID):
        print "analogRead", analogPinID
        
    def pwm0_begin(self, period):
        #print "pwm0_begin period:", period
        print "pwm0_begin", period
        
    def pwm1_begin(self, period):
        #print "pwm1_begin period:", period
        print "pwm1_begin", period
        
    def pwm0_set(self, channel, high_time):
        #print "pwm0_set high_time:", high_time
        print "pwm0_set", channel, " ", high_time
        
    def pwm1_set(self, channel, high_time):
        #print "pwm1_set high_time:", high_time
        print "pwm1_set", channel, " ", high_time
        
    def pwm0_end(self):
        print "pwm0_end"
        
    def pwm1_end(self):
        print "pwm1_end"
        
    def spi0_begin(self, divider, mode):
        print "spi0_begin"
        
    def spi0_trans(self, data, respond):
        print "spi0_trans"
        
    def spi0_end(self):
        self.UPER_IO(0, self.encodeSFP( 22, []))
         
    def i2c_begin(self):
        self.UPER_IO(0, self.encodeSFP(40, []))

    def i2c_trans(self, address, writeData, readLength):
        return(self.decodeSFP(self.UPER_IO(1, self.encodeSFP(41, [address, writeData, readLength]))))

    def i2c_end(self):
        self.UPER_IO(0, self.encodeSFP( 42, []))

    def registerWrite(self, registerAddress, value):
        self.UPER_IO(0, self.encodeSFP(100, [registerAddress, value]))

    def registerRead(self, registerAddress):
        return(self.decodeSFP(self.UPER_IO(1, self.encodeSFP(101, [registerAddress])))[1][1])

    def getDeviceInfo(self):
        device_info = "device info asked"
        return(device_info)

    def internalCallBack(intdata):
        print"default CallBack is working %r" % intdata
        return

    def __init__(self, callbackfun = internalCallBack, serial_port = "/dev/ttyACM0"):
                # 
                # self.ser = serial.Serial(
                # port=serial_port,
                # baudrate=1, #virtual com port on USB is always max speed
                # parity=serial.PARITY_ODD,
                # stopbits=serial.STOPBITS_ONE,
                # bytesize=serial.EIGHTBITS,
                # timeout = 0.1
                # )
                # self.ser.flushInput()
        print "Uper initialized"
        self.outq = Queue.Queue()
        self.callbackfun = callbackfun
        self.reader = Readers(None, self.outq, self.callbackfun, self.decodeSFP)

if __name__ == '__main__':
    """
    print " Will init UPER1 and read ADC, upgrade firmware and read device info."
    u = UPER()
    u.setSecondary(30)
    print "analogRead = %x" % u.analogRead(3)
    u.stop()
    """
    
    """
    uu = UPER()
    dev_info = uu.getDeviceInfo()
    print "%r" % dev_info
    uu.stop()
    """

