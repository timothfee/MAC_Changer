#!/usr/bin/env python

import subprocess

interface = input("What interface MAC would you like to change: ")
MAC = input("Enter the new MAC address: ")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {MAC}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"Interface successfully changed to {MAC}")
