import pyfiglet
import sys
import socket
import os 
import time 
import colorama 
from datetime import datetime
from colorama import Fore
   
os.system(' clear ')
print(Fore.RED+" [+] Starting Port Scanner ")
time.sleep(2)
os.system(' clear ') 
print("=" * 50)  
ascii_banner = pyfiglet.figlet_format("METAPORT")
print(ascii_banner)
   
if len(sys.argv) == 2:
      
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid ammount Argument")
  
print("+" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("+" * 50)
   
try:
      
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        result = s.connect_ex((target,port))
        if result ==0:
            print(Fore.BLUE+"Port {} is open".format(port))
        s.close()
          
except KeyboardInterrupt:
        os.system(' clear ')
        time.sleep(1)
        print(" [!] EXITING [!]")
        time.sleep(1)
        sys.exit()
except socket.gaierror:
        print("\n [!]Hostname Could Not Be Resolved[!]")
        sys.exit()
except socket.error:
        os.system(' clear ')
        time.sleep(1)
        print("\ Server is not giving resposes[!]")
        sys.exit()
except NameError:
        os.system(' clear ')
        time.sleep(1)
        print(" [!] TARGET WAS NOT DEFINED ")
        print(" [!] try python3 portscan.py [target] ")