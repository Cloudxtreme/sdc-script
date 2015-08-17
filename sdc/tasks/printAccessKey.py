def printAccessKey(self):
    """
    Print the access key to stdout

    :param self: The SDC instance
    """
    user = self.getUser('/me')
    key = user['user']['accessKey']
    if key:
        print(key+'\n')
    else:
        print('No access key available')
