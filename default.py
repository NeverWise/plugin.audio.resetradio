#!/usr/bin/python
import neverwise as nw, os#, datetime


class ResetRadio(object):

  def __init__(self):

    # http://resetdiretta.ns0.it:8000 # URL alternativo.
    # Ho tentato di inserire il nome della radio tra le informazioni della canzone ma dallo stream ricevo le informazioni della canzone corrente che cancellano il nome della radio.
    li = nw.createListItem(nw.addonName, thumbnailImage = '{0}/icon.png'.format(os.path.dirname(os.path.abspath(__file__))), streamtype = 'music', infolabels = { 'title' : nw.addonName })
    xbmc.Player().play('http://resetradiolive.ns0.it:8000', li)

# Entry point.
#startTime = datetime.datetime.now()
rr = ResetRadio()
del rr
#xbmc.log('{0} azione {1}'.format(nw.addonName, str(datetime.datetime.now() - startTime)))