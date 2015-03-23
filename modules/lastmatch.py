from riotwatcher import RiotWatcher
import gtk
import pango
import urllib2


_urlicon = "http://www.lolking.net/shared/images/champion_headers/1_0.jpg"

class Component:
    def __init__(self, raspiclock):
        summonername = raspiclock.getConfig("lol_summoner")
        self.lolkey = raspiclock.getConfig("lol_key")

        self.L = gtk.Frame()
        f = gtk.Fixed()

        self.match = gtk.Image()

        iconres = urllib2.urlopen(_urlicon)
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(303,50 , gtk.gdk.INTERP_NEAREST)

        self.match.set_from_pixbuf(iconloader)
        f.put(self.match, 5, 0)
        self.L.add(f)
    def update(self):
        return True

    def getL(self):
        return self.L
