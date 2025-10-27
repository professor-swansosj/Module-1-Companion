"""
Class Methods Example - Network Automation

This module demonstrates class methods in Python for network automation.
Class methods operate on the class itself rather than instances and are useful
for creating alternative constructors or working with class-level data.
"""

class NetworkDevice:
    """A network device with basic connection and management capabilities."""
    
    # Class variable to track all created devices
    device_count = 0
    
    def __init__(self, hostname: str, ip_address: str, device_type: str):
        """Initialize a network device with basic attributes."""
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.status = "offline"
        
        # Increment class variable
        NetworkDevice.device_count += 1
    
    @classmethod
    def from_dict(cls, device_data: dict):
        """
        Alternative constructor to create a device from a dictionary.
        
        Args:
            device_data (dict): Dictionary containing device information
            
        Returns:
            NetworkDevice: New device instance
        """
        return cls(
            device_data["hostname"],
            device_data["ip_address"], 
            device_data["device_type"]
        )
    
    @classmethod
    def from_csv_line(cls, csv_line: str):
        """
        Alternative constructor to create a device from a CSV line.
        
        Args:
            csv_line (str): CSV formatted string with device data
            
        Returns:
            NetworkDevice: New device instance
        """
        parts = csv_line.strip().split(',')
        return cls(parts[0], parts[1], parts[2])
    
    @classmethod
    def get_device_count(cls):
        """
        Get the total number of devices created.
        
        Returns:
            int: Total device count
        """
        return cls.device_count
    
    @classmethod
    def create_router(cls, hostname: str, ip_address: str):
        """
        Factory method to create a router device.
        
        Args:
            hostname (str): Router hostname
            ip_address (str): Router IP address
            
        Returns:
            NetworkDevice: New router instance
        """
        return cls(hostname, ip_address, "router")
    
    @classmethod
    def create_switch(cls, hostname: str, ip_address: str):
        """
        Factory method to create a switch device.
        
        Args:
            hostname (str): Switch hostname
            ip_address (str): Switch IP address
            
        Returns:
            NetworkDevice: New switch instance
        """
        return cls(hostname, ip_address, "switch")
    
    def connect(self):
        """Simulate connecting to the device."""
        print(f"Connecting to {self.hostname} at {self.ip_address}...")
        self.status = "connected"
        return True
    
    def disconnect(self):
        """Simulate disconnecting from the device."""
        print(f"Disconnecting from {self.hostname}...")
        self.status = "offline"
        return True
    
    def get_status(self):
        """Get device connection status."""
        return f"{self.hostname} ({self.device_type}): {self.status}"
    
    def backup_config(self):
        """Simulate backing up device configuration."""
        if self.status == "connected":
            print(f"Backing up configuration for {self.hostname}...")
            return f"config_backup_{self.hostname}.txt"
        else:
            print(f"Cannot backup config - {self.hostname} not connected")
            return None
    
    def restore_config(self, backup_file: str):
        """
        Simulate restoring device configuration from backup.
        
        Args:
            backup_file (str): Path to backup configuration file
        """
        if self.status == "connected":
            print(f"Restoring configuration for {self.hostname} from {backup_file}...")
            return True
        else:
            print(f"Cannot restore config - {self.hostname} not connected")
            return False
    
    def __str__(self):
        """String representation of the device."""
        return f"{self.hostname} ({self.device_type}) - {self.ip_address}"
    
    def __repr__(self):
        """Detailed string representation for debugging."""
        return f"NetworkDevice(hostname='{self.hostname}', ip_address='{self.ip_address}', device_type='{self.device_type}')"


def main():
    """Demonstrate class methods usage."""
    print("=== Network Device Class Methods Demo ===\n")
    
    # Create devices using regular constructor
    print("Creating devices with regular constructor:")
    device1 = NetworkDevice("core-switch-01", "10.0.1.1", "switch")
    device2 = NetworkDevice("edge-router-01", "10.0.1.254", "router")
    print(f"Created: {device1}")
    print(f"Created: {device2}")
    print(f"Total devices created: {NetworkDevice.get_device_count()}\n")
    
    # Create device from dictionary using class method
    print("Creating device from dictionary:")
    device_info = {
        "hostname": "firewall-01",
        "ip_address": "10.0.1.100", 
        "device_type": "firewall"
    }
    device3 = NetworkDevice.from_dict(device_info)
    print(f"Created from dict: {device3}")
    print(f"Total devices: {NetworkDevice.get_device_count()}\n")
    
    # Create device from CSV line using class method
    print("Creating device from CSV line:")
    csv_data = "access-point-01,10.0.2.50,wireless_ap"
    device4 = NetworkDevice.from_csv_line(csv_data)
    print(f"Created from CSV: {device4}")
    print(f"Total devices: {NetworkDevice.get_device_count()}\n")
    
    # Use factory methods
    print("Using factory class methods:")
    router1 = NetworkDevice.create_router("branch-router-01", "10.0.3.1")
    switch1 = NetworkDevice.create_switch("access-switch-01", "10.0.3.10")
    print(f"Factory router: {router1}")
    print(f"Factory switch: {switch1}")
    print(f"Final device count: {NetworkDevice.get_device_count()}\n")
    
    # Demonstrate instance methods
    print("Testing device methods:")
    router1.connect()
    print(router1.get_status())
    backup_file = router1.backup_config()
    
    # Demonstrate config restore with the backup file
    if backup_file:
        router1.restore_config(backup_file)
    
    router1.disconnect()
    print(router1.get_status())
    
    # Try to backup while disconnected
    router1.backup_config()


if __name__ == "__main__":
    main()