import sys
from types import MethodType
from . import tasks
from .session import Session

DEFAULT_HOST = 'https://app.sysdigcloud.com'


class SDC:
    """
        SysdigCloud main class for the sdc library
    """
    def __init__(self, username=None, password=None,
                 host=DEFAULT_HOST):
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
        self.host = host
        self.auth = None

    def login(self, username=None, password=None, host=None):
        if username is None:
            username = self.username
        if password is None:
            password = self.password
        if host is None:
            host = self.host

        if username is None or password is None:
            raise Exception('Username and password are required for authentication')

        self.auth = Session(host, username, password)
        self.auth.login()

    def logout(self):
        """
        Close the current session on sysdigcloud
        """
        self.auth.logout()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('USAGE %s\n' % sys.argv[0])
    else:
        auth = Session(DEFAULT_HOST, username=sys.argv[1], password=sys.argv[2])
        req = auth.login()
        req = auth.getAlerts()
        print(req.text)
        req = auth.logout()

