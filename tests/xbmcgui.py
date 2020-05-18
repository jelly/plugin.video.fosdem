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

    @staticmethod
    def addContextMenuItems(items, replaceItems=False):
        """A stub implementation for the xbmcgui ListItem class addContextMenuItems() method"""
        return

    @staticmethod
    def addStreamInfo(stream_type, stream_values):
        """A stub implementation for the xbmcgui LitItem class addStreamInfo() method"""
        return

    @staticmethod
    def setArt(key):
        """A stub implementation for the xbmcgui ListItem class setArt() method"""
        return

    @staticmethod
    def setContentLookup(enable):
        """A stub implementation for the xbmcgui ListItem class setContentLookup() method"""
        return

    @staticmethod
    def setInfo(type, infoLabels):  # pylint: disable=redefined-builtin
        """A stub implementation for the xbmcgui ListItem class setInfo() method"""
        return

    @staticmethod
    def setIsFolder(isFolder):
        """A stub implementation for the xbmcgui ListItem class setIsFolder() method"""
        return

    @staticmethod
    def setMimeType(mimetype):
        """A stub implementation for the xbmcgui ListItem class setMimeType() method"""
        return

    def setPath(self, path):
        """A stub implementation for the xbmcgui ListItem class setPath() method"""
        self.path = path

    @staticmethod
    def setProperty(key, value):
        """A stub implementation for the xbmcgui ListItem class setProperty() method"""
        return

    @staticmethod
    def setProperties(dictionary):
        """A stub implementation for the xbmcgui ListItem class setProperties() method"""
        return

    @staticmethod
    def setSubtitles(subtitleFiles):
        """A stub implementation for the xbmcgui ListItem class setSubtitles() method"""
        return

    @staticmethod
    def setUniqueIDs(values, defaultrating=None):
        """A stub implementation for the xbmcgui ListItem class setUniqueIDs() method"""
        return
