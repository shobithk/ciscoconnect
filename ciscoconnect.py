import pexpect
import sys
import time  #Only needed if you use time.sleep for pause between command  outputs

telnethost="routername"   # Router hostname or ip address
user = "testuser"   # username
password = "testpass"   # password
command1="terminal len 0"
command2="show clock"
command3="show version"
command4="exit"

child = pexpect.spawn ('telnet '+ telnethost)
child.logfile = sys.stdout

child.expect ('username:')
child.sendline (user)
child.expect ('password:')
child.sendline (password)
child.expect ('RouterName#')   # Substitute the RouterName with your actual device name prompt
child.sendline(command1)
child.expect ('RouterName#')   # Substitute the RouterName with your actual device name prompt
child.sendline(command2)
child.expect ('RouterName#')   # Substitute the RouterName with your actual device name prompt
child.sendline (command3)
time.sleep(60)   # Optional if you need a pause in command execution time In seconds. 
child.expect ('RouterName#')   # Substitute the RouterName with your actual device name prompt
child.sendline(command4)
