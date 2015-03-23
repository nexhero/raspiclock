from riotwatcher import RiotWatcher
import gtk
import pango
import urllib2

#Constans
_urlicon = "http://lkimg.zamimg.com/shared/riot/images/profile_icons/profileIcon"
summonername = "nexhero"
class Component:
    def __init__(self, raspiclock):
        summonername = raspiclock.getConfig("lol_summoner")
        self.lolkey = raspiclock.getConfig("lol_key")
        self.L = gtk.Frame()

        f = gtk.Fixed()
        self.text = gtk.Label()
        self.status = gtk.Label()
        self.icon = gtk.Image()

        w = RiotWatcher(self.lolkey, default_region = raspiclock.getConfig("lol_server"))
        summoner = w.get_summoner(name=summonername)
        urlicon =_urlicon + str(summoner['profileIconId']) +".jpg"
        status = w.get_server_status(raspiclock.getConfig("lol_server"))

        iconres = urllib2.urlopen(urlicon)
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(65, 65, gtk.gdk.INTERP_NEAREST)

        self.icon.set_from_pixbuf(iconloader)
        self.text.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#E07D4F"))
        self.text.modify_font(pango.FontDescription("Coolvetica 12"))
        self.status.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#85F2AA"))
        self.status.modify_font(pango.FontDescription("Coolvetica 12"))



        self.text.set_text("LAN")
        self.status.set_text(status['services'][1]['status'])

        #print status
        f.put(self.text, 80,10)
        f.put(self.icon, 5,5)
        f.put(self.status, 80, 35)

        self.L.add(f)

    def update(self):
        w = RiotWatcher(self.lolkey, default_region = 'lan')
        summoner = w.get_summoner(name='nexhero')
        urlicon =_urlicon + str(summoner['profileIconId']) +".jpg"
        status = w.get_server_status('lan')

        iconres = urllib2.urlopen(urlicon)
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(65, 65, gtk.gdk.INTERP_NEAREST)

        self.status.set_text(status['services'][1]['status'])
        self.icon.set_from_pixbuf(iconloader)

        return True

    def getL(self):
        return self.L
