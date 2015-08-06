import json


def getAccessKey(api):
    """
    Return the access key for the current user

    :param api: The api object with a session opened
    """
    user = json.loads(api.getUser('/me'))
    return user['user']['accessKey']
