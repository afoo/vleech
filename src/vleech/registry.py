'''plugin registry'''

class Registry(object):

    def __init__(self):
        self.plugins = list()

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def get_plugin_for_site(self, site):
        for plugin in self.plugins:
            if plugin.site in site:
                return plugin
        return None

plugins = Registry()
