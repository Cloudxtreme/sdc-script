import json


def disableAlerts(api):
    """
    Disable all the alerts on the host

    :param api: The api object with a session opened
    :return: The request object
    """
    alerts = json.loads(api.getAlerts())
    i = 0
    widths = [10, 10, 60, 10]

    printTable = lambda a, w: print('| ' + ' | '.join('{:{}}'.format(x, w[i])
                                    for i, x in enumerate(a)) + ' |')

    print('Disable all alerts\n')
    props = ['#', 'id', 'alert name', 'enabled']
    printTable(props, widths)
    printTable(['', '', '', ''], widths)

    for alert in alerts['alerts']:
        alert['enabled'] = False        # Disable the alert

        id = alert.pop('id', None)      # Remove id because is already present in the URL
        alert.pop('targets', None)      # Remove target key as described in the api

        formatted = {'alert': alert}
        ret = api.setAlert(formatted, id)

        props = [str(i + 1), str(id), alert['name'], str(alert['enabled'])]
        printTable(props, widths)

        i += 1
