# -*- coding: utf-8 -*-
# Módulo principal para el addon.

import routing
import xbmc
import xbmcgui
from xbmcaddon import Addon

# Objeto del addon
addon = Addon()

# Router
plugin = routing.Plugin()

@plugin.route('/')
def index():
    xbmcgui.ListItem("Peliculas | Movies")
    xbmcgui.ListItem("Series | TV Shows")
    xbmcgui.ListItem("Documentales | Documentaries")
    xbmcgui.ListItem("Cocina | Cooking")

if __name__ == '__main__':
    plugin.run()
