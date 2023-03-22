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
        # Show Inventory
        command1 = "show inventory"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('INVENTORY')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show Firmware
        command2 = "show version | i image"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('FIRMWARE CHECK')
        print()
        print(output)
        print()
        print('################################################################################')

for devices in core_switch_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        # Show Inventory
        command1 = "show inventory"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('INVENTORY')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show Firmware
        command2 = "more flash:packages.conf | i Build"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('FIRMWARE CHECK')
        print()
        print(output)
        print()
        print('################################################################################')

for devices in access_switch_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()
        # Show Inventory
        command1 = "show inventory"
        output = net_connect.send_command(command1)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('INVENTORY')
        print()
        print(output)
        print()
        print('################################################################################')
		
		# Show Firmware
        command2 = "show version | i image"
        output = net_connect.send_command(command2)

                # Automatically cleans-up the output so that only the show output is returned
        print('################################################################################')
        print(net_connect.find_prompt())
        print()
        print('FIRMWARE CHECK')
        print()
        print(output)
        print()
        print('################################################################################')