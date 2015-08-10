import json


def setAlert(self, alert, id):
    """
    Set a single correctly formatted alerts
    :param alert: The formatted alert object
    :param id: The alert id
    :return: The request object
    """
    if self.auth is None:
        raise Exception('Login required')

    if isinstance(alert, dict) and isinstance(id, int):
        ret = self.auth.session.put(
            self.auth.host + '/alerts/' + str(id),
            headers=self.auth.HEADERS,
            data=json.dumps(alert))
        ret.raise_for_status()
        return ret
    else:
        raise Exception('Alert in not valid')
