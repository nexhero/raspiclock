import pygtk
import pango

import sys
import gtk
import time
import pywapi
import string

class Component:
    def __init__(self, raspiclock):
        f = gtk.Fixed()
        self.L = gtk.Frame ()
        #self.L.set_shadow_type(gtk.SHADOW_NONE)

        self.temp = gtk.Label()
        self.temp.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.temp.modify_font(pango.FontDescription("Coolvetica 20"))

        self.text = gtk.Label()
        self.text.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))

        w = pywapi.get_weather_from_yahoo('75062')
        temp = w['condition']['temp']
        temp =(float(temp) * 9)//5 + 32

        self.temp.set_text(str(temp) + " F" )
        self.text.set_text(w['condition']['text'])


        f.put(self.temp, 5, 10)
        f.put(self.text, 5, 50)

        self.L.add(f)


    def update(self):
        w = pywapi.get_weather_from_yahoo('75062')
        temp = w['condition']['temp']
        temp =(float(temp) * 9)//5 + 32

        self.temp.set_text(str(temp) + " F" )
        self.text.set_text(w['condition']['text'])


        return True

    def getL(self):
        return self.L
