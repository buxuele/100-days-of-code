import os
import nmap
import subprocess

"""
scan res:
    hostnames:  192.168.8.1
    hostnames:  192.168.8.2
    hostnames:  192.168.8.104
    hostnames:  192.168.8.107
    hostnames:  192.168.8.108
    hostnames:  192.168.8.111
"""

def scan_network():
    scanner = nmap.PortScanner()    # init

    myIP = subprocess.check_output(['hostname -I'], shell=True)
    myIP = str(myIP, 'utf-8').split('.')
    print(myIP)     # get some ip(s)

    scanner_data = scanner.scan(hosts='.'.join(myIP[:3]) + '.1/24', arguments='-sP')

    print("**"*10)

    print(scanner.command_line())
    print(scanner.scaninfo())
    print(scanner.all_hosts())      # == scanData
    print(scanner['192.168.8.1'].hostname())    # _gateway
    print(scanner['192.168.8.1'].state())    #  up
    print(scanner['192.168.8.1'].all_protocols())    # []
    # print(scanner['192.168.8.111']['tcp'].keys())    #

    print(scanner.csv())

    print("**"*10)

    for ht in scanner_data['scan']:
        print("hostname: ", ht)


scan_network()
