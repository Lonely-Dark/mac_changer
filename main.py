from subprocess import call, check_output, CalledProcessError
from sys import exit
from argparse import ArgumentParser
from re import search

def parse_args():
    parser = ArgumentParser(description="Utility for change the MAC address")
    parser.add_argument("-i", "--interface", dest="interface", default="eth0", help="Interface to change a MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", default="00:11:22:33:44:55", help="New MAC address to change")
    args = parser.parse_args()
    
    if args.interface == "eth0" and args.new_mac == "00:11:22:33:44:55":
	    print("[+] Use the default values for interface(eth0) and MAC(00:11:22:33:44:55)")
    
    return args

def get_mac(interface):
    try:
        mac = search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(check_output(f"ifconfig {interface}", shell=True)))
    except CalledProcessError:
        print(f"[-] MAC address couldn't read for {interface}")
        exit()
        
    return mac.group(0)

def change_mac(interface, mac):
    print(f"[+] Changing MAC adress for {interface} from {get_mac(interface)} to {mac}")
    
    call(f"ifconfig {interface} down", shell=True)
    call(f"ifconfig {interface} hw ether {mac}", shell=True)
    call(f"ifconfig {interface} up", shell=True)
    
args = parse_args()

change_mac(args.interface, args.new_mac)
