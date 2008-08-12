# -*- coding: utf-8 -*-
'''plugin-foo

just inherit from vleech.plugin.Plugin
and implement the parse(self, url, data) method.
'''

__all__ = ['PluginError', 'plugins', 'Plugin']

class PluginError(Exception):
    pass

# global plugin registry
plugins = dict()


class MetaPlugin(type):
    'meta class to automatically register plugins with the plugin registry'

    def __init__(cls, name, bases, dic):
        if name != 'Plugin': # do not do this for the main Plugin class
            if not hasattr(cls, 'site'):
                raise PluginError('plugin class %s does not have a "site" attribute!' % name)
            plugins[cls.site] = cls
        super(MetaPlugin, cls).__init__(name, bases, dic)


class Plugin(object):
    'base class for all plugins'

    __metaclass__ = MetaPlugin

    def parse(self, url, data):
        'parse a video page and return a (video_url, video_title, video_type) tuple'
        raise NotImplementedError('every plugin must implement a parse(url, data) method')

    # helper methods

    def _data_search(self, regexp, data, error=''):
        'search data for re, raise PluginError if not found, else return group 1'
        if isinstance(regexp, basestring):
            regexp = re.compile(regexp, re.M)
        m = regexp.search(data)
        if m is None:
            raise PluginError(error)
        return m.group(1)

    
            
    
