Sysdig Cloud scripting library
===================

Python library that use the [Sysdig Cloud](https://sysdig.com/) API for run simple tasks on your host.


## Getting started

### Requirements

Python 3.x. That's all!

### Setup the environment

```
# Clone
git clone git@github.com:draios/sdc-script.git

# Enter
cd sdc-script

# Install
sudo python3 setup.py install

# Verify
sdc

# ... and you're ready to go!
```

Make sure to re-install the library after you checkout the latest version of the library!


## Usage

Use your Sysdig Cloud credentials that you would use with the [web application](https://www.app.sysdigcloud.com/).

```
sdc <username> <password>
```

By default the script will execute against the SaaS application at https://app.sysdigcloud.com. If you are using the on-premise version, you can specify your Sysdig Cloud server as follows:

```
sdc <username> <password> --server=http://my-local-sdc
```


### Tasks

On the command line you can specify one of the available tasks. To do so, simply specify the task name and parameters when required. For example:

```
sdc <username> <password> printAccessKey
```

Here is the list of tasks currently available:

```
* getUser          Get the user info             
* getAccessKey     Return the access key for the current user
* printAccessKey   Print the access key to stdout
* getAlerts        Get the alerts list of sysdigcloud
* disableAlerts    Disable all the alerts on the host
* enableAlerts     Enable all the alerts on the host
* setAlert         Set a single correctly formatted alerts
```

You can access further documentation by running the following command:

```
sdc help <task name>
```


### Custom scripts

The scripting library can be embedded in your custom scripts. Here is an example:

```
python
import sdc

session = sdc.SDC('username', 'password')   # Sysdig Cloud library instance
session.login()                             # Login to the SDC server

key = session.getAccessKey()                # Execute a task (e.g. to get the access key)

print('My key is: ' + key)

session.logout()                            # Make sure to logout before terminate the execution!
```
