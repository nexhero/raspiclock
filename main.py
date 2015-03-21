#!/usr/bin/env python
import os
import pygtk
import yaml
import sys
import gtk
import raspiclock
#pygtk.require('2.0')

class Table():

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_size_request(320, 240)
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
        self.table =  gtk.Table(4, 4)
        self.window.add(self.table)
    #    self.window.fullscreen()
    def show(self):
        self.window.show_all()


def main():
    rc = raspiclock.raspiclock()
    data = rc.ModulesList()
    t = Table()

    for key in data:
        m = data[key]
        f = key
        name = "modules." + f
        try:
            mod = __import__(name, fromlist=[''])
            comp = mod.Component(rc)
            t.table.attach(comp.getL(), m['x0'], m['x1'], m['y0'], m['y1'],xoptions = gtk.FILL, yoptions = gtk.FILL)
            gtk.timeout_add(int(m['update']), comp.update)
        except Exception as inst:
            print inst
            sys.exit( "Module Error " + name)

    t.show()
    gtk.main()

if __name__ == "__main__":
    main()
