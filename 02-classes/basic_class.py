"""
Basic Class Creation and Initialization Examples
Network Device Classes for Network Automation

Classes help organize network device data and functionality,
making code more maintainable and reusable.
"""

class NetworkDevice:
    """Basic network device class with initialization."""
    
    def __init__(self, hostname, ip_address, device_type, location="Unknown"):
        """
        Initialize a network device.
        
        Args:
            hostname: Device hostname
            ip_address: Management IP address
            device_type: Type of device (router, switch, firewall, etc.)
            location: Physical location (optional)
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.location = location
        self.is_connected = False
        self.uptime = 0
        self.interfaces = []
    
    def display_info(self):
        """Display basic device information."""
        print(f"""
Device Information:
  Hostname: {self.hostname}
  IP Address: {self.ip_address}
  Type: {self.device_type}
  Location: {self.location}
  Connected: {self.is_connected}
  Uptime: {self.uptime} hours
  Interfaces: {len(self.interfaces)} configured
        """)

class Router:
    """Router class with routing-specific attributes."""
    
    def __init__(self, hostname, ip_address, model, ios_version):
        """
        Initialize a router device.
        
        Args:
            hostname: Router hostname
            ip_address: Management IP address
            model: Router model (e.g., 'ISR4331')
            ios_version: IOS software version
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.model = model
        self.ios_version = ios_version
        self.routing_table = []
        self.ospf_enabled = False
        self.bgp_enabled = False
        self.interfaces = {}
    
    def show_router_info(self):
        """Display router-specific information."""
        print(f"""
Router Information:
  Hostname: {self.hostname}
  Management IP: {self.ip_address}
  Model: {self.model}
  IOS Version: {self.ios_version}
  Routing Protocols:
    - OSPF: {'Enabled' if self.ospf_enabled else 'Disabled'}
    - BGP: {'Enabled' if self.bgp_enabled else 'Disabled'}
  Routing Table Entries: {len(self.routing_table)}
  Configured Interfaces: {len(self.interfaces)}
        """)

class Switch:
    """Switch class with switching-specific attributes."""
    
    def __init__(self, hostname, ip_address, model, port_count=24):
        """
        Initialize a switch device.
        
        Args:
            hostname: Switch hostname
            ip_address: Management IP address
            model: Switch model (e.g., 'Catalyst2960')
            port_count: Number of ports (default: 24)
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.model = model
        self.port_count = port_count
        self.vlans = {}  # Dictionary of VLAN ID -> VLAN info
        self.mac_table = {}
        self.stp_enabled = True
        self.ports = {}
        
        # Initialize default VLAN
        self.vlans[1] = {
            'name': 'default',
            'description': 'Default VLAN',
            'ports': []
        }
    
    def display_switch_info(self):
        """Display switch-specific information."""
        print(f"""
