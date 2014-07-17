#!/usr/bin/python
import os
from neverwise import Util

# http://resetdiretta.ns0.it:8000 # URL alternativo.
# Ho tentato di inserire il nome della radio tra le informazioni della canzone ma dallo stream ricevo le informazioni della canzone corrente che cancellano il nome della radio.
li = Util.createListItem('Reset Radio', os.path.dirname(os.path.abspath(__file__)) + '/icon.png', '', 'music', { 'title' : 'Reset Radio' })
xbmc.Player(xbmc.PLAYER_CORE_PAPLAYER).play('http://resetradiolive.ns0.it:8000', li)
