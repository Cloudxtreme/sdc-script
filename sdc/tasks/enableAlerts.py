def enableAlerts(self):
    """
    Enable all the alerts on the host

    :param auth: The api dictionary with a session opened
    :return: The request dictionary
    """
    alerts = self.getAlerts()

    if len(alerts) < 1:
        print('No alerts available')
        return

    i = 0
    widths = [10, 10, 60, 10]

    printTable = lambda a, w: print('| ' + ' | '.join('{:{}}'.format(x, w[i])
                                    for i, x in enumerate(a)) + ' |')

    print('Enable all alerts\n')
    props = ['#', 'id', 'alert name', 'enabled']
    printTable(props, widths)
    printTable(['', '', '', ''], widths)

    for alert in alerts['alerts']:
        alert['enabled'] = True        # Enable the alert

        id = alert.pop('id', None)      # Remove id because is already present in the URL
        alert.pop('targets', None)      # Remove target key as described in the api

        formatted = {'alert': alert}
        self.setAlert(formatted, id)

        props = [str(i + 1), str(id), alert['name'], str(alert['enabled'])]
        printTable(props, widths)

        i += 1
