import ugfx
import pyb
import os
from database import *
from filesystem import *
import buttons
import gc
import stm

obj = []
sty = None

def draw(x,y,window):
	global obj
	global sty
	if len(obj) == 0:

		sty1 = ugfx.Style()
		sty1.set_enabled([ugfx.BLUE, ugfx.BLACK, ugfx.GREY, ugfx.GREY])

		sty2 = ugfx.Style()
		sty2.set_enabled([ugfx.RED, ugfx.BLACK, ugfx.GREY, ugfx.GREY])


		ugfx.set_default_font(ugfx.FONT_NAME)
		obj.append(ugfx.Label(5, 10, 310, 40 ,"Dan Nixon", parent=window))

		ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)

		obj.append(ugfx.Label(5, 50, 310, 20, "@technoducky", parent=window, style=sty1))
		obj.append(ugfx.Label(5, 65, 310, 20, "dan-nixon.com", parent=window, style=sty1))

		obj.append(ugfx.Label(5, 90, 310, 20, "Code Monkey", parent=window, style=sty2))
		obj.append(ugfx.Label(5, 105, 310, 20, "Electronics Engineer", parent=window, style=sty2))
		obj.append(ugfx.Label(5, 120, 310, 20, "Mad Scientist", parent=window, style=sty2))

		window.show()
	else:
		window.hide()
		window.show()


def draw_destroy(obj_name):
#there may be some .destroy() functions that could be wanted to be called
	global obj
	for o in obj:
		o.destroy()
	obj = []
