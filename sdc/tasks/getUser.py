import json


def getUser(self, user):
    """
    Get the user info

    :param self: The SDC instance
    :param user: Username
    :return: The user info dictionary
    """
    if self.auth is None:
        raise Exception('Login required')

    ret = self.auth.session.get(self.auth.host + '/user' + user)
    ret.raise_for_status()
    return json.loads(ret.text)
