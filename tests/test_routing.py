# -*- coding: utf-8 -*-
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Integration tests for Routing functionality"""

# pylint: disable=invalid-name

from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
import addon

xbmc = __import__('xbmc')
xbmcaddon = __import__('xbmcaddon')
xbmcgui = __import__('xbmcgui')
xbmcplugin = __import__('xbmcplugin')

plugin = addon.plugin


class TestRouting(unittest.TestCase):
    """TestCase class"""

    def test_main_menu(self):
        """Main menu: /"""
        addon.run(['plugin://plugin.video.fosdem', '0', ''])
        self.assertEqual(plugin.url_for(addon.main_menu), 'plugin://plugin.video.fosdem/')

    def test_show_dir(self):
        """Directory: /dir/2020"""
        addon.run(['plugin://plugin.video.fosdem/dir/2020', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_dir, subdir='2020'), 'plugin://plugin.video.fosdem/dir/2020')

    def test_show_day(self):
        """Day: /day/2020/1"""
        addon.run(['plugin://plugin.video.fosdem/day/2020/1', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_day, year='2020', day='1'), 'plugin://plugin.video.fosdem/day/2020/1')

    def test_show_room(self):
        """Room: /room/2020/1/Janson"""
        addon.run(['plugin://plugin.video.fosdem/room/2020/1/Janson', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_room, year='2020', day='1', room='Janson'), 'plugin://plugin.video.fosdem/room/2020/1/Janson')
        addon.run(['plugin://plugin.video.fosdem/room/2016/1/UB2.252A (Lameere)', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_room, year='2016', day='1', room='UB2.252A (Lameere)'),
                         'plugin://plugin.video.fosdem/room/2016/1/UB2.252A (Lameere)')

    def test_show_event(self):
        """Event: /event/2020/9025"""
        addon.run(['plugin://plugin.video.fosdem/event/2020/9025', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_event, year='2020', event_id='9025'), 'plugin://plugin.video.fosdem/event/2020/9025')
        addon.run(['plugin://plugin.video.fosdem/event/2020/10715', '0', ''])
        self.assertEqual(plugin.url_for(addon.show_event, year='2020', event_id='10715'), 'plugin://plugin.video.fosdem/event/2020/10715')

    def test_show_event_fail(self):
        """Event: /event/2020/9604"""
        addon.run(['plugin://plugin.video.fosdem/event/2020/9604', '0', ''])
        self.assertNotEqual(plugin.url_for(addon.show_event, year='2020', event_id='9604'), 'plugin://plugin.video.fosdem/event/2020/9604')
