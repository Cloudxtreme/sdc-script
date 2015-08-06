Python SDC Library
===================

Python library that use the [Sysdig Cloud](https://sysdig.com/) API for run simple tasks on your host

## Warning

Currently only python3 is supported, future updates will becomes soon

## USAGE

The python script `sdc.py` provide a command line interface that you can use for simply run a task

```
Usage:
    python sdc.py username password task
    python sdc.py help task
    python sdc.py help
```

Use the script with your `username` and `password` for run a task with your [Sysdig Cloud](https://sysdig.com/) account.

List of tasks available:

* `printAccessKey`	Print the access key to stdout
* `enableAlerts`	Enable all the alerts on the host
* `disableAlerts`	Disable all the alert on the host

## INSTALLATION

The python library currently requires the requests library installed in your python enviroment
```
python setup.py install
```