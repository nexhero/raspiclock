import pygtk
import pango

import sys
import gtk
import time
import pywapi
import string

class Component:
    def __init__(self, L = gtk.Frame ()):
        f = gtk.Fixed()

        self.temp = gtk.Label()
        self.temp.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.temp.modify_font(pango.FontDescription("GE Inspira 20"))

        self.text = gtk.Label()
        self.text.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))

        w = pywapi.get_weather_from_weather_com('75062')
        temp = w['current_conditions']['temperature']
        temp =(float(temp) * 9)//5 + 32

        self.temp.set_text(str(temp) + " F" )
        self.text.set_text(w['current_conditions']['text'])


        f.put(self.temp, 5, 10)
        f.put(self.text, 5, 50)

        L.add(f)
        L.show_all()
        self.L = L


    def update(self):
        w = pywapi.get_weather_from_weather_com('75062')
        temp = w['current_conditions']['temperature']
        temp =(float(temp) * 9)//5 + 32

        self.temp.set_text(str(temp) + " F" )
        self.text.set_text(w['current_conditions']['text'])


        return True

    def getL(self):
        return self.L
