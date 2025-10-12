"""
Class Properties Examples
Using Properties to Control Access to Network Device Attributes

Properties provide controlled access to class attributes with validation,
computed values, and encapsulation - essential for network device management.
"""

class NetworkInterface:
    """Network interface class demonstrating properties."""
    
    def __init__(self, name, interface_type="ethernet"):
        """Initialize network interface."""
        self._name = name
        self._ip_address = None
        self._subnet_mask = None
        self._status = "down"
        self._speed = "auto"
        self._duplex = "auto" 
        self._interface_type = interface_type
        self._mtu = 1500
    
    @property
    def name(self):
        """Get interface name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set interface name with validation."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Interface name must be a non-empty string")
        self._name = value.strip()
    
    @property
    def ip_address(self):
        """Get IP address."""
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self, value):
        """Set IP address with basic validation."""
        if value is None:
            self._ip_address = None
            return
        
        # Basic IP validation
        parts = value.split('.')
        if len(parts) != 4:
            raise ValueError("Invalid IP address format")
        
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                raise ValueError("Invalid IP address format")
        
        self._ip_address = value
    
    @property
    def subnet_mask(self):
        """Get subnet mask."""
        return self._subnet_mask
    
    @subnet_mask.setter
    def subnet_mask(self, value):
        """Set subnet mask with validation."""
        if value is None:
            self._subnet_mask = None
            return
        
        valid_masks = [
            "255.255.255.255", "255.255.255.254", "255.255.255.252",
            "255.255.255.248", "255.255.255.240", "255.255.255.224", 
            "255.255.255.192", "255.255.255.128", "255.255.255.0",
            "255.255.254.0", "255.255.252.0", "255.255.248.0",
            "255.255.240.0", "255.255.224.0", "255.255.192.0",
            "255.255.128.0", "255.255.0.0", "255.254.0.0", 
            "255.252.0.0", "255.248.0.0", "255.240.0.0",
            "255.224.0.0", "255.192.0.0", "255.128.0.0", "255.0.0.0"
        ]
        
        if value not in valid_masks:
            raise ValueError(f"Invalid subnet mask: {value}")
        
        self._subnet_mask = value
    
    @property
    def status(self):
        """Get interface status."""
        return self._status
    
    @status.setter
    def status(self, value):
        """Set interface status."""
        valid_statuses = ["up", "down", "admin-down", "testing"]
        if value not in valid_statuses:
            raise ValueError(f"Status must be one of: {', '.join(valid_statuses)}")
        self._status = value
    
    @property
    def speed(self):
        """Get interface speed."""
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """Set interface speed with validation."""
        valid_speeds = ["auto", "10", "100", "1000", "10000"]
        if str(value) not in valid_speeds:
            raise ValueError(f"Speed must be one of: {', '.join(valid_speeds)}")
        self._speed = str(value)
    
    @property
    def mtu(self):
        """Get MTU size."""
        return self._mtu
    
    @mtu.setter
    def mtu(self, value):
        """Set MTU with validation."""
        if not isinstance(value, int) or not 64 <= value <= 9216:
            raise ValueError("MTU must be between 64 and 9216 bytes")
        self._mtu = value
    
    @property
    def is_configured(self):
        """Computed property: check if interface is fully configured."""
        return (self._ip_address is not None and 
                self._subnet_mask is not None and
                self._status == "up")
    
    @property
    def network_address(self):
        """Computed property: calculate network address from IP and mask."""
        if not self.ip_address or not self.subnet_mask:
            return None
        
        # Simple network calculation
        ip_parts = [int(x) for x in self.ip_address.split('.')]
        mask_parts = [int(x) for x in self.subnet_mask.split('.')]
        
        network_parts = [ip_parts[i] & mask_parts[i] for i in range(4)]
        return '.'.join(map(str, network_parts))
    
    def display_config(self):
        """Display interface configuration."""
        print(f"""
