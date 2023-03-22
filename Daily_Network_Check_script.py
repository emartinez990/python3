#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco_fw1 = {
            "device_type": "cisco_ios",
                "ip": "<ip_address>",
                    "username": "<username>",
                        "password": "<password>",
                            "secret": "<password>"
                            }
							
cisco_fw2 = {
            "device_type": "cisco_ios",
                "ip": "<ip_address>",
                    "username": "<username>",
                        "password": "<password>",
                            "secret": "<password>"
                            }

cisco_core_sw = {
            "device_type": "cisco_ios",
                "ip": "<ip_address>",
                    "username": "<username>",
                        "password": "<password>",
                            "secret": "<password>"
                            }
cisco_sw1 = {
            "device_type": "cisco_ios",
            "host": "LU-ACSW01-500N",
            "ip": "<ip_address>",
            "username": "<username>",
            "password": "<password>",
            "secret": "<password>"  
                            }
cisco_sw2 = {
            "device_type": "cisco_ios",
                "ip": "<ip_address>",
                    "username": "<username>",
                        "password": "<password>",
                            "secret": "<password>"
                            }

firewall_devices = [cisco_fw1, cisco_fw2]
core_switch_devices = [cisco_core_sw]
access_switch_devices = [cisco_sw1, cisco_sw2]

for devices in firewall_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        # Show route
        command1 = "show route"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('ROUTING TABLE')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show crypto ikev2
        command2 = "show crypto ikev2 sa"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('TUNNEL TO BOSTON (CNC)')
        print()
        print(output)
        print()
        print('################################################################################')

for devices in core_switch_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        # Show ip route
        command1 = "show ip route"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('ROUTING TABLE')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show interfaces err-disabled
        command2 = "show cdp neighbor"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('CDP NEIGHBORS')
        print()
        print(output)
        print()
        print('################################################################################')

for devices in access_switch_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        # Show port-security
        command1 = "show port-security"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('PORT-SECURITY')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show interfaces err-disabled
        command2 = "show interface status err-disabled"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('ERR-DISABLED INTERFACES')
        print()
        print(output)
        print()
        print('################################################################################')
        
		# Show CDP Neighbors
        command3 = "show cdp neighbor"
        output = net_connect.send_command(command3)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('CDP NEIGHBORS')
        print()
        print(output)
        print()
        print('################################################################################')