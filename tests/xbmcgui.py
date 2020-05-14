# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""This file implements the Kodi xbmcgui module, either using stubs or alternative functionality"""

# pylint: disable=invalid-name,too-few-public-methods,unused-argument

from __future__ import absolute_import, division, print_function, unicode_literals
from xbmcextra import kodi_to_ansi


class Dialog:
    """A reimplementation of the xbmcgui Dialog class"""

    def __init__(self):
        """A stub constructor for the xbmcgui Dialog class"""

    @staticmethod
    def ok(heading, message='', line1='', line2='', line3=''):
        """A stub implementation for the xbmcgui Dialog class ok() method"""
        heading = kodi_to_ansi(heading)
        message = kodi_to_ansi(message)
        print('\033[37;44;1mOK:\033[35;49;1m [%s] \033[37;1m%s\033[39;0m' % (heading, message or line1))


class ListItem:
    """A reimplementation of the xbmcgui ListItem class"""

    def __init__(self, label='', label2='', path='', offscreen=False):
        """A stub constructor for the xbmcgui ListItem class"""
        self.label = kodi_to_ansi(label)
        self.label2 = kodi_to_ansi(label2)
        self.path = path
        self.offscreen = offscreen

        self.art = dict()
        self.content_lookup = None
        self.context_menu = list()
        self.info = dict()
        self.info_type = None
        self.is_folder = False
        self.mimetype = None
        self.properties = dict()
        self.rating = None
        self.stream_info = dict()
        self.stream_type = None
        self.subtitles = list()
        self.unique_ids = list()

    def addContextMenuItems(self, items, replaceItems=False):
        """A stub implementation for the xbmcgui ListItem class addContextMenuItems() method"""
        if replaceItems:
            self.context_menu = items
        else:
            self.context_menu.append(items)

    def addStreamInfo(self, stream_type, stream_values):
        """A stub implementation for the xbmcgui LitItem class addStreamInfo() method"""
        self.stream_type = stream_type
        self.stream_info = stream_values

    def setArt(self, key):
        """A stub implementation for the xbmcgui ListItem class setArt() method"""
        self.art = key

    def setContentLookup(self, enable):
        """A stub implementation for the xbmcgui ListItem class setContentLookup() method"""
        self.content_lookup = enable

    def setInfo(self, type, infoLabels):  # pylint: disable=redefined-builtin
        """A stub implementation for the xbmcgui ListItem class setInfo() method"""
        self.info_type = type
        self.info = infoLabels

    def setIsFolder(self, isFolder):
        """A stub implementation for the xbmcgui ListItem class setIsFolder() method"""
        self.is_folder = isFolder

    def setMimeType(self, mimetype):
        """A stub implementation for the xbmcgui ListItem class setMimeType() method"""
        self.mimetype = mimetype

    def setPath(self, path):
        """A stub implementation for the xbmcgui ListItem class setPath() method"""
        self.path = path

    def setProperty(self, key, value):
        """A stub implementation for the xbmcgui ListItem class setProperty() method"""
        self.properties[key] = value

    def setProperties(self, dictionary):
        """A stub implementation for the xbmcgui ListItem class setProperties() method"""
        self.properties.update(dictionary)

    def setSubtitles(self, subtitleFiles):
        """A stub implementation for the xbmcgui ListItem class setSubtitles() method"""
        self.subtitles = subtitleFiles

    def setUniqueIDs(self, values, defaultrating=None):
        """A stub implementation for the xbmcgui ListItem class setUniqueIDs() method"""
        self.unique_ids = values
        self.rating = defaultrating
