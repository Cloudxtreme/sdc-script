Python SDC Library
===================

Python library that use the [Sysdig Cloud](https://sysdig.com/) API for run simple tasks on your host.

## INSTALLATION

The python library currently requires the requests library installed in your python environment. 
```
sudo python3 setup.py install
```

## USAGE

The python executable script `sdc` provide a command line interface that you can use for simply run a task

```
Usage:
    sdc username password [host] task
    sdc help task
    sdc help
```

Use the script with your `username` and `password` for run a task on your [Sysdig Cloud](https://sysdig.com/) account.
The default host is `https://app.sysdigcloud.com/` , but you can specify a custom host. 
Pay attention to use the correct url with an `https://` connection for avoid errors.

List of tasks available:

* getAccessKey                  Return the access key for the current user
* setAlert                      Set a single correctly formatted alerts
* enableAlerts                  Enable all the alerts on the host
* getAlerts                     Get the alerts list of sysdigcloud
* getUser                       Get the user info             
* printAccessKey                Print the access key to stdout
* disableAlerts                 Disable all the alerts on the host

In alternative you could use `sdc` python library for create your custom tasks.

### Example

```python
import sdc

session = sdc.SDC('username', 'password')       # new sdc instance
session.login()                                 # login to your account use the credentials

key = session.getAccessKey()                    # retrieve the access key

print('My key is: ' + key)

session.logout()                                # logout and close the session
```