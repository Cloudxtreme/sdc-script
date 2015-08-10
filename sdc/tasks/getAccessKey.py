def getAccessKey(self):
    """
    Return the access key for the current user

    :param self: The SDC instance
    """
    user = self.getUser('/me')
    return user['user']['accessKey']
