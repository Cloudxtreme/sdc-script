import sys
from . import tasks
from .api import Api

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
        self.api = Api(host, username, password)
        self.api.login()

    def getAccessKey(self):
        """
        Return the accessKey retrivied from the server
        :return: access key string
        """
        return tasks.getAccessKey(self.api)

    def printAccessKey(self):
        """
        Print the access key to stdout
        """
        print('accessKey: ' + self.getAccessKey())

    def enableAlerts(self):
        """
        Enable all the alerts on the host
        """
        tasks.enableAlerts(self.api)

    def disableAlerts(self):
        """
        Disable all the alert on the host
        """
        tasks.disableAlerts(self.api)

    def logout(self):
        """
        Close the current session on sysdigcloud
        """
        self.api.logout()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('USAGE %s\n' % sys.argv[0])
    else:
        api = Api(DEFAULT_HOST, username=sys.argv[1], password=sys.argv[2])
        req = api.login()
        req = api.getAlerts()
        print(req.text)
        req = api.logout()

