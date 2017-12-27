#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ADXL345: Small, thin, ultralow power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Analog Devices Inc."]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	DEVID = 0
	THRESH_TAP = 29
	OFSX = 30
	OFSY = 31
	OFSZ = 32
	DUR = 33
	Latent = 34
	Window = 35
	THRESH_ACT = 36
	THRESH_INACT = 37
	TIME_INACT = 38
	ACT_INACT_CTL = 39
	THRESH_FF = 40
	TIME_FF = 41
	TAP_AXES = 42
	ACT_TAP_STATUS = 43
	BW_RATE = 44
	POWER_CTL = 45
	INT_ENABLE = 46
	INT_MAP = 47
	INT_SOURCE = 48
	DATA_FORMAT = 49
	DATAX = 50
	DATAY = 52
	DATAZ = 54
	FIFO_CTL = 56
	FIFO_STATUS = 57
