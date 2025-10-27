"""
🎯 Class Fundamentals - Build Your Network Device Empire!

Your mission: Transform from scattered variables to powerful object-oriented network management.
Follow the TODOs to build classes that network professionals actually use!

📚 STUDY THE README FIRST! It explains all the concepts you'll implement here.
"""

# ====================================================================
# PART 1: BASIC CLASSES - Your Foundation (Objects & Attributes)
# ====================================================================

class NetworkDevice:
    """
    Base class for all network devices.
    
    This is your foundation - every device needs hostname, IP, and connection status.
    Study the README section on "Objects and Attributes" before starting!
    """
    
    def __init__(self, hostname, ip_address, device_type="Unknown"):
        """
        Initialize a network device.
        
        TODO: Set up the basic attributes every device needs
        """
        # TODO: Store hostname, ip_address, and device_type as instance attributes
        # Hint: self.hostname = hostname
        
        # TODO: Initialize connection status as "disconnected"
        
        # TODO: Create an empty interfaces list for this device
        
        pass
    
    def connect(self):
        """
        Connect to the device.
        
        TODO: Implement the connection behavior (Methods section in README)
        """
        # TODO: Change status to "connected"
        # TODO: Print a connection success message with the hostname
        pass
    
    def disconnect(self):
        """
        Disconnect from the device.
        
        TODO: Implement disconnection behavior
        """
        # TODO: Change status to "disconnected" 
        # TODO: Print disconnection message
        pass
    
    def display_info(self):
        """
        Show device information.
        
        TODO: Display all device details
        """
        # TODO: Print hostname, IP, type, and connection status
        # Make it look professional!
        pass

# ====================================================================
# PART 2: SMART PROPERTIES - Data Validation (Properties section)  
# ====================================================================

class SmartNetworkDevice:
    """
    Enhanced device with property-based validation.
    
    Study the README "Properties (Smart Attributes)" section first!
    Properties let you control how data is stored and retrieved.
    """
    
    def __init__(self, hostname, device_type="Unknown"):
        self._hostname = hostname
        self._ip_address = None
        self._device_type = device_type
        self.status = "disconnected"
    
    @property
    def hostname(self):
        """Get the hostname."""
        return self._hostname
    
    @hostname.setter
    def hostname(self, value):
        """
        Set hostname with validation.
        
        TODO: Add hostname validation (Properties section in README)
        """
        # TODO: Check if value is a string and not empty
        # TODO: Check length is reasonable (1-63 characters)
        # TODO: Store the validated hostname
        # TODO: Raise ValueError if invalid
        pass
    
    @property
    def ip_address(self):
        """Get IP address."""
        return self._ip_address
    
    @ip_address.setter  
    def ip_address(self, value):
        """
        Set IP address with validation.
        
        TODO: Implement IP address validation
        """
        # TODO: Allow None to clear IP address
        # TODO: For non-None values, validate IP format
        # TODO: Check it has 4 parts separated by dots
        # TODO: Each part should be 0-255
        # TODO: Store valid IP or raise ValueError
        pass
    
    @property
    def is_configured(self):
        """
        Computed property: check if device is ready.
        
        TODO: Implement this computed property
        """
        # TODO: Return True if hostname exists and IP is set
        # TODO: Otherwise return False
        pass

# ====================================================================
# PART 3: INHERITANCE - Device Families (Inheritance section)
# ====================================================================

class Router(NetworkDevice):
    """
    Router class - inherits from NetworkDevice.
    
    Study the README "Inheritance" section first!
    Routers have everything a NetworkDevice has, plus routing-specific features.
    """
    
    def __init__(self, hostname, ip_address, model="Generic"):
        """
        Initialize router with inherited and new attributes.
        
        TODO: Use inheritance properly (super() call)
        """
        # TODO: Call parent class __init__ with "Router" as device_type
        # Hint: super().__init__(hostname, ip_address, "Router")
        
        # TODO: Add router-specific attributes
        # model, routing_table (empty list), ospf_enabled (False)
        
        pass
    
    def add_route(self, network, next_hop):
        """
        Add a static route.
        
        TODO: Implement route addition
        """
        # TODO: Create a route dictionary with 'network' and 'next_hop' keys
        # TODO: Add it to the routing_table list
        # TODO: Print confirmation message
        pass
    
    def show_routes(self):
        """
        Display routing table.
        
        TODO: Show all configured routes
        """
        # TODO: Print header for routing table
        # TODO: Loop through routes and display them nicely
        # TODO: Handle case when no routes exist
        pass

