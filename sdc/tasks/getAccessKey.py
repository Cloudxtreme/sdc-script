import json


def getAccessKey(auth):
    """
    Return the access key for the current user

    :param api: The api object with a session opened
    """
    user = json.loads(auth.getUser('/me'))
    return user['user']['accessKey']
