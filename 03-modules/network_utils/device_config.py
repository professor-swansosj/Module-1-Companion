"""
Device Configuration Module

This module contains functions for configuring network devices.
It demonstrates how to create reusable configuration functions.
"""

from typing import Dict, List, Optional
import json
import os
from datetime import datetime


def configure_interface(hostname: str, interface: str, ip_address: str, 
                       subnet_mask: str, description: str = "") -> bool:
    """
    Configure a network interface on a device.
    
    Args:
        hostname (str): Device hostname
        interface (str): Interface name (e.g., 'GigabitEthernet0/0')
        ip_address (str): IP address to assign
        subnet_mask (str): Subnet mask in dotted decimal notation
        description (str): Optional interface description
        
    Returns:
        bool: True if configuration successful, False otherwise
    """
    print(f"Configuring {interface} on {hostname}:")
    print(f"  IP Address: {ip_address}")
    print(f"  Subnet Mask: {subnet_mask}")
    if description:
        print(f"  Description: {description}")
    
    # Simulate configuration commands
    config_commands = [
        f"interface {interface}",
        f"ip address {ip_address} {subnet_mask}",
        "no shutdown"
    ]
    
    if description:
        config_commands.insert(1, f"description {description}")
    
    print("Configuration commands:")
    for cmd in config_commands:
        print(f"  {cmd}")
    
    # In a real implementation, you would send these commands to the device
    print(f"✓ Interface {interface} configured successfully on {hostname}")
    return True


def configure_vlan(hostname: str, vlan_id: int, vlan_name: str, 
                  ports: Optional[List[str]] = None) -> bool:
    """
    Configure a VLAN on a switch.
    
    Args:
        hostname (str): Switch hostname
        vlan_id (int): VLAN ID number
        vlan_name (str): VLAN name
        ports (List[str]): List of ports to assign to VLAN
        
    Returns:
        bool: True if configuration successful, False otherwise
    """
    if ports is None:
        ports = []
    
    print(f"Configuring VLAN {vlan_id} on {hostname}:")
    print(f"  VLAN Name: {vlan_name}")
    print(f"  Ports: {', '.join(ports) if ports else 'None assigned'}")
    
    # Simulate VLAN configuration
    config_commands = [
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        "exit"
    ]
    
    # Configure ports if provided
    for port in ports:
        config_commands.extend([
            f"interface {port}",
            "switchport mode access",
            f"switchport access vlan {vlan_id}",
            "exit"
        ])
    
    print("Configuration commands:")
    for cmd in config_commands:
        print(f"  {cmd}")
    
    print(f"✓ VLAN {vlan_id} configured successfully on {hostname}")
    return True


def configure_ospf(hostname: str, process_id: int, router_id: str,
                  networks: List[Dict[str, str]]) -> bool:
    """
    Configure OSPF routing protocol on a router.
    
    Args:
        hostname (str): Router hostname
        process_id (int): OSPF process ID
        router_id (str): Router ID in IP address format
        networks (List[Dict]): List of network dictionaries with 'network' and 'area' keys
        
    Returns:
        bool: True if configuration successful, False otherwise
    """
    print(f"Configuring OSPF on {hostname}:")
    print(f"  Process ID: {process_id}")
    print(f"  Router ID: {router_id}")
    print("  Networks:")
    
    config_commands = [
        f"router ospf {process_id}",
        f"router-id {router_id}"
    ]
    
    for network in networks:
        net_addr = network['network']
        area = network['area']
        print(f"    {net_addr} area {area}")
        config_commands.append(f"network {net_addr} area {area}")
    
    config_commands.append("exit")
    
    print("Configuration commands:")
    for cmd in config_commands:
        print(f"  {cmd}")
    
    print(f"✓ OSPF configured successfully on {hostname}")
    return True


def backup_configuration(hostname: str, config_type: str = "running",
                        backup_dir: str = "backups") -> Optional[str]:
    """
    Backup device configuration to a file.
    
    Args:
        hostname (str): Device hostname
        config_type (str): Type of config to backup ('running' or 'startup')
        backup_dir (str): Directory to store backup files
        
    Returns:
        Optional[str]: Path to backup file if successful, None otherwise
    """
    try:
        # Create backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)
        
        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{hostname}_{config_type}_config_{timestamp}.txt"
        backup_path = os.path.join(backup_dir, backup_filename)
        
        print(f"Backing up {config_type} configuration from {hostname}...")
        print(f"Backup file: {backup_path}")
        
        # Simulate configuration backup
        sample_config = f"""!
! {hostname} {config_type.title()} Configuration
! Backup created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {hostname}
!
boot-start-marker
boot-end-marker
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 duplex auto
 speed auto
!
interface GigabitEthernet0/1
 ip address 192.168.2.1 255.255.255.0
 duplex auto
 speed auto
!
router ospf 1
 router-id 1.1.1.1
 network 192.168.1.0 0.0.0.255 area 0
 network 192.168.2.0 0.0.0.255 area 0
!
ip http server
ip http secure-server
!
line con 0
line aux 0
line vty 0 4
 login
 transport input none
!
end
"""
        
        # Write backup to file
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(sample_config)
        
        print(f"✓ Configuration backup completed successfully")
        return backup_path
        
    except Exception as e:
        print(f"✗ Backup failed: {e}")
        return None


def load_device_list(filename: str) -> List[Dict[str, str]]:
    """
    Load device list from a JSON file.
    
    Args:
        filename (str): Path to JSON file containing device information
        
    Returns:
        List[Dict[str, str]]: List of device dictionaries
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            devices = json.load(f)
        print(f"✓ Loaded {len(devices)} devices from {filename}")
        return devices
    except FileNotFoundError:
        print(f"✗ Device file {filename} not found")
        return []
    except json.JSONDecodeError:
        print(f"✗ Invalid JSON in file {filename}")
        return []


def generate_config_template(device_type: str, hostname: str) -> str:
    """
    Generate a basic configuration template for a device.
    
    Args:
        device_type (str): Type of device ('router' or 'switch')
        hostname (str): Device hostname
        
    Returns:
        str: Configuration template
    """
    base_config = f"""!
! Configuration template for {hostname}
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {hostname}
!
boot-start-marker
boot-end-marker
!
"""
    
    if device_type.lower() == 'router':
        base_config += """
! Router-specific configuration
ip cef
!
interface GigabitEthernet0/0
 description WAN Interface
 no ip address
 shutdown
!
interface GigabitEthernet0/1
 description LAN Interface  
 no ip address
 shutdown
!
router ospf 1
 router-id 1.1.1.1
!
"""
    elif device_type.lower() == 'switch':
        base_config += """
! Switch-specific configuration
!
vlan 10
 name Data
!
vlan 20
 name Voice
!
interface range FastEthernet0/1-24
 switchport mode access
 switchport access vlan 10
!
interface GigabitEthernet0/1
 description Uplink
 switchport mode trunk
!
"""
    
    base_config += """
ip http server
!
line con 0
line aux 0
line vty 0 4
 login
 transport input none
!
end
"""
    
    return base_config