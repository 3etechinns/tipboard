from src.tipboard.app.parser import get_config_names


class Flipboard(object):

    def __init__(self):
        self.last_found_configs_number = -1
        self.paths = list()

    def get_paths(self):
        """ Returns url paths to dashboards (created from .yaml config from userspace). """
        config_names = get_config_names()
        if len(config_names) != self.last_found_configs_number:
            self.paths = list()
            for name in config_names:
                self.paths.append('/' + name)
            self.last_found_configs_number = len(config_names)
        return self.paths
