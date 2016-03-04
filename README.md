# Custom Port Scanner
This is a simple python script that will allow you to port scan a target

This is multi-threaded so it will create a new thread for each port. Currently there isn't support for stopping the threading beyond a certain point.

#Example
an example of how you can run this is as follows:

$> python port_scanner.py -H HOST_IP -p LIST OF PORTS

$> python port_scanner.py -H 192.168.XXX.XXX -p 1-500

or you can list ports individually

$> python port_scanner.py -H 192.168.XXX.XXXX -p 1 2 3 67 500

#What To Expect
This will clear your console and tell you that the scanner has begun. I will also list the ports it is currently scanning (based upon your input) and list all of the open ports that it found on the target. 
When the scanner is complete it will tell you how long it took to execute everything