class Switch(NetworkDevice):
    """
    Switch class - also inherits from NetworkDevice.
    
    Switches have everything a NetworkDevice has, plus switching features.
    """
    
    def __init__(self, hostname, ip_address, port_count=24):
        """
        Initialize switch with switching features.
        
        TODO: Implement switch initialization
        """
        # TODO: Call parent __init__ with "Switch" as device_type
        
        # TODO: Add switch-specific attributes:
        # port_count, vlans (empty dict), mac_table (empty dict)
        
        # TODO: Create default VLAN 1
        # Hint: self.vlans[1] = {"name": "default", "ports": []}
        
        pass
    
    def create_vlan(self, vlan_id, name):
        """
        Create a VLAN.
        
        TODO: Add VLAN to the switch
        """
        # TODO: Add VLAN to vlans dict with name and empty ports list
        # TODO: Print VLAN creation message
        pass
    
    def show_vlans(self):
        """
        Display all VLANs.
        
        TODO: Show VLAN information
        """
        # TODO: Print VLAN header
        # TODO: Loop through vlans and display ID, name, and port count
        pass

# ====================================================================
# PART 4: MULTIPLE INHERITANCE - Advanced Concepts 
# ====================================================================

class CiscoDevice:
    """
    Mixin class for Cisco-specific features.
    
    This demonstrates multiple inheritance - combining features from multiple classes.
    """
    
    def __init__(self, ios_version="15.1", **kwargs):
        """TODO: Initialize Cisco-specific attributes"""
        # TODO: Store ios_version
        # TODO: Call super().__init__(**kwargs) to continue inheritance chain
        pass
    
    def show_version(self):
        """
        Show Cisco IOS version.
        
        TODO: Display Cisco version info
        """
        # TODO: Print Cisco IOS version information
        pass

class CiscoRouter(Router, CiscoDevice):
    """
    Cisco-specific router using multiple inheritance.
    
    This class inherits from both Router AND CiscoDevice!
    Study the README inheritance section for multiple inheritance.
    """
    
    def __init__(self, hostname, ip_address, model="ISR4331", ios_version="16.9"):
        """
        TODO: Handle multiple inheritance initialization
        """
        # TODO: Initialize Router part
        # TODO: Initialize CiscoDevice part  
        # Hint: Use Router.__init__ and CiscoDevice.__init__
        pass
    
    def show_cisco_routes(self):
        """
        Show routes in Cisco format.
        
        TODO: Combine router and Cisco functionality
        """
        # TODO: Print Cisco-style header
        # TODO: Call parent show_routes method
        # TODO: Add Cisco-specific route information
        pass

# ====================================================================
# 🎮 TEST YOUR CLASSES - Complete TODOs above, then uncomment below!
# ====================================================================

if __name__ == "__main__":
    print("=== 🎯 Class Fundamentals Challenge ===\n")
    
    # TODO: Complete all the classes above, then uncomment these tests:
    
    # # Test 1: Basic NetworkDevice
    # print("1️⃣ Basic Network Device:")
    # device = NetworkDevice("CORE-SW1", "192.168.1.10", "Switch")
    # device.display_info()
    # device.connect()
    # device.disconnect()
    # print()
    
    # # Test 2: Smart Properties
    # print("2️⃣ Smart Properties:")
    # smart_device = SmartNetworkDevice("BORDER-RTR", "Router")
    # smart_device.ip_address = "192.168.1.1"  # Should work
    # print(f"Configured: {smart_device.is_configured}")
    # 
    # # Test validation
    # try:
    #     smart_device.ip_address = "999.999.999.999"  # Should fail
    # except ValueError as e:
    #     print(f"✅ Validation caught invalid IP: {e}")
    # print()
    
    # # Test 3: Router Inheritance
    # print("3️⃣ Router Inheritance:")
    # router = Router("BORDER-R1", "10.0.1.1", "ISR4331")
    # router.connect()
    # router.add_route("0.0.0.0/0", "10.0.1.254")
    # router.add_route("192.168.0.0/16", "10.0.1.2")
    # router.show_routes()
    # print()
    
    # # Test 4: Switch Inheritance  
    # print("4️⃣ Switch Inheritance:")
    # switch = Switch("ACCESS-SW1", "10.0.1.2", 48)
    # switch.connect()
    # switch.create_vlan(10, "Data")
    # switch.create_vlan(20, "Voice") 
    # switch.show_vlans()
    # print()
    
    # # Test 5: Multiple Inheritance (Advanced!)
    # print("5️⃣ Multiple Inheritance:")
    # cisco_router = CiscoRouter("CORE-R1", "10.0.2.1", "ISR4451", "16.12")
    # cisco_router.connect()
    # cisco_router.show_version()
    # cisco_router.add_route("172.16.0.0/12", "10.0.2.254")
    # cisco_router.show_cisco_routes()
    
    # 🏆 SUCCESS MESSAGE
    print("🎯 Complete the TODOs above to unlock the test code!")
    print("📚 Remember: Study the README first to understand the concepts!")
    print("💡 Each TODO builds on the previous one - work step by step!")
    print()
    print("🚀 Once working, try these BONUS challenges:")
    print("   • Add a Firewall class with security-specific methods")  
    print("   • Create validation for port numbers (1-65535)")
    print("   • Add a WirelessAP class with SSID management")
    print("   • Implement a __str__ method for each class")