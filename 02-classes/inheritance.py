"""
Class Inheritance Example - Network Automation

This module demonstrates class inheritance in Python for network automation.
Inheritance allows you to create specialized device classes that share common
functionality while adding vendor-specific or device-type-specific features.
"""

from typing import List, Dict, Any


class NetworkDevice:
    """Base class for all network devices with common functionality."""
    
    def __init__(self, hostname: str, ip_address: str, device_type: str, vendor: str = "Generic"):
        """Initialize a network device with basic attributes."""
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.vendor = vendor
        self.status = "offline"
        self.config = {}
    
    def connect(self):
        """Connect to the network device."""
        print(f"Connecting to {self.hostname} at {self.ip_address}...")
        self.status = "connected"
        return True
    
    def disconnect(self):
        """Disconnect from the network device."""
        print(f"Disconnecting from {self.hostname}...")
        self.status = "offline"
        return True
    
    def get_version(self):
        """Get device OS version - to be overridden by subclasses."""
        return "Unknown OS Version"
    
    def backup_config(self):
        """Backup device configuration."""
        if self.status == "connected":
            print(f"Backing up configuration for {self.hostname}...")
            return f"{self.hostname}_backup.cfg"
        return None
    
    def get_status(self):
        """Get device status information."""
        return f"{self.hostname} ({self.vendor} {self.device_type}): {self.status}"
    
    def __str__(self):
        """String representation of the device."""
        return f"{self.vendor} {self.device_type}: {self.hostname} ({self.ip_address})"


class CiscoDevice(NetworkDevice):
    """Cisco network device with Cisco-specific functionality."""
    
    def __init__(self, hostname: str, ip_address: str, device_type: str, ios_version: str = "15.1"):
        """Initialize Cisco device with IOS version."""
        super().__init__(hostname, ip_address, device_type, "Cisco")
        self.ios_version = ios_version
        self.enable_password = None
    
    def get_version(self): # type: ignore
        """Get Cisco IOS version."""
        return f"Cisco IOS {self.ios_version}"
    
    def configure_interface(self, interface: str, ip_address: str, subnet_mask: str):
        """Configure a Cisco interface."""
        if self.status != "connected":
            print("Device not connected!")
            return False
        
        config_commands = [
            f"interface {interface}",
            f"ip address {ip_address} {subnet_mask}",
            "no shutdown"
        ]
        
        print(f"Configuring {interface} on {self.hostname}:")
        for cmd in config_commands:
            print(f"  {cmd}")
        
        self.config[interface] = {
            "ip_address": ip_address,
            "subnet_mask": subnet_mask,
            "status": "up"
        }
        return True
    
    def show_running_config(self):
        """Display running configuration summary."""
        print(f"\n=== Running Config for {self.hostname} ===")
        print(f"Version: {self.get_version()}")
        print("Interfaces:")
        for interface, config in self.config.items():
            print(f"  {interface}: {config['ip_address']}/{config['subnet_mask']} ({config['status']})")


class JuniperDevice(NetworkDevice):
    """Juniper network device with Junos-specific functionality."""
    
    def __init__(self, hostname: str, ip_address: str, device_type: str, junos_version: str = "20.4"):
        """Initialize Juniper device with Junos version."""
        super().__init__(hostname, ip_address, device_type, "Juniper")
        self.junos_version = junos_version
    
    def get_version(self): # type: ignore
        """Get Junos version."""
        return f"Junos OS {self.junos_version}"
    
    def configure_interface(self, interface: str, ip_address: str, prefix_length: int):
        """Configure a Juniper interface with CIDR notation."""
        if self.status != "connected":
            print("Device not connected!")
            return False
        
        print(f"Configuring {interface} on {self.hostname} (Junos style):")
        print(f"  set interfaces {interface} unit 0 family inet address {ip_address}/{prefix_length}")
        
        self.config[interface] = {
            "ip_address": ip_address,
            "prefix_length": prefix_length,
            "status": "up"
        }
        return True
    
    def show_configuration(self):
        """Display Junos configuration summary."""
        print(f"\n=== Configuration for {self.hostname} ===")
        print(f"Version: {self.get_version()}")
        print("Interfaces:")
        for interface, config in self.config.items():
            print(f"  {interface}: {config['ip_address']}/{config['prefix_length']}")


class Router(NetworkDevice):
    """Router-specific functionality regardless of vendor."""
    
    def __init__(self, hostname: str, ip_address: str, vendor: str = "Generic"):
        """Initialize router."""
        super().__init__(hostname, ip_address, "router", vendor)
        self.routing_table = []
        self.ospf_config = {}
    
    def configure_ospf(self, process_id: int, router_id: str, networks: List[Dict[str, Any]]):
        """Configure OSPF routing protocol."""
        print(f"Configuring OSPF on {self.hostname}:")
        print(f"  Process ID: {process_id}")
        print(f"  Router ID: {router_id}")
        
        self.ospf_config = {
            "process_id": process_id,
            "router_id": router_id,
            "networks": networks
        }
        
        print("  Networks:")
        for network in networks:
            print(f"    {network['network']} area {network['area']}")
        
        return True
    
    def add_static_route(self, network: str, next_hop: str):
        """Add a static route."""
        route = {"network": network, "next_hop": next_hop}
        self.routing_table.append(route)
        print(f"Added static route: {network} via {next_hop}")
    
    def show_routing_table(self):
        """Display routing table."""
        print(f"\n=== Routing Table for {self.hostname} ===")
        if self.routing_table:
            for route in self.routing_table:
                print(f"  {route['network']} via {route['next_hop']}")
        else:
            print("  No static routes configured")


