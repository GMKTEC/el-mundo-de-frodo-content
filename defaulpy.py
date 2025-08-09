
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
    # Menú principal del addon
    addon.add_directory({
        'mode': 'peliculas',
        'url': '',
        'title': 'Peliculas | Movies',
        'is_folder': True,
    })
    addon.add_directory({
        'mode': 'series',
        'url': '',
        'title': 'Series | TV Shows',
        'is_folder': True,
    })
    addon.add_directory({
        'mode': 'documentales',
        'url': '',
        'title': 'Documentales | Documentaries',
        'is_folder': True,
    })
    addon.add_directory({
        'mode': 'cocina',
        'url': '',
        'title': 'Cocina | Cooking',
        'is_folder': True,
    })


@plugin.route('/peliculas')
def peliculas():
    # Aquí puedes añadir los ítems de tu lista de películas
    xbmcgui.ListItem("El Señor de los Anillos: La Comunidad del Anillo")
    xbmcgui.ListItem("El Señor de los Anillos: Las Dos Torres")


if __name__ == '__main__':
    plugin.run()
