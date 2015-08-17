def enableAlerts(self):
    """
    Enable all the alerts on the host

    :param self: The SDC instance
    """
    alerts = self.getAlerts()

    if len(alerts) < 1:
        print('No alerts available')
        return

    print('Enable all alerts\n')

    for alert in alerts['alerts']:
        alert['enabled'] = True         # Enable the alert

        id = alert.pop('id', None)      # Remove id because is already present in the URL
        alert.pop('targets', None)      # Remove target key as described in the api

        formatted = {'alert': alert}
        self.setAlert(formatted, id)

    self.printAlerts()                  # print all alerts
