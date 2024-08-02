import pyfiglet
import sys
import socket
import ipaddress
from datetime import datetime

target = (input("What IP Address do you want to Scan?: "))

def validate_ip(target):
    try:
        ip_object = ipaddress.ip_address(target)
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
        print(ascii_banner)

        if len(sys.argv) == 2:
            target = socket.gethostbyname(sys.argv[1])
        else:
            print("Enter One IP Address or Website")

        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning Started at: " + str(datetime.now()))
        print("-" * 50)

        try:
            for port in range(1,100):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
                s.close()

        except KeyboardInterrupt:
            print("\n Exitting Scan" )
            sys.exit()
        except socket.gaierror:
            print("\n Hostname could not be Resolved.")
            sys.exit()
        except socket.error:
            print("\ Server not Responding")
            sys.exit()
    except ValueError:
        print("Invalid IP Address Provided")
        
validate_ip(target)