Switch Information:
  Hostname: {self.hostname}
  Management IP: {self.ip_address}
  Model: {self.model}
  Port Count: {self.port_count}
  VLANs Configured: {len(self.vlans)}
  MAC Table Entries: {len(self.mac_table)}
  STP Enabled: {self.stp_enabled}
        """)

class AccessPoint:
    """Wireless Access Point class."""
    
    def __init__(self, hostname, ip_address, ssid, channel=6):
        """
        Initialize a wireless access point.
        
        Args:
            hostname: AP hostname
            ip_address: Management IP address
            ssid: Wireless network name
            channel: WiFi channel (default: 6)
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.ssid = ssid
        self.channel = channel
        self.clients_connected = 0
        self.security_type = "WPA2"
        self.power_level = 100  # Percentage
        self.band = "2.4GHz"
    
    def show_ap_status(self):
        """Display access point status."""
        print(f"""
Access Point Status:
  Hostname: {self.hostname}
  IP Address: {self.ip_address}
  SSID: {self.ssid}
  Channel: {self.channel}
  Band: {self.band}
  Security: {self.security_type}
  Power Level: {self.power_level}%
  Connected Clients: {self.clients_connected}
        """)

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Basic Class Creation and Initialization Practice ===\n")
    
    # Example 1: Create a basic network device
    print("1. Creating a Basic Network Device:")
    device1 = NetworkDevice(
        hostname="CORE-SW1",
        ip_address="192.168.1.10", 
        device_type="Core Switch",
        location="Data Center Rack 1"
    )
    device1.display_info()
    
    # Example 2: Create multiple devices
    print("2. Creating Multiple Network Devices:")
    devices = []
    
    # Create router
    router1 = Router(
        hostname="BORDER-RTR1",
        ip_address="203.0.113.1",
        model="ISR4331", 
        ios_version="15.6(3)M2"
    )
    devices.append(router1)
    
    # Create switch
    switch1 = Switch(
        hostname="ACCESS-SW1",
        ip_address="192.168.1.20",
        model="Catalyst2960-X",
        port_count=48
    )
    devices.append(switch1)
    
    # Create access point
    ap1 = AccessPoint(
        hostname="OFFICE-AP1", 
        ip_address="192.168.1.30",
        ssid="CompanyWiFi",
        channel=11
    )
    devices.append(ap1)
    
    # Display all devices
    print(f"Created {len(devices)} network devices:")
    for device in devices:
        if hasattr(device, 'show_router_info'):
            device.show_router_info()
        elif hasattr(device, 'display_switch_info'):
            device.display_switch_info()
        elif hasattr(device, 'show_ap_status'):
            device.show_ap_status()
    
    # Example 3: Modifying object attributes
    print("3. Modifying Device Attributes:")
    print("Original device status:")
    device1.display_info()
    
    # Modify attributes
    device1.is_connected = True
    device1.uptime = 72
    device1.interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2", "GigabitEthernet0/24"]
    
    print("After modification:")
    device1.display_info()
    
    # Example 4: Router-specific operations
    print("4. Router-Specific Operations:")
    router1.ospf_enabled = True
    router1.routing_table = [
        "0.0.0.0/0 via 203.0.113.1",
        "192.168.1.0/24 via GigabitEthernet0/1", 
        "10.1.1.0/30 via Serial0/0/0"
    ]
    router1.interfaces = {
        "GigabitEthernet0/0": {"ip": "203.0.113.2", "status": "up"},
        "GigabitEthernet0/1": {"ip": "192.168.1.1", "status": "up"},
        "Serial0/0/0": {"ip": "10.1.1.1", "status": "up"}
    }
    router1.show_router_info()
    
    # Example 5: Switch VLAN management
    print("5. Switch VLAN Operations:")
    # Add VLANs to switch
    switch1.vlans[10] = {
        'name': 'SALES',
        'description': 'Sales Department',
        'ports': ['Gi0/1', 'Gi0/2', 'Gi0/3']
    }
    switch1.vlans[20] = {
        'name': 'FINANCE', 
        'description': 'Finance Department',
        'ports': ['Gi0/5', 'Gi0/6']
    }
    
    # Add MAC addresses
    switch1.mac_table = {
        "00:11:22:33:44:55": "Gi0/1",
        "00:66:77:88:99:AA": "Gi0/2",
        "00:BB:CC:DD:EE:FF": "Gi0/5"
    }
    
    switch1.display_switch_info()
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Create your own NetworkDevice objects with different parameters")
    print("2. Create a Firewall class with security-specific attributes") 
    print("3. Modify device attributes and observe the changes")
    print("4. Create a list of mixed device types and iterate through them")
    
    # Practice Exercise 1: Create your own devices
    print("\nPractice 1 - Create Your Own Devices:")
    # TODO: Create a router for your home network
    # home_router = Router(...)
    
    # TODO: Create a wireless AP
    # guest_ap = AccessPoint(...)
    
    # Practice Exercise 2: Create a Firewall class
    print("\nPractice 2 - Create a Firewall Class:")
    """
    class Firewall:
        def __init__(self, hostname, ip_address, model, license_type="Standard"):
            # Your code here - what attributes should a firewall have?
            pass
        
        def show_security_status(self):
            # Your code here - display firewall-specific information
            pass
    """
    
    print("\nChallenge: Design classes for other network devices!")
    print("Consider: Load balancers, WAN accelerators, network monitors, etc.")