Interface Configuration:
  Name: {self.name}
  Type: {self._interface_type}
  IP Address: {self.ip_address or 'Not configured'}
  Subnet Mask: {self.subnet_mask or 'Not configured'}
  Network: {self.network_address or 'Not calculated'}
  Status: {self.status}
  Speed: {self.speed} Mbps
  Duplex: {self._duplex}
  MTU: {self.mtu} bytes
  Fully Configured: {self.is_configured}
        """)

class NetworkDevice:
    """Network device with property-controlled management IP."""
    
    def __init__(self, hostname, device_type):
        self._hostname = hostname
        self._device_type = device_type
        self._management_ip = None
        self._is_reachable = False
        self._last_contact = None
        self._cpu_usage = 0
        self._memory_usage = 0
    
    @property
    def hostname(self):
        """Get device hostname."""
        return self._hostname
    
    @hostname.setter  
    def hostname(self, value):
        """Set hostname with validation."""
        if not isinstance(value, str) or len(value) < 1 or len(value) > 63:
            raise ValueError("Hostname must be 1-63 characters")
        
        # Basic hostname validation (simplified)
        if not value.replace('-', '').replace('_', '').isalnum():
            raise ValueError("Hostname contains invalid characters")
        
        self._hostname = value
    
    @property
    def management_ip(self):
        """Get management IP address."""
        return self._management_ip
    
    @management_ip.setter
    def management_ip(self, value):
        """Set management IP with validation."""
        if value is None:
            self._management_ip = None
            return
        
        # Validate IP address format
        try:
            parts = value.split('.')
            if len(parts) != 4:
                raise ValueError("Invalid IP format")
            
            for part in parts:
                if not 0 <= int(part) <= 255:
                    raise ValueError("Invalid IP octet")
            
            # Check for reserved ranges
            first_octet = int(parts[0])
            if first_octet in [0, 127, 224, 240]:
                raise ValueError("IP address in reserved range")
            
            self._management_ip = value
        except ValueError as e:
            raise ValueError(f"Invalid management IP: {e}")
    
    @property
    def cpu_usage(self):
        """Get CPU usage percentage."""
        return self._cpu_usage
    
    @cpu_usage.setter
    def cpu_usage(self, value):
        """Set CPU usage with validation."""
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            raise ValueError("CPU usage must be between 0 and 100")
        self._cpu_usage = float(value)
    
    @property
    def memory_usage(self):
        """Get memory usage percentage.""" 
        return self._memory_usage
    
    @memory_usage.setter
    def memory_usage(self, value):
        """Set memory usage with validation."""
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            raise ValueError("Memory usage must be between 0 and 100")
        self._memory_usage = float(value)
    
    @property
    def health_status(self):
        """Computed property: overall device health."""
        if self._cpu_usage > 90 or self._memory_usage > 90:
            return "Critical"
        elif self._cpu_usage > 70 or self._memory_usage > 70:
            return "Warning"
        elif self._is_reachable:
            return "Healthy"
        else:
            return "Unreachable"
    
    @property
    def device_summary(self):
        """Computed property: device summary string."""
        return f"{self.hostname} ({self._device_type}) - {self.health_status}"
    
    def display_status(self):
        """Display device status."""
        print(f"""
