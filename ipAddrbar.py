#!/usr/bin/env python
import rumps
import requests


class IP_Address_Bar(rumps.App):
    def __init__(self):
        res = requests.get('http://ipinfo.io/ip')
        abc = ("Internet IP : " + res.text.strip() )
        super(IP_Address_Bar, self).__init__("IP BAR")
        
        self.title = abc
        self.menu = ["Display Public IP"]

    @rumps.clicked("Display Public IP")
    def prefs(self, _):
      rumps.alert(title="Your Current Internet IP", message=self.title )

if __name__ == "__main__":
    IP_Address_Bar().run()
