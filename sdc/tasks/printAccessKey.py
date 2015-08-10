def printAccessKey(self):
    """
    Print the access key to stdout
    """
    key = self.getAccessKey()
    if key:
        print('accessKey: ' + key)
    else:
        print('No access key available')
