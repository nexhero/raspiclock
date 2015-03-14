#!/usr/bin/env python
import os
import pygtk
import yaml
import sys
pygtk.require('2.0')
import gtk

class Table():

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_size_request(320, 240)
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
        self.table =  gtk.Table(4, 4)
        self.window.add(self.table)
    def show(self):
        self.window.show_all()

def rcPath():
    return os.path.dirname(__file__)


def main():
    path = rcPath()
    path = path + "/raspiclock.yaml"
    stream = file(path, "r")
    try:
        data = yaml.load(stream)
    except ValueError:
        sys.exit("Config file error")

    t = Table()

    for e in data['modules']:
        m = data['modules'][e]
        f = m['file']
        name = "modules." + f
        try:
            mod = __import__(name, fromlist=[''])
            comp = mod.Component()
            t.table.attach(comp.getL(), m['x0'], m['x1'], m['y0'], m['y1'],xoptions = gtk.FILL, yoptions = gtk.FILL)
            gtk.timeout_add(int(m['update']), comp.update)
        except ValueError:
            sys.exit( name + "Module Error")

    t.show()
    gtk.main()

if __name__ == "__main__":
    main()
