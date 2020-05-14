# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import xml.etree.ElementTree as ET


CACHE = {}
FORMAT_URL = 'https://fosdem.org/{}/schedule/xml'


def fetch_xml(year):
    global CACHE

    if year in CACHE:
        return CACHE[year]

    http_get = urlopen(FORMAT_URL.format(year))
    data = http_get.read()
    http_get.close()
    CACHE[year] = ET.fromstring(data)
    return CACHE[year]


def contains_videos(links):
    videos = list(filter(lambda x: 'video.fosdem.org' in x,
                         map(lambda x: x.attrib['href'], links)))
    return videos != []
