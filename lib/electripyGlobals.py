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

"""
    This module holds all global variable definitions.
    These globals can be imported, used and shared between all the modules of the library
"""

###
# Global Macros
###
HIGH = 1
LOW = 0

###
# Global board
###
from boards.dummy import dummy

board = dummy.DummyBoard()
