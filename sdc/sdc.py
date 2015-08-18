import sys
from types import MethodType
from . import tasks
from .session import Session

DEFAULT_SERVER = 'https://app.sysdigcloud.com'


class SDC:
    """
        SysdigCloud main class for the sdc library
    """
    def __init__(self, username=None, password=None,
                 server=DEFAULT_SERVER):
        """
        Create a new Api instance and open a new session

        :param username: username on sysdigcloud
        :param password: password on sysdigcloud
        :param host: custom host
        """
        for _, function in tasks.__dict__.items():
            if callable(function):
                handler = MethodType(function, self)
                setattr(self.__class__, function.__name__, handler)

        self.username = username
        self.password = password
        self.server = server
        self.auth = None

    def login(self, username=None, password=None, server=None):
        if username is None:
            username = self.username
        if password is None:
            password = self.password
        if server is None:
            server = self.server

        if not server.startswith('http'):
            # add https if not present
            server = 'https://' + server
        server += '/api'    # api endpoint

        if username is None or password is None:
            raise Exception('Username and password are required for authentication')

        self.auth = Session(server, username, password)
        self.auth.login()

    def logout(self):
        """
        Close the current session on sysdigcloud
        """
        self.auth.logout()

    def _printTable(self, props, widths):
        """
        Print a table with 4 props
        :param props: properties to print []
        :param widths: widths for each column []
        """
        for i, prop in enumerate(props):
            if isinstance(prop, str):
                # string formatting
                props[i] = prop if len(prop) <= widths[i] else prop[:widths[i] - 3] + '...'
        print('| ' + ' | '.join('{:{}}'.format(x, widths[i])
                                for i, x in enumerate(props)) + ' |')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('USAGE %s\n' % sys.argv[0])
    else:
        auth = Session(DEFAULT_HOST, username=sys.argv[1], password=sys.argv[2])
        req = auth.login()
        req = auth.getAlerts()
        print(req.text)
        req = auth.logout()

