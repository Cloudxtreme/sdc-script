from __future__ import print_function
import sys
from . import tasks
from .session import Session

DEFAULT_HOST = 'https://app.sysdigcloud.com'


class SDC:
    """
        SysdigCloud main class for the sdc library
    """
    def __init__(self, username, password,
                 host=DEFAULT_HOST):
        """
        Create a new Api instance and open a new session

        :param username: username on sysdigcloud
        :param password: password on sysdigcloud
        :param host: custom host
        """
        if not username or not password:
            raise Exception('Username and password are needed for authentication')
        self.auth = Session(host, username, password)
        self.auth.login()

    def getAccessKey(self):
        """
        Return the accessKey retrivied from the server
        :return: access key string
        """
        return tasks.getAccessKey(self.auth)

    def printAccessKey(self):
        """
        Print the access key to stdout
        """
        print('accessKey: ' + self.getAccessKey())

    def enableAlerts(self):
        """
        Enable all the alerts on the host
        """
        tasks.enableAlerts(self.auth)

    def disableAlerts(self):
        """
        Disable all the alert on the host
        """
        tasks.disableAlerts(self.auth)

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

