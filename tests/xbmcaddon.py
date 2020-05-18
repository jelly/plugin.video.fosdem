# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""This file implements the Kodi xbmcaddon module, either using stubs or alternative functionality"""

# pylint: disable=invalid-name

from __future__ import absolute_import, division, print_function, unicode_literals
from xbmcextra import ADDON_ID, ADDON_INFO, addon_settings

# Ensure the addon settings are retained (as we don't write to disk)
ADDON_SETTINGS = addon_settings(ADDON_ID)


class Addon:
    """A reimplementation of the xbmcaddon Addon class"""

    def __init__(self, id=ADDON_ID):  # pylint: disable=redefined-builtin
        """A stub constructor for the xbmcaddon Addon class"""
        self.id = id
        if id == ADDON_ID:
            self.settings = ADDON_SETTINGS
        else:
            self.settings = addon_settings(id)

    def getAddonInfo(self, key):
        """A working implementation for the xbmcaddon Addon class getAddonInfo() method"""
        stub_info = dict(id=self.id, name=self.id, version='2.3.4', type='kodi.inputstream', profile='special://userdata', path='special://userdata')
        # Add stub_info values to ADDON_INFO when missing (e.g. path and profile)
        addon_info = dict(stub_info, **ADDON_INFO)
        return addon_info.get(self.id, stub_info).get(key)

    def getSetting(self, key):
        """A working implementation for the xbmcaddon Addon class getSetting() method"""
        return self.settings.get(key, '')
