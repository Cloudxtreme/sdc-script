Sysdig Cloud scripting library
===================

Python library that use the [Sysdig Cloud](https://sysdig.com/) API for run simple tasks on your host.


## Getting started

### Requirements

Python 3.x and pip3. That's all!

### Setup the environment

```
# Clone
git clone git@github.com:draios/sdc-script.git

# Enter
cd sdc-script

# Install
sudo pip3 install -r requirements.txt

# Verify
sdc

# ... and you're ready to go!
```

Make sure to re-install the library after you checkout the latest version of the library!


## Usage

Use your Sysdig Cloud credentials that you would use with the [web application](https://app.sysdigcloud.com).

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
* printAccessKey   Print the access key to stdout
* printAlerts      Print the alert list to stdout
* disableAlerts    Disable alerts
* enableAlerts     Enable alerts
```

You can access further documentation by running the following command:

```
sdc help <task name>
```
