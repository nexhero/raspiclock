import pygtk
import pango
import gtk
import time
import json
import urllib

import requests

class Component:
    def __init__(self, raspiclock):
        self.url = raspiclock.getConfig("systeminfo")

        f = gtk.Fixed()
        self.L = gtk.Frame("Computer Information")

        self.MemPer = gtk.Label()
        self.MemFree = gtk.Label()
        self.MemTotal = gtk.Label()

        r = requests.get(self.url)
        data = r.json()

        memTotal = data['mem']['MemTotal']
        memFree = data['mem']['MemFree']
        memPer = (float(memFree)/float(memTotal))*100
        memPer = round(memPer,2)
        memPer = 100 - memPer
        self.MemFree.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.MemFree.modify_font(pango.FontDescription("Coolvetica 14"))
        self.MemFree.set_text("Free: " + memFree + "kB")

        self.MemTotal.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.MemTotal.modify_font(pango.FontDescription("Coolvetica 14"))
        self.MemTotal.set_text("Total: " + memTotal + "kB")

        self.MemPer.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFFFFF"))
        self.MemPer.modify_font(pango.FontDescription("Coolvetica 14"))
        self.MemPer.set_text("MemPer: " + str(memPer) + "%")

        f.put(self.MemFree, 10, 5)
        f.put(self.MemTotal, 10, 25)
        f.put(self.MemPer, 10, 45)

        self.L.add(f)


    def update(self):

        r = requests.get(self.url)
        data = r.json()
        memTotal = data['mem']['MemTotal']
        memFree = data['mem']['MemFree']
        memPer = (float(memFree)/float(memTotal))*100
        memPer = round(memPer,2)
        memPer = 100 - memPer

        self.MemFree.set_text("Free: " + memFree + "kB")
        self.MemTotal.set_text("Total: " + memTotal + "kB")
        self.MemPer.set_text(str(memPer) + "%")

        return True

    def getL(self):
        return self.L
