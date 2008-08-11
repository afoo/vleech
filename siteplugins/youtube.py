# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re

class Youtube(Plugin):

    site = 'youtube.com'

    ID_RE = re.compile(r'video_id=(.*?)&', re.M)
    T_RE  = re.compile(r'&t=(.*?)&', re.M)
    TITLE_RE = re.compile(r'&title=(.*)\'', re.M)

    def parse(self, url, data):
        m = self.ID_RE.search(data)
        if m is None:
            raise PluginError('could not find video id')
        video_id = m.group(1).replace("'", '')

        m = self.T_RE.search(data)
        if m is None:
            raise PluginError('could not find "t" variable')
        t = m.group(1).replace("'", '')

        url = 'http://www.youtube.com/get_video?video_id=%s&t=%s&fmt=18' % (video_id, t)

        m = self.TITLE_RE.search(data)
        if m is None:
            raise PluginError('could not find title')
        title = m.group(1)

        return url, title, 'mp4'
