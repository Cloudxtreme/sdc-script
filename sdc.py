import sys
import sdc

DEFAULT_HOST = 'https://app-staging.sysdigcloud.com/api'

if __name__ == '__main__':
    tasks = ['printAccessKey', 'enableAlerts', 'disableAlerts']

    if len(sys.argv) == 4:
        # Task mode
        task = sys.argv[3]

        if task in tasks:
            sdc = sdc.SDC(sys.argv[1], sys.argv[2], host=DEFAULT_HOST)

            eval('sdc.' + task + '()',
                 {},            # Globals dict arguments for use inside the evaluated function
                 {'sdc': sdc})  # sdc instance for use the API

            sdc.logout()
        else:
            # Print a documentation message
            print('Currently supported tasks: ' + (', '.join(tasks)))
    elif len(sys.argv) == 3 and sys.argv[1] == 'help':
        # Help mode
        task = sys.argv[2]
        if task in tasks:
            # Print the task documentation
            print(getattr(sdc.SDC, task).__doc__.strip())
        else:
            print('Task not found')
    else:
        print('Usage:\n\tpython %(arg)s username password task\n\tpython %(arg)s help task\n\tpython %(arg)s help' % {'arg': sys.argv[0]})
        if len(sys.argv) == 2 and sys.argv[1] == 'help':
            print('\nList of tasks available:\n')
            for task in tasks:
                print('\t' + task + '\t' + getattr(sdc.SDC, task).__doc__.strip())
