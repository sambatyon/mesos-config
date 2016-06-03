import json

from io import StringIO

class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class CoreConfig:
    def __init__(self, yaml):
        if 'work_dir' not in yaml:
            raise ParseError('A working directory was not given.')

        self.prefix = yaml['prefix'] if 'prefix' in yaml else '/usr/bin/mesos-master'
        self.work_dir = yaml['work_dir']
        self.web_ui = yaml['web_ui'] if 'web_ui' in yaml else None
        self.cluster = yaml['cluster'] if 'cluster' in yaml else None
        self.hostname = yaml['hostname'] if 'hostname' in yaml else None
        self.hostname = yaml['hostname_lookup'] if 'hostname_lookup' in yaml else None

    def __str__(self):
        string = self.prefix
        string += ' \\\n    --work_dir=' + self.work_dir
        if self.web_ui:
            string += ' \\\n    --web_ui=' + self.web_ui
        if self.cluster:
            string += ' \\\n    --cluster=' + self.cluster
        return string


class SecurityConfig:
    def __init__(self, yaml):
        if 'credentials' in yaml:
            self.credentials = yaml['credentials']


    def __str__(self):
        string = ' '
        if type(self.credentials) is list:
            fp = StringIO()
            json.dump({'credentials':self.credentials}, fp)
            string += ' \\\n    --credentials=\'' + fp.getvalue() + '\''
        elif self.credentials.startswith('file://'):
            string += ' \\\n    --credentials=' + self.credentials
        else:
            string += ' \\\n    --credentials=file://' + self.credentials
        return string


class MasterConfig:
    def __init__(self, yaml):
        self.core = CoreConfig(yaml['core'])
        self.security = SecurityConfig(yaml['security'])

    def __str__(self):
        return '#!/usr/bin/env bash\n\n' + str(self.core) + str(self.security)
