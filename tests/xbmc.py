# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""This file implements the Kodi xbmc module, either using stubs or alternative functionality"""

# pylint: disable=invalid-name,no-self-use,unused-argument

from __future__ import absolute_import, division, print_function, unicode_literals

LOGLEVELS = ['Debug', 'Info', 'Notice', 'Warning', 'Error', 'Severe', 'Fatal', 'None']
LOGDEBUG = 0
LOGINFO = 1
LOGNOTICE = 2
LOGWARNING = 3
LOGERROR = 4
LOGSEVERE = 5
LOGFATAL = 6
LOGNONE = 7


def log(msg, level=0):
    """A reimplementation of the xbmc log() function"""
    color1 = '\033[32;1m'
    color2 = '\033[32;0m'
    name = LOGLEVELS[level]
    if level in (4, 5, 6, 7):
        color1 = '\033[31;1m'
        if level in (6, 7):
            raise Exception(msg)
    elif level in (2, 3):
        color1 = '\033[33;1m'
    elif level == 0:
        color2 = '\033[30;1m'
    print('{color1}{name}: {color2}{msg}\033[39;0m'.format(name=name, color1=color1, color2=color2, msg=msg))
