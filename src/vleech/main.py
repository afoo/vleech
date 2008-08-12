# -*- coding: utf-8 -*-

import glob
import os
import sys
import re
import urllib2
import urlparse
from subprocess import call

from vleech.plugin import plugins, PluginError
from vleech.siteplugins import *


__all__ = ['main']

class Config(object):
    KEYS = (
        'plugin_dir',
        'user_agent',
        'downloader')

    # defaults
    plugin_dir = os.path.join(os.environ['HOME'], '.vleech/siteplugins/')
    user_agent = 'Vleech 0.2'
    downloader = 'curl' # or wget

    def __init__(self):
        try:
            cf = open(os.path.join(os.environ['HOME'], '.vleech/config'))
            config = cf.read()
            cf.close()
        except IOError:
            config = ''
        for line in config.splitlines():
            try:
                key, value = re.split(r'\s*=\s*', line)
            except ValueError:
                continue
            if key in self.KEYS:
                setattr(self, key, value)
            else:
                warn('uknown config key: ' + key)

                     
def err(msg):
    sys.stderr.write('ERROR: %s\n' % (msg,))
    sys.exit(1)

def warn(msg):
    sys.stderr.write('WARNING: %s\n' % (msg,))

def load_plugins(config):
    if not os.path.exists(config.plugin_dir):
        os.makedirs(config.plugin_dir)
    sys.path.insert(0, config.plugin_dir)
    for plugin in glob.glob(os.path.join(config.plugin_dir, '*.py')):
        __import__(os.path.basename(plugin)[:-3])
    sys.path.pop(0)

def make_video_filename(title, type):
    return title.lower().replace(' ', '_') + '.' + type

def main(argv):
    if len(argv) != 2:
        err('USAGE: vleech <url>')
    config = Config()
    load_plugins(config)
    url = argv[1]
    plugin = None
    for p in plugins:
        if p in url:
            plugin = plugins[p]
            break
    if plugin is None:
        err('no valid plugin for that URL found')
    plugin = plugin()

    request = urllib2.Request(url)
    request.add_header('User-Agent', config.user_agent)
    opener = urllib2.build_opener()
    data = opener.open(request).read()
    try:
        video_url, video_title, video_type = plugin.parse(url, data)
    except PluginError, e:
        err(str(e))
    print 'video url:', video_url
    print 'video title:', video_title
    video_file = make_video_filename(video_title, video_type)
    print 'filename:', video_file
    if os.path.exists(video_file):
        err('%s already exists' % video_file)
    downloaders = dict(
        curl = lambda f, url: ('curl', '-L', '-o', f, '-A', config.user_agent, url),
        wget = lambda f, url: ('wget', '-O', f, '-U', config.user_agent, url))
    cmd = downloaders.get(config.downloader)
    if cmd is None:
        err('no valid downloader configured')
    call(cmd(video_file, video_url))
    
