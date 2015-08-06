import json


def disableAlerts(api):
    """
    Disable all the alerts on the host

    :param api: The api object with a session opened
    :return: The request object
    """
    alerts = json.loads(api.getAlerts())
    for alert in alerts['alerts']:
        alert['enabled'] = False        # Disable the alert

        id = alert.pop('id', None)      # Remove id because is already present in the URL
        alert.pop('targets', None)      # Remove target key as described in the api

        formatted = {'alert': alert}
        api.setAlert(formatted, id)
