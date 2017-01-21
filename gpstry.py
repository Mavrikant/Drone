#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0)

params = urllib.urlencode({'key': 'KI5JPZ91PRQUBKN7'})
ser.flushInput()
while 1:
    time.sleep(1)
    try:
        x=ser.readline()
        print x
    except:
        y=x
