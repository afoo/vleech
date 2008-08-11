# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re


class GoogleVideo(Plugin):

    site = 'video.google.com'

    URL_RE = re.compile(r'right-click <a href="(.*?)"', re.M)
    TITLE_RE = re.compile(r'titlebar-title">(.*?)</div>', re.M)

    def parse(self, url, data):
        m = self.URL_RE.search(data)
        if m is None:
            raise PluginError('could not find video url')
        video_url = m.group(1)

        m = self.TITLE_RE.search(data)
        if m is None:
            raise PluginError('could not find title')
        title = m.group(1)

        return video_url, title, 'mp4'
        
        
