import json


def getUser(self, user):
    """
    Get the user info
    :param user: Current username
    :return: The request object
    """
    if self.auth is None:
        raise Exception('Login required')

    ret = self.auth.session.get(self.auth.host + '/user' + user)
    ret.raise_for_status()
    return json.loads(ret.text)
