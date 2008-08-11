# -*- coding: utf-8 -*-

import glob
import os
import sys
import urllib2
import urlparse
from subprocess import call

from vleech.plugin import plugins

__all__ = ['main']

class Config(object):
    plugin_dir = '../siteplugins/'
    user_agent = 'Mozilla'

def err(msg):
    sys.stderr.write('ERROR: %s\n' % (msg,))
    sys.exit(1)

def warn(msg):
    sys.stderr.write('WARNING: %s\n' % (msg,))

def load_config():
    return Config()

def load_plugins(config):
    sys.path.insert(0, config.plugin_dir)
    for plugin in glob.glob(os.path.join(config.plugin_dir, '*.py')):
        __import__(os.path.basename(plugin)[:-3])
    sys.path.pop(0)

def make_video_filename(title, type):
    return title.lower().replace(' ', '_') + '.' + type

def main(argv):
    config = load_config()
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
    data = urllib2.urlopen(url).read()
    try:
        video_url, video_title, video_type = plugin.parse(url, data)
    except PluginError, e:
        err(str(e))
    print 'video url:', video_url
    print 'video title:', video_title
    video_file = make_video_filename(video_title, video_type)
    print 'filename:', video_file
    call(('curl', '-L', '-o', video_file, '-A', config.user_agent, video_url))
