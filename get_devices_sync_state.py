#!/usr/bin/python3

######################################################################################################
## Purpose: Get F5 Device statuses
## By Guru Palanisamy 
## Usage: get_devices_sync_state -u user_id -f devices.lst 
##
## -------- -------- ----------------------------
## Date:    Initials Comments
## -------- -------- ----------------------------
## 20210204 Guru P   New Script Added 
######################################################################################################

from __future__ import absolute_import, print_function
import sys
import os
import argparse
import getpass
import bigsuds
from pprint import pprint

## Make Python 2 work as Python 3
try:
    input = raw_input
except NameError:
    pass

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('-u', '--user', help='F5 User name', required=False)
my_parser.add_argument('-p', '--password', help='F5 Password', required=False)
my_parser.add_argument('-f', '--file', help='Input file with device hostnames or Management IPs one per line', required=False)

# Execute the parse_args() method
args = my_parser.parse_args()
ltm_list = ['']

if args.user:
    ltm_user=args.user
else:
    ltm_user=input("Username: ")

if args.password:
    ltm_password=args.password
else:
    ltm_password=getpass.getpass("Password: ")

if args.file:
    if not os.path.exists(args.file):
        print(f"Input file '{args.file}' doesn't exist")
        sys.exit(1)
    else:
        ltm_list = open(args.file, 'r').read().splitlines()
else:
    ltm_list[0] = input("F5 Device IP or hostname:")

with open('output.csv', 'w+') as outfile:
    outfile.write("Device,Version,Role,Sync,State,Comments\n")
    for ltm in ltm_list:
        b = bigsuds.BIGIP(ltm, ltm_user, ltm_password)
        try:
            ver = b.System.SystemInfo.get_version()
            ha_state=b.System.Failover.get_failover_state().replace('FAILOVER_STATE_','')
            f5state=b.Management.DeviceGroup.get_sync_status_overview()
            if ha_state == 'STANDBY':
                f5state['status']=''
                f5state['details']=['']
            print(f"{ltm}, {ver}, {ha_state}, {f5state['status']}, {''.join(f5state['details'])}")
            outfile.write(f"{ltm}, {ver}, {ha_state}, {f5state['status']}, {''.join(f5state['details'])}\n")

        except Exception as ex:
            print("Error: unable to connect to " + ltm + ". Skipping")

sys.exit(0)
######## End of Script ########
