import json


def getAlerts(self):
    """
    Get the alerts list of sysdigcloud

    :param self: The SDC instance
    :return: List of alerts dictionaries
    """
    if self.auth is None:
        raise Exception('Login required')

    ret = self.auth.session.get(self.auth.host + '/alerts')
    ret.raise_for_status()
    return json.loads(ret.text)
