import pygtk
import pango
import gtk
import time

class Component:
    def __init__(self, ):

        f = gtk.Fixed()
        self.L = gtk.Frame()
        self.time = gtk.Label()
        self.day = gtk.Label()
        self.month = gtk.Label()

        self.time.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.time.modify_font(pango.FontDescription("GE Inspira 48"))

        self.day.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFA500"))
        self.day.modify_font(pango.FontDescription("GE Inspira 20"))

        self.month.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFA500"))
        self.month.modify_font(pango.FontDescription("GE Inspira 20"))

        f.put(self.time, 10, 10)
        f.put(self.day, 160, 10)
        f.put(self.month, 160, 40)
        self.L.add(f)


    def update(self):
        self.time.set_text(time.strftime('%H:%M'))
        self.day.set_text(time.strftime('%d'))
        self.month.set_text(time.strftime('%B'))
        return True

    def getL(self):
        return self.L
