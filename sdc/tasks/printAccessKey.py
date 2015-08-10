def printAccessKey(self):
    """
    Print the access key to stdout

    :param self: The SDC instance
    """
    key = self.getAccessKey()
    if key:
        print('accessKey: ' + key)
    else:
        print('No access key available')
