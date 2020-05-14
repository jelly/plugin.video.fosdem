# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Extra functions for testing"""

# pylint: disable=invalid-name

from __future__ import absolute_import, division, print_function, unicode_literals
import xml.etree.ElementTree as ET


def kodi_to_ansi(string):
    """Convert Kodi format tags to ANSI codes"""
    if string is None:
        return None
    string = string.replace('[B]', '\033[1m')
    string = string.replace('[/B]', '\033[21m')
    string = string.replace('[I]', '\033[3m')
    string = string.replace('[/I]', '\033[23m')
    string = string.replace('[COLOR=gray]', '\033[30;1m')
    string = string.replace('[COLOR=red]', '\033[31m')
    string = string.replace('[COLOR=green]', '\033[32m')
    string = string.replace('[COLOR=yellow]', '\033[33m')
    string = string.replace('[COLOR=blue]', '\033[34m')
    string = string.replace('[COLOR=purple]', '\033[35m')
    string = string.replace('[COLOR=cyan]', '\033[36m')
    string = string.replace('[COLOR=white]', '\033[37m')
    string = string.replace('[/COLOR]', '\033[39;0m')
    return string


def uri_to_path(uri):
    """Shorten a plugin URI to just the path"""
    if uri is None:
        return None
    return ' \033[33m→ \033[34m%s\033[39;0m' % uri.replace('plugin://' + ADDON_ID, '')


def read_addon_xml(path):
    """Parse the addon.xml and return an info dictionary"""
    info = dict(
        path='./',  # '/storage/.kodi/addons/plugin.video.fosdem',
        profile='special://userdata',  # 'special://profile/addon_data/plugin.video.fosdem/',
        type='xbmc.python.pluginsource',
    )

    tree = ET.parse(path)
    root = tree.getroot()

    info.update(root.attrib)  # Add 'id', 'name' and 'version'
    info['author'] = info.pop('provider-name')

    for child in root:
        if child.attrib.get('point') != 'xbmc.addon.metadata':
            continue
        for grandchild in child:
            # Handle assets differently
            if grandchild.tag == 'assets':
                for asset in grandchild:
                    info[asset.tag] = asset.text
                continue
            # Not in English ?  Drop it
            if grandchild.attrib.get('lang', 'en_GB') != 'en_GB':
                continue
            # Add metadata
            info[grandchild.tag] = grandchild.text

    return {info['name']: info}


def addon_settings(addon_id=None):
    """Use the addon_settings file"""
    import json
    try:
        with open('tests/userdata/addon_settings.json') as fdesc:
            settings = json.load(fdesc)
    except OSError as e:
        print("Error: Cannot use 'tests/userdata/addon_settings.json' : %s" % e)
        settings = {}

    if addon_id:
        return settings[addon_id]

    return settings


ADDON_INFO = read_addon_xml('addon.xml')
ADDON_ID = next(iter(list(ADDON_INFO.values()))).get('id')
