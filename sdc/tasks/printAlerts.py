def printAlerts(self):
    """
    Print the alerts list to stdout

    :param self: The SDC instance
    """
    alerts = self.getAlerts()

    widths = [4, 4, 30, 40, 7]
    props = ['#', 'id', 'Name', 'When', 'Enabled']

    print('Alerts list\n')
    self._printTable(props, widths)
    self._printTable(['', '', '', '', ''], widths)

    i = 0
    for alert in alerts['alerts']:
        when = alert['type'].capitalize() + ': ' + alert['condition']
        props = [i + 1, int(alert['id']), alert['name'], when, str(alert['enabled'])]
        self._printTable(props, widths)
        i += 1
