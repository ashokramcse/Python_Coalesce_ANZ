'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
#python installchilkat.py -g
import sys

import chilkat

#  This example assumes Chilkat SSH/SFTP to have been previously unlocked.


ssh = chilkat.CkSsh()
ssh.UnlockComponent("test.rebex.net")
port = 22    

success = ssh.Connect("test.rebex.net",port)

if (success != True):
    print(ssh.lastErrorText())
    sys.exit()
print("entering server...")
#  Authenticate using login/password:
success = ssh.AuthenticatePw("demo","password")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Send some commands and get the output.
strOutput = ssh.quickCommand("df","ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print("---- df ----")
print(strOutput)

strOutput = ssh.quickCommand("echo hello world","ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print("---- echo hello world ----")
print(strOutput)

strOutput = ssh.quickCommand("date","ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print("---- date ----")
print(strOutput)
