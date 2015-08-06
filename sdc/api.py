import requests
import json

class Api():
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
        self.session = None
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
        if self.username and self.password:
            payload = {'username': self.username, 'password': self.password}
            ret = requests.post(self.host + '/login',
                                data=json.dumps(payload),
                                headers=self.HEADERS)
            ret.raise_for_status()
            self.session = ret.cookies
            return ret
        else:
            raise Exception('Credentials not currently set')

    def logout(self):
        """
        Close the current session on sysdigcloud
        :return: The request object
        """
        if self.session:
            ret = requests.post(self.host + '/logout', cookies=self.session)
            return ret
        else:
            raise Exception('Session in not currently open')

    def getAlerts(self):
        """
        Get the alerts list of sysdigcloud
        :return: List of alerts objects
        """
        if self.session:
            ret = requests.get(self.host + '/alerts', cookies=self.session)
            ret.raise_for_status()
            return ret.text
        else:
            raise Exception('Session in not currently open')

    def setAlert(self, alert, id):
        """
        Set a single correctly formatted alerts
        :param alert: The formatted alert object
        :param id: The alert id
        :return: The request object
        """
        if self.session:
            if isinstance(alert, dict):
                ret = requests.put(self.host + '/alerts/' + str(id),
                                   headers=self.HEADERS,
                                   data=json.dumps(alert),
                                   cookies=self.session)
                ret.raise_for_status()
                return ret
            else:
                raise Exception('Alert in not valid')
        else:
            raise Exception('Session in not currently open')

    def getUser(self, user):
        """
        Get the user info
        :param user: Current username
        :return: The request object
        """
        if self.session:
            ret = requests.get(self.host + '/user' + user,
                               cookies=self.session)
            ret.raise_for_status()
            return ret.text
        else:
            raise Exception('Session in not currently open')