import subprocess
from sys import exit
import argparse
import re

parser = argparse.ArgumentParser(description="Utility for change the MAC address")
parser.add_argument("-i", "--interface", dest="interface", default="eth0", help="Interface to change a MAC address")
parser.add_argument("-m", "--mac", dest="new_mac", default="00:11:22:33:44:55", help="New MAC address to change")
args = parser.parse_args()

try:
    old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(subprocess.check_output(f"ifconfig {args.interface}", shell=True)))
except subprocess.CalledProcessError:
    print(f"[-] MAC address couldn't read for {args.interface}")
    exit()

if args.interface == "eth0" and args.new_mac == "00:11:22:33:44:55":
	print("[+] Use the default values for interface(eth0) and MAC(00:11:22:33:44:55)")

print(f"[+] Changing MAC adress for {args.interface} from {old_mac.group(0)} to {args.new_mac}")

subprocess.call(f"ifconfig {args.interface} down", shell=True)
subprocess.call(f"ifconfig {args.interface} hw ether {args.new_mac}", shell=True)
subprocess.call(f"ifconfig {args.interface} up", shell=True)