Device Status:
  Hostname: {self.hostname}
  Type: {self._device_type}
  Management IP: {self.management_ip or 'Not configured'}
  Reachable: {self._is_reachable}
  CPU Usage: {self.cpu_usage}%
  Memory Usage: {self.memory_usage}%
  Health Status: {self.health_status}
  Summary: {self.device_summary}
        """)

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Class Properties Practice ===\n")
    
    # Example 1: Network interface with properties
    print("1. Network Interface Configuration:")
    interface = NetworkInterface("GigabitEthernet0/1", "ethernet")
    
    # Configure interface step by step
    interface.ip_address = "192.168.1.1"
    interface.subnet_mask = "255.255.255.0"
    interface.status = "up"
    interface.speed = "1000"
    interface.mtu = 1500
    
    interface.display_config()
    
    # Example 2: Property validation
    print("2. Property Validation Examples:")
    interface2 = None
    try:
        # Valid configuration
        interface2 = NetworkInterface("Serial0/0/0", "serial")
        interface2.ip_address = "10.1.1.1"
        interface2.subnet_mask = "255.255.255.252"
        print("✓ Valid configuration accepted")
        
        # Invalid IP address - this will raise an error
        interface2.ip_address = "300.1.1.1"
    except ValueError as e:
        print(f"✗ Invalid IP caught: {e}")
    
    if interface2 is not None:
        try:
            # Invalid subnet mask
            interface2.subnet_mask = "255.255.255.1"
        except ValueError as e:
            print(f"✗ Invalid subnet mask caught: {e}")
    
    # Example 3: Network device with properties
    print("\n3. Network Device with Properties:")
    device = NetworkDevice("CORE-SW1", "Switch")
    
    # Configure device
    device.management_ip = "192.168.1.10"
    device.cpu_usage = 25.5
    device.memory_usage = 42.0
    device._is_reachable = True
    
    device.display_status()
    
    # Example 4: Computed properties
    print("4. Computed Properties Demonstration:")
    print(f"Network address: {interface.network_address}")
    print(f"Interface configured: {interface.is_configured}")
    print(f"Device health: {device.health_status}")
    print(f"Device summary: {device.device_summary}")
    
    # Example 5: Property validation errors
    print("\n5. Property Validation Error Handling:")
    
    validation_tests = [
        ("Invalid hostname", lambda: setattr(device, 'hostname', '')),
        ("Invalid CPU usage", lambda: setattr(device, 'cpu_usage', 150)),
        ("Invalid memory usage", lambda: setattr(device, 'memory_usage', -10)),
        ("Invalid management IP", lambda: setattr(device, 'management_ip', '192.168.1')),
        ("Invalid interface speed", lambda: setattr(interface, 'speed', '500')),
        ("Invalid MTU", lambda: setattr(interface, 'mtu', 50))
    ]
    
    for test_name, test_func in validation_tests:
        try:
            test_func()
            print(f"✗ {test_name}: Should have failed!")
        except ValueError as e:
            print(f"✓ {test_name}: Correctly caught - {e}")
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Create an interface and try setting invalid values")
    print("2. Add a new property with validation to NetworkInterface")
    print("3. Create computed properties that depend on multiple attributes")
    print("4. Add a read-only property (no setter)")
    
    # Practice Exercise 1: Create and configure interfaces
    print("\nPractice 1 - Configure Multiple Interfaces:")
    interfaces = []
    
    # TODO: Create 3 interfaces with different configurations
    # interface1 = NetworkInterface("GigabitEthernet0/1")
    # Configure each with different IP addresses, speeds, etc.
    
    # Practice Exercise 2: Add new properties
    print("\nPractice 2 - Add New Properties:")
    print("Challenge: Add these properties to NetworkInterface:")
    print("- duplex (full, half, auto) with validation")
    print("- vlan_id (1-4094) with validation")
    print("- description (string, max 240 characters)")
    
    # Practice Exercise 3: Computed properties
    print("\nPractice 3 - Create Computed Properties:")
    print("Challenge: Add these computed properties:")
    print("- broadcast_address (calculated from IP and mask)")
    print("- host_count (number of possible hosts)")
    print("- interface_utilization (based on current traffic)")
    
    # Practice Exercise 4: Read-only property
    print("\nPractice 4 - Read-Only Property:")
    """
    @property
    def configuration_hash(self):
        '''Read-only property: hash of current configuration'''
        import hashlib
        config_string = f"{self.ip_address}{self.subnet_mask}{self.speed}"
        return hashlib.md5(config_string.encode()).hexdigest()[:8]
    """
    
    print("\nAdd the above property to see configuration changes!")