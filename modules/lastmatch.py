from riotwatcher import RiotWatcher
import gtk
import pango
import urllib2
import time
import json
_urlicon = "http://www.lolking.net/shared/images/champion_headers/"

class Component:
    def __init__(self, raspiclock):
        summonername = raspiclock.getConfig("lol_summoner")
        self.lolkey = raspiclock.getConfig("lol_key")

        self.L = gtk.Frame()
        f = gtk.Fixed()

        self.match = gtk.Image()
        self.kda = gtk.Label()

        self.kda.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#85F2AA"))
        self.kda.modify_font(pango.FontDescription("Coolvetica 12"))

        w = RiotWatcher(self.lolkey, default_region = raspiclock.getConfig("lol_server"))
        summoner = w.get_summoner(name=summonername)
        sumid= summoner['id']
        print sumid
        #urlicon =_urlicon + str(summoner['profileIconId']) +"_0.jpg"

        match = w.get_match_history(sumid)
        #print json.dumps(match['matches'][0]['participants'][0]['championId'], sort_keys=True, indent=4, separators=(',', ': '))
        last = -1
        for key in match['matches']:
                last = last + 1
                print last

        champ =  match['matches'][last]['participants'][0]['championId']
        urlicon = _urlicon + str(champ) + "_0.jpg"

        iconres = urllib2.urlopen("http://www.lolking.net/shared/images/champion_headers/412_0.jpg")
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(393,65 , gtk.gdk.INTERP_NEAREST)

        self.match.set_from_pixbuf(iconloader)




        self.kda.set_text("KDA: 16.5")

        f.put(self.match, -80, 0)
        self.L.add(f)
    def update(self):
        w = RiotWatcher(self.lolkey, default_region = 'lan')
        summoner = w.get_summoner(name='nexhero')
        sumid= summoner['id']
        print sumid
        _urlicon = "http://www.lolking.net/shared/images/champion_headers/"
        urlicon =_urlicon + str(summoner['profileIconId']) +"_0.jpg"

        match = w.get_match_history(sumid)
        #print json.dumps(match['matches'][0]['participants'][0]['championId'], sort_keys=True, indent=4, separators=(',', ': '))
        last = -1
        for key in match['matches']:
                last = last + 1
                print last

        champ =  match['matches'][last]['participants'][0]['championId']
        print urlicon
        urlicon = _urlicon + str(champ) + "_0.jpg"

        iconres = urllib2.urlopen(urlicon)
        iconloader = gtk.gdk.PixbufLoader()
        iconloader.write(iconres.read())
        iconloader.close()
        iconloader = iconloader.get_pixbuf()
        iconloader = iconloader.scale_simple(393,65 , gtk.gdk.INTERP_NEAREST)

        self.match.set_from_pixbuf(iconloader)

        return True

    def getL(self):
        return self.L
