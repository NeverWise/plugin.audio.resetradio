# Version 1.0.0 (16/09/2013)
# Reset Radio
# La prima web radio europea di musica Creative Commons in Free-Download.
# By NeverWise
# <mail>
# <url>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################
import os, xbmc, tools

# http://resetdiretta.ns0.it:8000 # URL alternativo.
# Ho tentato di inserire il nome della radio tra le informazioni della canzone ma dallo stream ricevo le informazioni della canzone corrente che cancellano il nome della radio.
li = tools.createListItem('Reset Radio', os.path.dirname(os.path.abspath(__file__)) + '/icon.png', '', 'music', { 'title' : 'Reset Radio' })
xbmc.Player(xbmc.PLAYER_CORE_PAPLAYER).playStream('http://resetradiolive.ns0.it:8000', li)
