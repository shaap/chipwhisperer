#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Colin O'Flynn <coflynn@newae.com>
# All rights reserved.
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

import time
from subprocess import call
from _base import AuxiliaryTemplate


class ResetAVR(AuxiliaryTemplate):
    _name = 'Reset AVR via AVRDUDE'

    def __init__(self):
        AuxiliaryTemplate.__init__(self)
        self.getParams().addChildren([
            {'name':'AVRDUDE Path', 'type':'file', 'key':'avrdudepath', 'value':r'/usr/bin/avrdude'},
            {'name':'AVR Part', 'type':'list', 'key':'part', 'values':['m328p','atxmega16a4'], 'value':'m328p'},
            {'name':'Test Reset', 'type':'action', 'action':self.testReset}
        ])

    def captureInit(self):
        pass

    def captureComplete(self):
        pass

    def traceArm(self):
        avrdude = self.findParam('avrdudepath').getValue()
        ret = call([avrdude, "-p%s" % self.findParam('part').getValue(), "-cavrisp2"])
        if int(ret) != 0:
            raise IOError("Error Calling avrdude.")

#        time.sleep(2)

    def traceDone(self):
        pass

    def testReset(self, _=None):
        self.traceArm()
