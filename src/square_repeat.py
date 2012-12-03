#!/usr/bin/python

import gtk
import gtk.gdk as gdk
import math
import random
import gobject

# The number of circles and the window size.
num = 400
size = 512

# Initialize circle coordinates and velocities.

def expose(*args):
    cr = darea.window.cairo_create()
    cr.set_line_width(4)
    for i in range(num):
        cr.set_source_rgb(1, 0, 0)
 	cr.rectangle(50, 50, i, i)
	print i
        #cr.arc(x[i], y[i], 8, 0, 2 * math.pi)
        cr.stroke_preserve()
        cr.set_source_rgb(1, 1, 1)
        #cr.fill()

# Self-evident?
def timeout():
    darea.queue_draw()
    return True


# Initialize the window.
window = gtk.Window()
window.resize(size, size)
window.connect("destroy", gtk.main_quit)
darea = gtk.DrawingArea()
darea.connect("expose-event", expose)
window.add(darea)
window.show_all()


# Self-evident?
gobject.idle_add(timeout)
gtk.main()









