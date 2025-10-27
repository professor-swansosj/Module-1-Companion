"""
Network Devices Module

This module contains classes for representing different types of network devices.
It demonstrates object-oriented programming principles for network automation.
"""

from typing import Dict, List, Optional
from datetime import datetime


class NetworkDevice:
    """Base class for all network devices."""
    
    def __init__(self, hostname: str, ip_address: str, device_type: str, vendor: str = "Generic"):
        """
        Initialize a network device.
        
        Args:
            hostname (str): Device hostname
            ip_address (str): Management IP address  
            device_type (str): Type of device (router, switch, firewall, etc.)
            vendor (str): Device vendor (Cisco, Juniper, etc.)
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.vendor = vendor
        self.status = "offline"
        self.uptime = None
        self.last_backup = None
    
    def connect(self) -> bool:
        """
        Connect to the network device.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        print(f"Connecting to {self.hostname} at {self.ip_address}...")
        # Simulate connection logic
        self.status = "connected"
        print(f"✓ Successfully connected to {self.hostname}")
        return True
    
    def disconnect(self) -> bool:
        """
        Disconnect from the network device.
        
        Returns:
            bool: True if disconnection successful
        """
        print(f"Disconnecting from {self.hostname}...")
        self.status = "offline"
        print(f"✓ Disconnected from {self.hostname}")
        return True
    
    def get_status(self) -> str:
        """
        Get current device status.
        
        Returns:
            str: Status string
        """
        return f"{self.hostname} ({self.vendor} {self.device_type}): {self.status}"
    
    def backup_config(self) -> Optional[str]:
        """
        Backup device configuration.
        
        Returns:
            Optional[str]: Backup filename if successful, None otherwise
        """
        if self.status != "connected":
            print(f"Cannot backup {self.hostname} - device not connected")
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{self.hostname}_backup_{timestamp}.cfg"
        
        print(f"Backing up configuration for {self.hostname}...")
        # Simulate backup process
        self.last_backup = datetime.now()
        print(f"✓ Configuration saved to {backup_filename}")
        
        return backup_filename
    
    def get_uptime(self) -> str:
        """
        Get device uptime.
        
        Returns:
            str: Uptime string
        """
        if self.status != "connected":
            return "Unknown (device offline)"
        
        # Simulate uptime
        return "15 days, 8 hours, 42 minutes"
    
    def __str__(self) -> str:
        """String representation of the device."""
        return f"{self.vendor} {self.device_type}: {self.hostname} ({self.ip_address})"
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return (f"NetworkDevice(hostname='{self.hostname}', "
                f"ip_address='{self.ip_address}', "
                f"device_type='{self.device_type}', "
                f"vendor='{self.vendor}')")


