#!/usr/bin/env python
'''
@author: Matthew C. Jones, CPA, CISA, OSCP
IS Audits & Consulting, LLC
TJS Deemer Dana LLP

Metasploit integration classes and modules
'''

import subprocess
import os

class msf_command:
    '''
    Parent command class for building and executing Metasploit framework commands
    '''

    def __init__(self):
        '''
        Constructor:
        '''
        self.command = ""
        self.commandArgs = ""
        self.newWindow = False
               
    def execute(self):
        '''
        Execute Metasploit command stored in .command property with arguments stored in
        .commandArgs property via subprocess
        '''
        
        if self.command == "":
            print("Error generating Metasploit command - no command attribute stored")
        else:
            #strCommand = os.path.join(get_msf_path(),self.command)+" "+self.commandArgs
            strCommand = os.path.join(get_msf_path(),self.command)
            if self.commandArgs != "":
                strCommand+=" "+self.commandArgs
            if self.newWindow == True:
                #TODO - fix command opening in new window option
                #subprocess.Popen(strCommand, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
                subprocess.Popen(strCommand, shell=True).wait()
            else:
                subprocess.Popen(strCommand, shell=True).wait()
        
class msfconsole_command(msf_command):
    '''
    Commands are built and piped via console similar to a resource file so multiple
    Handlers and exploits can be executed in a single thread
    
    command attribute should be a string with individual commands separated by ;
    parse_msfconsole_args builds this string from individual command strings passed as args
    '''
    
    def __init__(self,*commandLines):
        '''
        Constructor: if command arguments are passed at initialization they are passed to
        parse_msfconsole_args function and stored in the command attribute
        '''
        self.commandArgs = self.parse_msfconsole_args(*commandLines)
        self.command = "msfconsole -x"
        self.newWindow = False
        
    def parse_msfconsole_args(self,*commandLines):
        '''
        Build command attribute based on arguments passed and return as a string
        '''
        cmd = "'"                               #msfconsole -x needs command args in quotes
        for commandLine in commandLines[:]:     #cast args as a list and loop
            cmd += commandLine+";"
        cmd += "'"
        return cmd
    
    def add_msfconsole_args(self,*commandLines):
        '''
        Add additional msfconsole args to existing cmdArgs
        '''
        self.commandArgs = self.commandArgs[0:-1]   #strip ending single quote to add new args 
        for commandLine in commandLines[:]:         #cast args as a list and loop
            self.commandArgs += commandLine+";"
        self.commandArgs += "'"
        
def get_msf_path():
    '''
    Gets the path for Metasploit executable
    '''
    pathlist = []
    #add some default installation locations just in case the config file is wrong
    #TODO: Currently path options are hardcoded and OS specific - this needs to be fixed!!!
    pathlist.append ("/opt/framework3/msf3")
    pathlist.append ("/opt/framework/msf3")
    pathlist.append ("/opt/metasploit/msf3")
    pathlist.append ("/usr/share/metasploit-framework")
    #print pathlist
    
    for filepath in pathlist:
        if os.path.isfile(os.path.join(filepath,"msfconsole")):
            #print("msfconsole found at "+path)
            return filepath
    
    print ("Could not find metasploit path; we are going to try to call commands without path but this may not work!!!")
    return ""

if __name__ == '__main__':
    #self test code goes here!!!
    #get_msf_path()
    
    #spawn a test generic handler as a command
    myCommand = msfconsole_command("use exploit/multi/handler",
                                   "set PAYLOAD windows/meterpreter/reverse_https",
                                   "set LHOST 127.0.0.1",
                                   "set ExitOnSession false",
                                   "exploit -j")
    myCommand.newWindow = True
    myCommand.execute()
