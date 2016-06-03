class CoreConfig:
    def __init__(self):
        self.prefix = '/usr/bin/mesos-master'

    def __str__(self):
        return self.prefix


class MasterConfig:
    def __init__(self, yaml_object):
        self.core_config = CoreConfig()
        self.core_config.prefix = yaml_object['core']['prefix']

    def __str__(self):
        return str(self.core_config)