class Router(NetworkDevice):
    """Router class with routing-specific functionality."""
    
    def __init__(self, hostname: str, ip_address: str, vendor: str = "Generic"):
        """
        Initialize a router device.
        
        Args:
            hostname (str): Router hostname
            ip_address (str): Management IP address
            vendor (str): Router vendor
        """
        super().__init__(hostname, ip_address, "router", vendor)
        self.routing_table: List[Dict[str, str]] = []
        self.ospf_config: Dict = {}
        self.interfaces: Dict[str, Dict] = {}
    
    def add_static_route(self, network: str, next_hop: str, 
                        administrative_distance: int = 1) -> bool:
        """
        Add a static route to the routing table.
        
        Args:
            network (str): Destination network (e.g., '192.168.1.0/24')
            next_hop (str): Next hop IP address
            administrative_distance (int): Route administrative distance
            
        Returns:
            bool: True if route added successfully
        """
        route = {
            "network": network,
            "next_hop": next_hop,
            "administrative_distance": administrative_distance,
            "type": "static"
        }
        
        self.routing_table.append(route)
        print(f"Added static route: {network} via {next_hop}")
        return True
    
    def configure_interface(self, interface: str, ip_address: str, 
                          subnet_mask: str, description: str = "") -> bool:
        """
        Configure a router interface.
        
        Args:
            interface (str): Interface name
            ip_address (str): IP address
            subnet_mask (str): Subnet mask
            description (str): Interface description
            
        Returns:
            bool: True if configuration successful
        """
        self.interfaces[interface] = {
            "ip_address": ip_address,
            "subnet_mask": subnet_mask,
            "description": description,
            "status": "up"
        }
        
        print(f"Configured {interface} on {self.hostname}:")
        print(f"  IP: {ip_address}/{subnet_mask}")
        if description:
            print(f"  Description: {description}")
        
        return True
    
    def show_routing_table(self) -> None:
        """Display the routing table."""
        print(f"\n=== Routing Table for {self.hostname} ===")
        if not self.routing_table:
            print("No routes configured")
            return
        
        for route in self.routing_table:
            print(f"  {route['network']} via {route['next_hop']} "
                  f"[{route['administrative_distance']}/{route['type']}]")
    
    def show_interfaces(self) -> None:
        """Display interface configuration."""
        print(f"\n=== Interface Configuration for {self.hostname} ===")
        if not self.interfaces:
            print("No interfaces configured")
            return
        
        for interface, config in self.interfaces.items():
            print(f"  {interface}:")
            print(f"    IP Address: {config['ip_address']}/{config['subnet_mask']}")
            print(f"    Status: {config['status']}")
            if config['description']:
                print(f"    Description: {config['description']}")


class Switch(NetworkDevice):
    """Switch class with switching-specific functionality."""
    
    def __init__(self, hostname: str, ip_address: str, vendor: str = "Generic"):
        """
        Initialize a switch device.
        
        Args:
            hostname (str): Switch hostname
            ip_address (str): Management IP address
            vendor (str): Switch vendor
        """
        super().__init__(hostname, ip_address, "switch", vendor)
        self.vlans: Dict[int, Dict] = {}
        self.port_config: Dict[str, Dict] = {}
        self.mac_address_table: List[Dict] = []
    
    def create_vlan(self, vlan_id: int, vlan_name: str) -> bool:
        """
        Create a VLAN.
        
        Args:
            vlan_id (int): VLAN ID
            vlan_name (str): VLAN name
            
        Returns:
            bool: True if VLAN created successfully
        """
        if vlan_id in self.vlans:
            print(f"VLAN {vlan_id} already exists on {self.hostname}")
            return False
        
        self.vlans[vlan_id] = {
            "name": vlan_name,
            "ports": [],
            "status": "active"
        }
        
        print(f"Created VLAN {vlan_id} ({vlan_name}) on {self.hostname}")
        return True
    
    def configure_port(self, port: str, vlan: int, mode: str = "access", 
                      description: str = "") -> bool:
        """
        Configure a switch port.
        
        Args:
            port (str): Port name (e.g., 'FastEthernet0/1')
            vlan (int): VLAN ID
            mode (str): Port mode ('access' or 'trunk')
            description (str): Port description
            
        Returns:
            bool: True if port configured successfully
        """
        if vlan not in self.vlans:
            print(f"VLAN {vlan} does not exist. Create it first.")
            return False
        
        self.port_config[port] = {
            "vlan": vlan,
            "mode": mode,
            "description": description,
            "status": "up"
        }
        
        # Add port to VLAN
        if port not in self.vlans[vlan]["ports"]:
            self.vlans[vlan]["ports"].append(port)
        
        print(f"Configured port {port} on {self.hostname}:")
        print(f"  Mode: {mode}")
        print(f"  VLAN: {vlan}")
        if description:
            print(f"  Description: {description}")
        
        return True
    
    def show_vlans(self) -> None:
        """Display VLAN configuration."""
        print(f"\n=== VLAN Configuration for {self.hostname} ===")
        if not self.vlans:
            print("No VLANs configured")
            return
        
        for vlan_id, config in self.vlans.items():
            ports = ", ".join(config["ports"]) if config["ports"] else "None"
            print(f"  VLAN {vlan_id} ({config['name']}): {config['status']}")
            print(f"    Ports: {ports}")
    
    def show_port_config(self) -> None:
        """Display port configuration."""
        print(f"\n=== Port Configuration for {self.hostname} ===")
        if not self.port_config:
            print("No ports configured")
            return
        
        for port, config in self.port_config.items():
            print(f"  {port}:")
            print(f"    Mode: {config['mode']}")
            print(f"    VLAN: {config['vlan']}")
            print(f"    Status: {config['status']}")
            if config['description']:
                print(f"    Description: {config['description']}")
    
    def add_mac_entry(self, mac_address: str, vlan: int, port: str) -> bool:
        """
        Add a MAC address table entry.
        
        Args:
            mac_address (str): MAC address
            vlan (int): VLAN ID
            port (str): Port name
            
        Returns:
            bool: True if entry added successfully
        """
        entry = {
            "mac_address": mac_address,
            "vlan": vlan,
            "port": port,
            "type": "dynamic"
        }
        
        self.mac_address_table.append(entry)
        return True
    
    def show_mac_table(self) -> None:
        """Display MAC address table."""
        print(f"\n=== MAC Address Table for {self.hostname} ===")
        if not self.mac_address_table:
            print("MAC address table empty")
            return
        
        print("MAC Address       VLAN  Port            Type")
        print("-" * 45)
        for entry in self.mac_address_table:
            print(f"{entry['mac_address']: <17} {entry['vlan']: <5} "
                  f"{entry['port']: <15} {entry['type']}")


