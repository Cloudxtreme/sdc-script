import tabulate

def printAlerts(self):
    """
    Print the alerts list to stdout

    :param self: The SDC instance
    """
    alerts = self.getAlerts()

    props = ['#', 'Id', 'Name', 'Scope', 'When', 'Enabled']
    table = []

    i = 0
    for alert in alerts['alerts']:
        when = alert['type'].capitalize() + ': ' + alert['condition']
        filter = alert['filter'] if 'filter' in alert else ''
        table.append([i + 1, str(alert['id']), alert['name'], filter, when, str(alert['enabled'])])
        i += 1
    print(tabulate.tabulate(table, props, tablefmt='pipe'))
