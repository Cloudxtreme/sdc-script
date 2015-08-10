def getAccessKey(self):
    """
    Return the access key for the current user

    :param api: The api object with a session opened
    """
    user = self.getUser('/me')
    return user['user']['accessKey']
