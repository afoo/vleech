# -*- coding: utf-8 -*-

from vleech.plugin import Plugin, PluginError

import re


class GoogleVideo(Plugin):

    site = 'video.google.com'

    URL_RE   = r'right-click <a href="(.*?)"'
    TITLE_RE = r'titlebar-title">(.*?)</div>'

    def parse(self, url, data):
        video_url = self._data_search(self.URL_RE, data, 'could not find video url')
        title = self._data_search(self.TITLE_RE, data, 'could not find title')
        return video_url, title, 'mp4'
        
        
