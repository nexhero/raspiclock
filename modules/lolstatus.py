from riotwatcher import RiotWatcher
import gtk
import pango
import urllib2

#Constans
urlicon = "http://lkimg.zamimg.com/shared/riot/images/profile_icons/profileIcon26.jpg"
class Component:
    def __init__(self, raspiclock):
        self.lolkey = '4b6141d1-344f-4b4b-841c-01deeb170f7a'
        self.L = gtk.Frame()

        f = gtk.Fixed()
        self.text = gtk.Label()
        self.status = gtk.Label()
        self.icon = gtk.Image()

        iconres = urllib2.urlopen(urlicon)
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(65, 65, gtk.gdk.INTERP_NEAREST)

        self.icon.set_from_pixbuf(iconloader)
        print self.icon.get_pixel_size()
        self.text.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFA500"))
        self.text.modify_font(pango.FontDescription("Coolvetica 12"))
        self.status.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FFA500"))
        self.status.modify_font(pango.FontDescription("Coolvetica 12"))

        w = RiotWatcher(self.lolkey)
        status = w.get_server_status('lan')

        self.text.set_text(status['name'])
        self.status.set_text(status['services'][1]['status'])

        #print status
        #f.put(self.text, 5,10)
        f.put(self.icon, 0,0)
        #f.put(self.status, 50, 35)

        self.L.add(f)

    def update(self):
        return True

    def getL(self):
        return self.L
