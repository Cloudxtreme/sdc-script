Sysdig Cloud Scripting Library
===================

The Sysdig Cloud Scripting Library is a python based library that utilizes the Sysdig Cloud API to perform useful tasks on your Sysdig Cloud agent enabled host. Use the scripts from the the Linux shell to control certain features such as alerting or to access information from your Sysdig Cloud account such as your access key number. 

The library will be continually updated and expanded with new commands over time

### Requirements

To use the Sysdig Cloud Scripting Library your host needs Python 3.x installed. To setup the environment you will need git and pip3 installed as well.

###Setup Your Environment

Install git and clone the script repository:
```
sudo apt-get install git
sudo git clone git@github.com:draios/sdc-script.git
```

Enter the scripting folder and install the environment:
```
cd sdc-script
sudo python3 setup.py install
```

Install additional dependencies via pip3
```
sudo apt-get install python3-pip
sudo pip3 install -r requirements.txt
```

Now verify everything is installed and working with:
```
sdc
```

You should see Sysdig Cloud scripting library usage information.

Make sure to re-install the library after you checkout the latest version!


### Usage

Use your Sysdig Cloud credentials that you would with the web application in the following format for each task:
```
sdc <username> <password> <task>
```
Example:
```
sdc joe@sysdig.com  mypasswd  printAccessKey
```

By default the script will execute against the SaaS application at https://app.sysdigcloud.com. If you are using the on-premises version, you can specify your Sysdig Cloud server as follows:
```
sdc <username> <password> --server=https://my-local-sdc-svr <task>
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
