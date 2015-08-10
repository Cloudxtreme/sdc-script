import requests
import json


class Session:
    HEADERS = {'Content-type': 'application/json; charset=UTF-8'}

    def __init__(self,
                 host,
                 username=None,
                 password=None):
        """
        Creare an api object that used the passed host
        :param host: The sysdigcloud host
        :param username: The sysdigcloud username
        :param password: The sysdigcloud password
        :return:
        """
        self.host = host
        self.session = requests.Session()
        self.setCredentials(username, password)

    def setCredentials(self,
                       username,
                       password):
        """
        Set the credentials necessary for the auth
        :param username: username on sysdigcloud
        :param password: password on sysdigcloud
        :return:
        """
        self.username = username
        self.password = password

    def login(self):
        """
        Open a new session on sysdigcloud
        :return: The request object
        """
        if self.username and self.password and self.session:
            payload = {'username': self.username, 'password': self.password}
            ret = self.session.post(self.host + '/login',
                                    data=json.dumps(payload),
                                    headers=self.HEADERS)
            ret.raise_for_status()
            return ret
        else:
            raise Exception('Credentials not currently set')

    def logout(self):
        """
        Close the current session on sysdigcloud
        :return: The request object
        """
        if self.session:
            ret = self.session.post(self.host + '/logout')
            return ret
        else:
            raise Exception('Session in not currently open')