class Switch(NetworkDevice):
    """Switch-specific functionality regardless of vendor."""
    
    def __init__(self, hostname: str, ip_address: str, vendor: str = "Generic"):
        """Initialize switch."""
        super().__init__(hostname, ip_address, "switch", vendor)
        self.vlans = {}
        self.port_config = {}
    
    def create_vlan(self, vlan_id: int, name: str):
        """Create a VLAN."""
        self.vlans[vlan_id] = {"name": name, "ports": []}
        print(f"Created VLAN {vlan_id}: {name}")
    
    def configure_port(self, port: str, vlan: int, mode: str = "access"):
        """Configure switch port."""
        if vlan not in self.vlans:
            print(f"VLAN {vlan} does not exist!")
            return False
        
        self.port_config[port] = {"vlan": vlan, "mode": mode}
        self.vlans[vlan]["ports"].append(port)
        print(f"Configured port {port}: {mode} mode, VLAN {vlan}")
        return True
    
    def show_vlans(self):
        """Display VLAN configuration."""
        print(f"\n=== VLAN Configuration for {self.hostname} ===")
        for vlan_id, config in self.vlans.items():
            ports = ", ".join(config["ports"]) if config["ports"] else "None"
            print(f"  VLAN {vlan_id} ({config['name']}): Ports {ports}")


class CiscoRouter(Router, CiscoDevice):
    """Cisco-specific router combining Router and CiscoDevice functionality."""
    
    def __init__(self, hostname: str, ip_address: str, ios_version: str = "15.1"):
        """Initialize Cisco router."""
        # Call Router's __init__ which will call NetworkDevice's __init__
        Router.__init__(self, hostname, ip_address, "Cisco")
        # Set Cisco-specific attributes
        self.ios_version = ios_version
    
    def get_version(self): # type: ignore
        """Override to return Cisco IOS version."""
        return f"Cisco IOS {self.ios_version}"


class CiscoSwitch(Switch, CiscoDevice):
    """Cisco-specific switch combining Switch and CiscoDevice functionality."""
    
    def __init__(self, hostname: str, ip_address: str, ios_version: str = "15.1"):
        """Initialize Cisco switch."""
        Switch.__init__(self, hostname, ip_address, "Cisco")
        self.ios_version = ios_version
    
    def get_version(self): # type: ignore
        """Override to return Cisco IOS version."""
        return f"Cisco IOS {self.ios_version}"


def main():
    """Demonstrate class inheritance."""
    print("=== Network Device Inheritance Demo ===\n")
    
    # Create base network devices
    print("1. Creating base network devices:")
    generic_device = NetworkDevice("generic-device", "10.0.0.1", "unknown")
    print(f"Created: {generic_device}")
    print(f"Version: {generic_device.get_version()}\n")
    
    # Create vendor-specific devices
    print("2. Creating vendor-specific devices:")
    cisco_device = CiscoDevice("cisco-device", "10.0.0.2", "router", "16.9")
    juniper_device = JuniperDevice("juniper-device", "10.0.0.3", "switch", "21.1")
    
    print(f"Cisco: {cisco_device}")
    print(f"Version: {cisco_device.get_version()}")
    print(f"Juniper: {juniper_device}")
    print(f"Version: {juniper_device.get_version()}\n")
    
    # Configure Cisco device
    print("3. Configuring Cisco device:")
    cisco_device.connect()
    cisco_device.configure_interface("GigabitEthernet0/0", "192.168.1.1", "255.255.255.0")
    cisco_device.show_running_config()
    
    # Configure Juniper device
    print("\n4. Configuring Juniper device:")
    juniper_device.connect()
    juniper_device.configure_interface("ge-0/0/0", "192.168.2.1", 24)
    juniper_device.show_configuration()
    
    # Create device-type specific objects
    print("\n5. Creating device-type specific objects:")
    router = Router("border-router", "10.0.1.1", "Generic")
    switch = Switch("access-switch", "10.0.1.2", "Generic")
    
    # Configure router
    print("\n6. Configuring router:")
    router.connect()
    ospf_networks = [
        {"network": "10.0.1.0/24", "area": "0"},
        {"network": "192.168.1.0/24", "area": "1"}
    ]
    router.configure_ospf(1, "1.1.1.1", ospf_networks)
    router.add_static_route("0.0.0.0/0", "10.0.1.254")
    router.show_routing_table()
    
    # Configure switch
    print("\n7. Configuring switch:")
    switch.connect()
    switch.create_vlan(10, "Data")
    switch.create_vlan(20, "Voice")
    switch.configure_port("FastEthernet0/1", 10)
    switch.configure_port("FastEthernet0/2", 20)
    switch.show_vlans()
    
    # Create specialized Cisco devices
    print("\n8. Creating specialized Cisco devices:")
    cisco_router = CiscoRouter("core-router", "10.0.2.1", "16.12")
    cisco_switch = CiscoSwitch("distribution-switch", "10.0.2.2", "15.2")
    
    print(f"Cisco Router: {cisco_router}")
    print(f"Version: {cisco_router.get_version()}")
    print(f"Cisco Switch: {cisco_switch}")
    print(f"Version: {cisco_switch.get_version()}")
    
    # Demonstrate polymorphism
    print("\n9. Demonstrating polymorphism:")
    devices = [cisco_device, juniper_device, cisco_router, cisco_switch]
    
    print("Device versions:")
    for device in devices:
        print(f"  {device.hostname}: {device.get_version()}")


if __name__ == "__main__":
    main()