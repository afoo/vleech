# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re


class Break(Plugin):

    site = 'break.com'

    PATH_RE = re.compile(r'ContentFilePath=\'(.*?)\'', re.M)
    NAME_RE = re.compile(r'FileName=\'(.*?)\'', re.M)

    def parse(self, url, data):
        path = self._data_search(self.PATH_RE, data, 'file path not found')
        name = self._data_search(self.NAME_RE, data, 'file name not found')
        url = 'http://media1.break.com/dnet/media/%s/%s.wmv' % (path, name)
        return url, name, 'wmv'

        
