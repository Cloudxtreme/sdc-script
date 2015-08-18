#!/usr/bin/env python3
import argparse
import sys
import sdc

__doc__ = '''Sysdig Cloud scripting library (python)

Usage: sdc <username> <password> [--server=https://my-local-sdc] <task name> [task parameters]

Example: sdc <username> <password> printAccessKey


Notes:
<username> and <password> are your Sysdig Cloud credentials.

If you don't specify a server, the script will use the SaaS server at https://app.sysdigcloud.com.


Tasks:

* printAccessKey   Print the access key to stdout
* printAlerts      Print the alerts list to stdout
* disableAlerts    Disable all the alerts on the host
* enableAlerts     Enable all the alerts on the host

Run sdc help <task name> for further information.


For more information and examples, refer to the online documentation at https://github.com/draios/sdc-script.'''

DEFAULT_SERVER = 'https://app.sysdigcloud.com/'

tasks = [f for _, f in sdc.tasks.__dict__.items() if callable(f)]
tasksNames = [t.__name__ for t in tasks]

if len(sys.argv) >= 4:
    parser = argparse.ArgumentParser(description='Sysdigcloud command line script')
    parser.add_argument('-s', '--server',
                        help='Sysdigcloud server',
                        default=DEFAULT_SERVER)
    parser.add_argument('username', type=str, help='Sysdigcloud username')
    parser.add_argument('password', type=str, help='Sysdigcloud password')
    parser.add_argument('task', type=str, help='Task to perform')
    args = parser.parse_args()

    if args.task in tasksNames:
        session = sdc.SDC(args.username, args.password, server=args.server)
        session.login()

        eval('session.' + args.task + '()',
             {},            # Globals dict arguments for use inside the evaluated function
             {'session': session})  # sdc instance for use the API

        session.logout()
    else:
        print(__doc__)
elif len(sys.argv) == 3 and sys.argv[1] == 'help':
    # Help mode
    task = sys.argv[2]
    if task in tasksNames:
        # Print the task documentation
        index = tasksNames.index(task)
        print(tasks[index].__doc__.strip().split('\n', 1)[0])
    else:
        print('Task not found')
else:
    print(__doc__)
