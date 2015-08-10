#!/usr/bin/env python3
import sys
import sdc

"""
SDC command line utility for easily run a task on your sysdigcloud account.
The script needs an username and a password for login inside your account.
You can also specify a custom host address.
Run the help for the a list of current supported tasks.

Usage:
    sdc username password [host] task
    sdc help task
    sdc help
"""

DEFAULT_HOST = 'https://app.sysdigcloud.com/'

tasks = [f for _, f in sdc.tasks.__dict__.items() if callable(f)]
tasksNames = [t.__name__ for t in tasks]

if len(sys.argv) >= 4:

    if len(sys.argv) == 5:
        host = sys.argv[3]
        task = sys.argv[4]
    else:
        host = DEFAULT_HOST
        task = sys.argv[3]

    if task in tasksNames:
        session = sdc.SDC(sys.argv[1], sys.argv[2], host=host)
        session.login()

        eval('session.' + task + '()',
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
    print('Usage:\n\t%(arg)s username password [host] task\n\t%(arg)s help task\n\t%(arg)s help' % {'arg': sys.argv[0]})
    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print('\nList of tasks available:\n')
        for task in tasksNames:
            index = tasksNames.index(task)
            doc = tasks[index].__doc__.strip().split('\n', 1)[0]
            print(''.join('{:{}}'.format(x, 30) for _, x in enumerate([task, doc])))
