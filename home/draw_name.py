import ugfx
import pyb
import os
from database import *
from filesystem import *
import buttons
import gc
import stm

obj = []
sty = {}

def draw(x,y,window):
    global obj
    global sty

    if len(obj) == 0:
        sty['twitter'] = ugfx.Style()
        sty['twitter'].set_enabled([ugfx.html_color(0x00FFFF), ugfx.BLACK, ugfx.GREY, ugfx.GREY])

        sty['web'] = ugfx.Style()
        sty['web'].set_enabled([ugfx.BLUE, ugfx.BLACK, ugfx.GREY, ugfx.GREY])

        sty['profile'] = ugfx.Style()
        sty['profile'].set_enabled([ugfx.RED, ugfx.BLACK, ugfx.GREY, ugfx.GREY])

        ugfx.set_default_font(ugfx.FONT_NAME)
        obj.append(ugfx.Label(5, 10, 310, 40 ,"Dan Nixon", parent=window))

        ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)

        obj.append(ugfx.Label(180, 65, 310, 25, "@technoducky", parent=window, style=sty['twitter']))
        obj.append(ugfx.Label(180, 90, 310, 25, "dan-nixon.com", parent=window, style=sty['web']))

        obj.append(ugfx.Label(5, 65, 170, 25, "Code Monkey", parent=window, style=sty['profile']))
        obj.append(ugfx.Label(5, 90, 170, 25, "Electronics Engineer", parent=window, style=sty['profile']))
        obj.append(ugfx.Label(5, 115, 170, 25, "Mad Scientist", parent=window, style=sty['profile']))

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