def create_network_topology() -> List[NetworkDevice]:
    """
    Create a sample network topology with various devices.
    
    Returns:
        List[NetworkDevice]: List of network devices
    """
    devices = []
    
    # Create routers
    core_router = Router("Core-Router-01", "10.0.0.1", "Cisco")
    branch_router = Router("Branch-Router-01", "10.0.1.1", "Cisco")
    
    # Create switches
    access_switch1 = Switch("Access-Switch-01", "10.0.0.10", "Cisco")
    access_switch2 = Switch("Access-Switch-02", "10.0.0.11", "Cisco")
    
    # Configure core router
    core_router.configure_interface("GigabitEthernet0/0", "10.0.0.1", "255.255.255.0", "LAN Interface")
    core_router.configure_interface("GigabitEthernet0/1", "192.168.100.1", "255.255.255.252", "WAN Interface")
    core_router.add_static_route("0.0.0.0/0", "192.168.100.2")
    
    # Configure branch router
    branch_router.configure_interface("GigabitEthernet0/0", "10.0.1.1", "255.255.255.0", "Branch LAN")
    branch_router.configure_interface("GigabitEthernet0/1", "192.168.100.6", "255.255.255.252", "To Core")
    branch_router.add_static_route("10.0.0.0/24", "192.168.100.5")
    
    # Configure access switch 1
    access_switch1.create_vlan(10, "Data")
    access_switch1.create_vlan(20, "Voice")
    access_switch1.configure_port("FastEthernet0/1", 10, "access", "Workstation 1")
    access_switch1.configure_port("FastEthernet0/2", 10, "access", "Workstation 2") 
    access_switch1.configure_port("FastEthernet0/24", 10, "trunk", "Uplink to Core")
    
    # Configure access switch 2
    access_switch2.create_vlan(30, "Guest")
    access_switch2.create_vlan(40, "IoT")
    access_switch2.configure_port("FastEthernet0/1", 30, "access", "Guest Access")
    access_switch2.configure_port("FastEthernet0/2", 40, "access", "IoT Device")
    
    devices.extend([core_router, branch_router, access_switch1, access_switch2])
    
    return devices