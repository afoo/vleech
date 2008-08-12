# -*- coding: utf-8 -*-

from vleech.plugin import Plugin

import re


class MyVideo(Plugin):

    site = 'myvideo.de'

    URL_RE   = r'.swf\?(.*?)&'
    TITLE_RE = r'\d/(.*?)\?'

    def parse(self, url, data):
        vurl = self._data_search(self.URL_RE, data, 'could not find URL')
        title = self._data_search(self.TITLE_RE, url, 'could not find title')
        return vurl, title, 'flv'
