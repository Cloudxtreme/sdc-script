def enableAlerts(self):
    """
    Enable all the alerts on the host

    :param self: The SDC instance
    """
    alerts = self.getAlerts()

    if len(alerts) < 1:
        print('No alerts available')
        return

    i = 0
    widths = [4, 4, 30, 40, 7]
    props = ['#', 'id', 'Name', 'When', 'Enabled']

    print('Enable all alerts\n')
    self._printTable(props, widths)
    self._printTable(['', '', '', ''], widths)

    for alert in alerts['alerts']:
        alert['enabled'] = True        # Enable the alert

        id = alert.pop('id', None)      # Remove id because is already present in the URL
        alert.pop('targets', None)      # Remove target key as described in the api

        formatted = {'alert': alert}
        self.setAlert(formatted, id)
        when = alert['type'].capitalize() + ': ' + alert['condition']

        props = [i + 1, int(id), alert['name'], when, str(alert['enabled'])]
        self._printTable(props, widths)
        i += 1
