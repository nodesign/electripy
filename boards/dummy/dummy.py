### 
#
# Electripy, HAL library for Python
#
# Library was originally created for WeIO, www.we-io.net
# and than forked as a separate project in order to promote
# concept of using interpreted languages in microcontrolers.
# 
# This library is common effort of their original creators
# Uros PETREVSKI, Drasko DRASKOVIC and 8devices team
#              _           _        _             
#          ___| | ___  ___| |_ _ __(_)_ __  _   _ 
#         / _ \ |/ _ \/ __| __| '__| | '_ \| | | |
#        |  __/ |  __/ (__| |_| |  | | |_) | |_| |
#         \___|_|\___|\___|\__|_|  |_| .__/ \__, |
#                                    |_|    |___/ 
#
#           Hardware Abstraction Layer Library
#                       for Python
#
# This file is part of Electripy
# Electripy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Electripy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors : 
# Uros PETREVSKI <uros@nodesign.net>
# Drasko DRASKOVIC <drasko.draskovic@gmail.com>
#
###

""" Dummy board for testing purposes """
class Board():
    def __init__(self):
        self.name = 'dummy'

    def digitalWrite(self, pin, state):
        print "dummyBoard.digitalWrite(pin, state) has been called with parameters: %d, %d" % (pin, state)
    
    def digitalRead(self, pin):
        print "dummyBoard.digitalRead(pin) has been called with parameter: %d" % pin
    
    def analogRead(self, pin):
        print "dummyBoard.analogRead(pin) has been called with parameter: %d" % pin
