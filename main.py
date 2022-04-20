import usb_hid
import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


class FootController: 

	def __init__(self):
		self.keyboard = Keyboard(usb_hid.device)
    	self.appSwitcherMode = False 
		self.whiteButtonPressed = False
		self.yellowButtonPressed = False 
		self.blueButtonPressed = False
		self.redButtonPressed = False
		self.lastButtonPressedTime = None
		self.singlePressTimeThreshold = 0.2 # in seconds
		self.holdTimeThreshold = 0.4 # in seconds

	def run(self):

		while True:
			self.checkButtonPresses()

			# Are we in a mode?
			if self.appSwitcherMode:
				self.keyboard.send(Keycode.COMMAND)
				self.switchingApps()

			# Check for button presses
			if (self.whiteButtonPressed || self.yellowButtonPressed || self.blueButtonPressed || self.blueButtonPressed) and self.lastButtonPressedTime is None:
				self.lastButtonPressedTime = time.monotonic()

			if self.whiteButtonPressed && !self.appSwitcherMode && self.isSinglePress():
				self.appSwitcherMode = True 
				self.keyboard.send(Keycode.COMMAND, Keycode.TAB)

			if self.yellowButtonPressed:
				if self.isSinglePress() || self.isHold()
					self.keyboard.send(Keycode.SHIFT, Keycode.OPTION, 'g') # Whatever SIRI is mapped to

			if self.blueButtonPressed && self.isSinglePress():
				self.keyboard.send(Keycode.COMMAND, Keycode.SHIFT, 'a') # Zoom mute / unmute

			if self.redButtonPressed && self.isSinglePress():
				self.keyboard.send(Keycode.COMMAND, Keycode.SHIFT, 'm') # Teams mute / unmute

			# Reset if nothing is pressed
			if (!self.whiteButtonPressed && !self.yellowButtonPressed && !self.blueButtonPressed && !self.blueButtonPressed):
				self.lastButtonPressedTime = None

	
	def checkButtonPresses(self):
		self.whiteButtonPressed = cpx.touch_A1
		self.yellowButtonPressed = cpx.touch_A2
		self.blueButtonPressed = cpx.touch_A3
		self.redButtonPressed = cpx.touch_A4

	def isSinglePress(self):
		currentTime = time.monotonic()
		return currentTime >= self.lastButtonPressedTime + self.singlePressTimeThreshold && currentTime <= self.lastButtonPressedTime + self.holdTimeThreshold

	def isHold(self):
		currentTime = time.monotonic()
		return currentTime > self.lastButtonPressedTime + self.holdTimeThreshold


	def switchingApps(self):
		# Backwards
		if self.redButtonPressed && self.isSinglePress():
			self.keyboard.send(Keycode.COMMAND, Keycode.TAB)

		#Forwards
		if self.blueButtonPressed && self.isSinglePress():
			self.keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.TAB)

		if self.yellowButtonPressed && self.isSinglePress():
			self.appSwitcherMode = False





footController = new FootController()
footController.run()
