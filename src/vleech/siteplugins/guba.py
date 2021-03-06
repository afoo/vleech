# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re


class Guba(Plugin):

    site = 'guba.com'

    URL_RE = r'(http://free\.guba\.com/uploaditem/.*?)"'
    TITLE_RE = r'var theName="(.*?)"'

    def parse(self, url, data):
        url = self._data_search(self.URL_RE, data, 'could not find URL')
        title = self._data_search(self.TITLE_RE, data, 'could not find title')
        return url, title, 'flv'
        
