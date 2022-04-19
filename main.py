import usb_hid
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

def run():
	
	while True:
		if cpx.touch_A1:
			kbd.send(Keycode.COMMAND, Keycode.TAB)

        if cpx.touch_A2:
            kbd.send(Keycode.F5)



run()
