# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re

class Youtube(Plugin):

    site = 'youtube.com'

    ID_RE = re.compile(r'video_id=(.*?)&', re.M)
    T_RE  = re.compile(r'&t=(.*?)&', re.M)
    TITLE_RE = re.compile(r'&title=(.*)\'', re.M)

    def parse(self, url, data):
        video_id = self._data_search(self.ID_RE, data, 'could not find video id')
        video_id = video_id.replace("'", '')

        t = self._data_search(self.T_RE, data, 'could not find "t" variable')
        t = t.replace("'", '')

        url = 'http://www.youtube.com/get_video?video_id=%s&t=%s&fmt=18' % (video_id, t)

        title = self._data_search(self.TITLE_RE, data, 'vould not find title')

        return url, title, 'mp4'
