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

from ADXL345_constants import *

# name:        ADXL345
# description: Small, thin, ultralow power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g.
# manuf:       Analog Devices Inc.
# version:     0.1
# url:         http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class ADXL345_Base:
	"""Small, thin, ultralow power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g."""
	# Register DEVID
	# Fixed device ID 
	
	def setDEVID(self, val):
		"""Set register DEVID"""
		self.write(REG.DEVID, val, 8)
	
	def getDEVID(self):
		"""Get register DEVID"""
		return self.read(REG.DEVID, 8)
	
	# Bits DEVID
	# Register THRESH_TAP
	# Threshold value for tap interrupts. The data format is unsigned, therefore, the magnitude of the tap event is
	#       compared with the value in THRESH_TAP for normal tap detection. The scale factor is 62.5 mg/LSB
	#       (that is, 0xFF = 16 g). A value of 0 may result in undesirable behavior if single tap/double tap interrupts are
	#       enabled. 
	
	
	def setTHRESH_TAP(self, val):
		"""Set register THRESH_TAP"""
		self.write(REG.THRESH_TAP, val, 8)
	
	def getTHRESH_TAP(self):
		"""Get register THRESH_TAP"""
		return self.read(REG.THRESH_TAP, 8)
	
	# Bits THRESH_TAP
	# Register OFSX
	# The OFSX, OFSY, and OFSZ registers are each eight bits and offer user-set offset adjustments in twos complement
	#       format with a scale factor of 15.6 mg/LSB (that is, 0x7F = 2 g). The value stored in the offset registers is
	#       automatically added to the acceleration data, and the resulting value is stored in the output data registers.
	#       For additional information regarding offset calibration and the use of the offset registers, refer to the
	#       Offset Calibration section. 
	
	
	def setOFSX(self, val):
		"""Set register OFSX"""
		self.write(REG.OFSX, val, 8)
	
	def getOFSX(self):
		"""Get register OFSX"""
		return self.read(REG.OFSX, 8)
	
	# Bits OFSX
	# Register OFSY
	# Y-axis offset 
	
	def setOFSY(self, val):
		"""Set register OFSY"""
		self.write(REG.OFSY, val, 8)
	
	def getOFSY(self):
		"""Get register OFSY"""
		return self.read(REG.OFSY, 8)
	
	# Bits OFSY
	# Register OFSZ
	# Z-axis offset 
	
	def setOFSZ(self, val):
		"""Set register OFSZ"""
		self.write(REG.OFSZ, val, 8)
	
	def getOFSZ(self):
		"""Get register OFSZ"""
		return self.read(REG.OFSZ, 8)
	
	# Bits OFSZ
	# Register DUR
	# Tap duration: Unsigned time value representing the maximum time that an event must be above the THRESH_TAP threshold to
	#       qualify as a tap event. The scale factor is 625 μs/LSB. A value of 0 disables the single tap/ double tap functions. 
	
	
	def setDUR(self, val):
		"""Set register DUR"""
		self.write(REG.DUR, val, 8)
	
	def getDUR(self):
		"""Get register DUR"""
		return self.read(REG.DUR, 8)
	
	# Bits DUR
	# Register Latent
	# Tap latency: Unsigned time value representing the wait time from the detection of a tap event to the start of the time window (defined by the window register) during which a possible second tap event can be detected. The scale factor is 1.25 ms/LSB. A value of 0 disables the double tap function. 
	
	def setLatent(self, val):
		"""Set register Latent"""
		self.write(REG.Latent, val, 8)
	
	def getLatent(self):
		"""Get register Latent"""
		return self.read(REG.Latent, 8)
	
	# Bits Latent
	# Register Window
	# Tap window: Unsigned time value representing the amount of time after the expiration of the latency time (determined by the latent register) during which a second valid tap can begin. The scale factor is 1.25 ms/LSB. A value of 0 disables the double tap function. 
	
	def setWindow(self, val):
		"""Set register Window"""
		self.write(REG.Window, val, 8)
	
	def getWindow(self):
		"""Get register Window"""
		return self.read(REG.Window, 8)
	
	# Bits Window
	# Register THRESH_ACT
	# Threshold value for detecting activity. The data format is unsigned, so the magnitude of the activity event is compared with the value in the THRESH_ACT register. The scale factor is 62.5 mg/LSB. A value of 0 may result in undesirable behavior if the activity interrupt is enabled. 
	
	def setTHRESH_ACT(self, val):
		"""Set register THRESH_ACT"""
		self.write(REG.THRESH_ACT, val, 8)
	
	def getTHRESH_ACT(self):
		"""Get register THRESH_ACT"""
		return self.read(REG.THRESH_ACT, 8)
	
	# Bits THRESH_ACT
	# Register THRESH_INACT
	# Inactivity threshold: threshold value for detecting inactivity. The data format is unsigned, so the magnitude of the inactivity event is compared with the value in the THRESH_INACT register. The scale factor is 62.5 mg/LSB. A value of 0 may result in undesirable behavior if the inactivity interrupt is enabled. 
	
	def setTHRESH_INACT(self, val):
		"""Set register THRESH_INACT"""
		self.write(REG.THRESH_INACT, val, 8)
	
	def getTHRESH_INACT(self):
		"""Get register THRESH_INACT"""
		return self.read(REG.THRESH_INACT, 8)
	
	# Bits THRESH_INACT
	# Register TIME_INACT
	# Inactivity time: unsigned time value representing the amount of time that acceleration must be less than the value in the THRESH_INACT register for inactivity to be declared. The scale factor is 1 sec/LSB. Unlike the other interrupt functions, which use unfiltered data (see the Threshold section), the inactivity function uses filtered output data. At least one output sample must be generated for the inactivity interrupt to be triggered. This results in the function appearing unresponsive if the TIME_INACT register is set to a value less than the time constant of the output data rate. A value of 0 results in an interrupt when the output data is less than the value in the THRESH_INACT register. 
	
	def setTIME_INACT(self, val):
		"""Set register TIME_INACT"""
		self.write(REG.TIME_INACT, val, 8)
	
	def getTIME_INACT(self):
		"""Get register TIME_INACT"""
		return self.read(REG.TIME_INACT, 8)
	
	# Bits TIME_INACT
	# Register ACT_INACT_CTL
	# Axis enable control for activity and inactivity detection 
	
	def setACT_INACT_CTL(self, val):
		"""Set register ACT_INACT_CTL"""
		self.write(REG.ACT_INACT_CTL, val, 8)
	
	def getACT_INACT_CTL(self):
		"""Get register ACT_INACT_CTL"""
		return self.read(REG.ACT_INACT_CTL, 8)
	
	# Bits ACT
	# Bits ACT_X
	# Enable axis participation in detecting activity or inactivity.
	#           If all axes are excluded, the function is disabled. For activity detection, all participating axes are logically OR'ed, causing the activity function to trigger when any of the partici- pating axes exceeds the threshold. For inactivity detection, all participating axes are logically AND'ed, causing the inactivity function to trigger only if all participating axes are below the threshold for the specified time. 
	
	# Bits ACT_Y
	# Enable axis participation in detecting activity or inactivity. 
	# Bits ACT_Z
	# Enable axis participation in detecting activity or inactivity. 
	# Bits INACT
	# Bits INACT_X
	# Bits INACT_Y
	# Bits INACT_Z
	# Register THRESH_FF
	# Free-fall threshold: threshold value, in unsigned format, for free-fall detection. The acceleration on all axes is compared with the value in THRESH_FF to determine if a free-fall event occurred. The scale factor is 62.5 mg/LSB. Note that a value of 0 mg may result in undesirable behavior if the free- fall interrupt is enabled. Values between 300 mg and 600 mg (0x05 to 0x09) are recommended.threshold value, in unsigned format, for free-fall detection. The acceleration on all axes is compared with the value in THRESH_FF to determine if a free-fall event occurred. The scale factor is 62.5 mg/LSB. Note that a value of 0 mg may result in undesirable behavior if the free- fall interrupt is enabled. Values between 300 mg and 600 mg (0x05 to 0x09) are recommended. 
	
	def setTHRESH_FF(self, val):
		"""Set register THRESH_FF"""
		self.write(REG.THRESH_FF, val, 8)
	
	def getTHRESH_FF(self):
		"""Get register THRESH_FF"""
		return self.read(REG.THRESH_FF, 8)
	
	# Bits THRESH_FF
	# Register TIME_FF
	# Free-fall time: unsigned time value representing the minimum time that the value of all axes must be less than THRESH_FF to generate a free-fall interrupt. The scale factor is 5 ms/LSB. A value of 0 may result in undesirable behavior if the free-fall interrupt is enabled. Values between 100 ms and 350 ms (0x14 to 0x46) are recommended. 
	
	def setTIME_FF(self, val):
		"""Set register TIME_FF"""
		self.write(REG.TIME_FF, val, 8)
	
	def getTIME_FF(self):
		"""Get register TIME_FF"""
		return self.read(REG.TIME_FF, 8)
	
	# Bits TIME_FF
	# Register TAP_AXES
	# Axis control for single tap/double tap 
	
	def setTAP_AXES(self, val):
		"""Set register TAP_AXES"""
		self.write(REG.TAP_AXES, val, 8)
	
	def getTAP_AXES(self):
		"""Get register TAP_AXES"""
		return self.read(REG.TAP_AXES, 8)
	
	# Bits TAP_AXES
	# Register ACT_TAP_STATUS
	# Source of single tap/double tap 
	
	def setACT_TAP_STATUS(self, val):
		"""Set register ACT_TAP_STATUS"""
		self.write(REG.ACT_TAP_STATUS, val, 8)
	
	def getACT_TAP_STATUS(self):
		"""Get register ACT_TAP_STATUS"""
		return self.read(REG.ACT_TAP_STATUS, 8)
	
	# Bits unused_0
	# Bits Suppress
	# Setting the suppress bit suppresses double tap detection if acceleration greater than the value in THRESH_TAP
	#           is present between taps. See the Tap Detection section for more details. 
	
	# Bits TAP_X
	# Enable x-axis participation in tap detection. A setting of 0 excludes the selected axis from participation in tap detection.
	# Bits TAP_Y
	# Dto. for y-axis
	# Bits TAP_Z
	# Dto. for z-axis
	# Register BW_RATE
	# Data rate and power mode control:
	#       The ACT_X/Y/Z TAP_X/Y/Z bits indicate the first axis involved in a tap or activity event.
	#       When new data is available, these bits are not cleared but are overwritten by the new data. The ACT_TAP_STATUS
	#       register should be read before clearing the interrupt. Disabling an axis from participation clears the
	#       corresponding source bit when the next activity or single tap/double tap event occurs. 
	
	
	def setBW_RATE(self, val):
		"""Set register BW_RATE"""
		self.write(REG.BW_RATE, val, 8)
	
	def getBW_RATE(self):
		"""Get register BW_RATE"""
		return self.read(REG.BW_RATE, 8)
	
	# Bits unused_0
	# Bits ACT_X
	# A setting of 1 corresponds to involvement in the event
	# Bits ACT_Y
	# Bits ACT_Z
	# Bits Asleep
	# Indicates that the part is asleep, and a setting of 0 indicates that the part is not asleep. This bit toggles only if the device is configured for auto sleep. See the AUTO_SLEEP Bit section for more information on autosleep mode.
	# Bits TAP_X
	# Bits TAP_Y
	# Bits TAP_Z
	# Register POWER_CTL
	# Power-saving features control 
	
	def setPOWER_CTL(self, val):
		"""Set register POWER_CTL"""
		self.write(REG.POWER_CTL, val, 8)
	
	def getPOWER_CTL(self):
		"""Get register POWER_CTL"""
		return self.read(REG.POWER_CTL, 8)
	
	# Bits reserved_0
	# Bits LINK
	# A 1 with both the activity and inactivity functions enabled delays the start of the activity function until inactivity is detected. After activity is detected, inactivity detection begins, preventing the detection of activity. This bit serially links the activity and inactivity functions. When this bit is set to 0, the inactivity and activity functions are concurrent. Additional information can be found in the Link Mode section.
	#           When clearing the link bit, it is recommended that the part be placed into standby mode and then set back to measurement mode with a subsequent write. This is done to ensure that the device is properly biased if sleep mode is manually disabled; otherwise, the first few samples of data after the link bit is cleared may have additional noise, especially if the device was asleep when the bit was cleared. 
	
	# Bits AUTO_SLEEP
	# If the link bit is set, a setting of 1 in the AUTO_SLEEP bit enables the auto-sleep functionality. In this mode, the ADXL345 auto- matically switches to sleep mode if the inactivity function is enabled and inactivity is detected (that is, when acceleration is below the THRESH_INACT value for at least the time indicated by TIME_INACT). If activity is also enabled, the ADXL345 automatically wakes up from sleep after detecting activity and returns to operation at the output data rate set in the BW_RATE register. A setting of 0 in the AUTO_SLEEP bit disables automatic switching to sleep mode. See the description of the Sleep Bit in this section for more information on sleep mode.
	#           If the link bit is not set, the AUTO_SLEEP feature is disabled and setting the AUTO_SLEEP bit does not have an impact on device operation. Refer to the Link Bit section or the Link Mode section for more information on utilization of the link feature.<br>
	#           When clearing the AUTO_SLEEP bit, it is recommended that the part be placed into standby mode and then set back to measure- ment mode with a subsequent write. This is done to ensure that the device is properly biased if sleep mode is manually disabled; otherwise, the first few samples of data after the AUTO_SLEEP bit is cleared may have additional noise, especially if the device was asleep when the bit was cleared. 
	
	# Bits Measure
	# The ADXL345 powers up in standby mode with minimum power consumption. 
	# Bits Sleep
	# Sleep mode suppresses DATA_READY, stops transmission of data to FIFO, and switches the sampling rate to one specified by the wakeup bits. In sleep mode, only the activity function can be used. When the DATA_READY interrupt is suppressed, the output data registers (Register 0x32 to Register 0x37) are still updated at the sampling rate set by the wakeup bits (D1:D0).<br>
	#           When clearing the sleep bit, it is recommended that the part be placed into standby mode and then set back to measurement mode with a subsequent write. This is done to ensure that the device is properly biased if sleep mode is manually disabled; otherwise, the first few samples of data after the sleep bit is cleared may have additional noise, especially if the device was asleep when the bit was cleared. 
	
	# Bits Wakeup
	# control the frequency of readings in sleep mode 
	# Register INT_ENABLE
	# Interrupt enable control: A value of 1 enables their respective functions to generate interrupts, whereas
	#       a value of 0 prevents the functions from generating interrupts. The functions are always enabled. It is
	#       recommended that interrupts be configured before enabling their outputs. 
	
	
	def setINT_ENABLE(self, val):
		"""Set register INT_ENABLE"""
		self.write(REG.INT_ENABLE, val, 8)
	
	def getINT_ENABLE(self):
		"""Get register INT_ENABLE"""
		return self.read(REG.INT_ENABLE, 8)
	
	# Bits DATA_READY
	# enables only the interrupt output
	# Bits SINGLE_TAP
	# Bits DOUBLE_TAP
	# Bits Activity
	# Bits Inactivity
	# Bits FREE_FALL
	# Bits Watermark
	# enables only the interrupt output
	# Bits Overrun
	# enables only the interrupt output
	# Register INT_MAP
	# Interrupt mapping control: Any bits set to 0 in this register send their respective interrupts to the INT1 pin,
	#       whereas bits set to 1 send their respective interrupts to the INT2 pin. All selected interrupts for a given pin are OR'ed. 
	
	
	def setINT_MAP(self, val):
		"""Set register INT_MAP"""
		self.write(REG.INT_MAP, val, 8)
	
	def getINT_MAP(self):
		"""Get register INT_MAP"""
		return self.read(REG.INT_MAP, 8)
	
	# Bits DATA_READY
	# Bits SINGLE_TAP
	# Bits DOUBLE_TAP
	# Bits Activity
	# Bits Inactivity
	# Bits FREE_FALL
	# Bits Watermark
	# Bits Overrun
	# Register INT_SOURCE
	# Source of interrupts: Bits set to 1 in this register indicate that their respective functions have triggered an
	#       event, whereas a value of 0 indicates that the corresponding event has not occurred. 
	
	
	def setINT_SOURCE(self, val):
		"""Set register INT_SOURCE"""
		self.write(REG.INT_SOURCE, val, 8)
	
	def getINT_SOURCE(self):
		"""Get register INT_SOURCE"""
		return self.read(REG.INT_SOURCE, 8)
	
	# Bits DATA_READY
	# may require multiple reads, as indicated in the FIFO mode descriptions; <br>always set if the corresponding events occur, regardless of the INT_ENABLE register settings, and are cleared by reading data from the DATAX, DATAY, and DATAZ registers
	# Bits SINGLE_TAP
	# Bits DOUBLE_TAP
	# Bits Activity
	# Bits Inactivity
	# Bits FREE_FALL
	# Bits Watermark
	# may require multiple reads, as indicated in the FIFO mode descriptions; <br>always set if the corresponding events occur, regardless of the INT_ENABLE register settings, and are cleared by reading data from the DATAX, DATAY, and DATAZ registers
	# Bits Overrun
	# always set if the corresponding events occur, regardless of the INT_ENABLE register settings, and are cleared by reading data from the DATAX, DATAY, and DATAZ registers
	# Register DATA_FORMAT
	# Control the presentation of data to Register 0x32 through Register 0x37. All data, except that for the +/-16 g range,
	#       must be clipped to avoid rollover. 
	
	
	def setDATA_FORMAT(self, val):
		"""Set register DATA_FORMAT"""
		self.write(REG.DATA_FORMAT, val, 8)
	
	def getDATA_FORMAT(self):
		"""Get register DATA_FORMAT"""
		return self.read(REG.DATA_FORMAT, 8)
	
	# Bits SELF_TEST
	# 1 in the SELF_TEST bit applies a self-test force to the sensor,
	#           causing a shift in the output data. A value of 0 disables the self-test force. 
	
	# Bits SPI
	# 1 in the SPI bit sets the device to 3-wire SPI mode, and a value of 0 sets the device to 4-wire SPI mode.
	# Bits INT_INVERT
	# 0 in the INT_INVERT bit sets the interrupts to active high, and a value of 1 sets the interrupts to active low.
	# Bits reserved_0
	# Bits FULL_RES
	# 1, the device is in full resolution mode, where the output resolution increases with the g range set by the range bits to maintain a 4 mg/LSB scale factor. When the FULL_RES bit is set to 0, the device is in 10-bit mode, and the range bits determine the maximum g range and scale factor.
	# Bits Justify
	# A setting of 1 in the justify bit selects left-justified (MSB) mode, and a setting of 0 selects right-justified mode with sign extension.
	# Bits Range
	# set the g range 
	# Register DATAX
	# X-Axis output data is twos complement,
	#       The DATA_FORMAT register controls the format of the data. It is recommended that a multiple-byte read of all
	#       registers be performed to prevent a change in data between reads of sequential registers. 
	
	
	def setDATAX(self, val):
		"""Set register DATAX"""
		self.write(REG.DATAX, val, 16)
	
	def getDATAX(self):
		"""Get register DATAX"""
		return self.read(REG.DATAX, 16)
	
	# Bits DATAX
	# Register DATAY
	# Y-Axis output data is twos complement,
	#       The DATA_FORMAT register controls the format of the data. It is recommended that a multiple-byte read of all
	#       registers be performed to prevent a change in data between reads of sequential registers. 
	
	
	def setDATAY(self, val):
		"""Set register DATAY"""
		self.write(REG.DATAY, val, 16)
	
	def getDATAY(self):
		"""Get register DATAY"""
		return self.read(REG.DATAY, 16)
	
	# Bits DATAY
	# Register DATAZ
	# Z-Axis output data is twos complement,
	#       The DATA_FORMAT register controls the format of the data. It is recommended that a multiple-byte read of all
	#       registers be performed to prevent a change in data between reads of sequential registers. 
	
	
	def setDATAZ(self, val):
		"""Set register DATAZ"""
		self.write(REG.DATAZ, val, 16)
	
	def getDATAZ(self):
		"""Get register DATAZ"""
		return self.read(REG.DATAZ, 16)
	
	# Bits DATAZ
	# Register FIFO_CTL
	# FIFO control 
	
	def setFIFO_CTL(self, val):
		"""Set register FIFO_CTL"""
		self.write(REG.FIFO_CTL, val, 8)
	
	def getFIFO_CTL(self):
		"""Get register FIFO_CTL"""
		return self.read(REG.FIFO_CTL, 8)
	
	# Bits FIFO_MODE
	# Bits Trigger
	# Bits Samples
	# The function of these bits depends on the FIFO mode selected (see Table 23). Entering a value of 0 in the samples bits immediately sets the watermark status bit in the INT_SOURCE register, regardless of which FIFO mode is selected. Undesirable operation may occur if a value of 0 is used for the samples bits when trigger mode is used. 
	# Register FIFO_STATUS
	# FIFO status 
	
	def setFIFO_STATUS(self, val):
		"""Set register FIFO_STATUS"""
		self.write(REG.FIFO_STATUS, val, 8)
	
	def getFIFO_STATUS(self):
		"""Get register FIFO_STATUS"""
		return self.read(REG.FIFO_STATUS, 8)
	
	# Bits FIFO_TRIG
	# A 1 corresponds to a trigger event occurring, and a 0 means that a FIFO trigger event has not occurred.
	# Bits unused_0
	# Bits Entries
	# How many data values are stored in FIFO. Access to collect the data from FIFO is provided through the DATAX, DATAY, and DATAZ registers. FIFO reads must be done in burst or multiple-byte mode because each FIFO level is cleared after any read (single- or multiple-byte) of FIFO. FIFO stores a maximum of 32 entries, which equates to a maximum of 33 entries available at any given time because an additional entry is available at the output filter of the device.
