import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon

addon = xbmcaddon.Addon()

username = addon.getSetting('username') or 'Visitor'

itemWelcome = xbmcgui.ListItem('Welcome, %s' % username)
itemSportsTV = xbmcgui.ListItem('Sports TV')
itemNetworkTV = xbmcgui.ListItem('Network TV')
itemMovies = xbmcgui.ListItem('Movies')

xbmcplugin.addDirectoryItem(int(sys.argv[1]), '', itemNetworkTV, isFolder=0)
xbmcplugin.addDirectoryItem(int(sys.argv[1]), '', itemSportsTV, isFolder=0)
xbmcplugin.addDirectoryItem(int(sys.argv[1]), '', itemMovies, isFolder=0)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
