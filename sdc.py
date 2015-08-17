#!/usr/bin/env python3
import argparse
import sys
import sdc

"""
SDC command line utility for easily run a task on your sysdigcloud account.
The script needs an username and a password for login inside your account.
You can also specify a custom server address using --server.
Run the help for the a list of current supported tasks.

Usage:
    sdc username password task --server=server
    sdc help task
    sdc help
"""

DEFAULT_HOST = 'https://app.sysdigcloud.com/'

tasks = [f for _, f in sdc.tasks.__dict__.items() if callable(f)]
tasksNames = [t.__name__ for t in tasks]

if len(sys.argv) >= 4:
    parser = argparse.ArgumentParser(description='Sysdigcloud command line script')
    parser.add_argument('-s', '--server',
                        help='Sysdigcloud server',
                        default=DEFAULT_HOST)
    parser.add_argument('username', type=str, help='Sysdigcloud username')
    parser.add_argument('password', type=str, help='Sysdigcloud username')
    parser.add_argument('task', type=str, help='Task to perform')
    args = parser.parse_args()

    if args.task in tasksNames:
        session = sdc.SDC(args.username, args.password, host=args.server)
        session.login()

        eval('session.' + args.task + '()',
             {},            # Globals dict arguments for use inside the evaluated function
             {'session': session})  # sdc instance for use the API

        session.logout()
    else:
        # Print a documentation message
        print('Currently supported tasks: ' + (', '.join(tasksNames)))
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
    print('Usage:\n\tsdc username password task --server=server\n\tsdc help task\n\tsdcs help')
    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print('\nList of tasks available:\n')
        for task in tasksNames:
            index = tasksNames.index(task)
            doc = tasks[index].__doc__.strip().split('\n', 1)[0]
            print(''.join('{:{}}'.format(x, 30) for _, x in enumerate([task, doc])))
