"""
Main script demonstrating how to import and use custom modules.

This script shows different ways to import functions and classes
from the network_utils package and use them in network automation tasks.
"""

import sys
import os

# Add the current directory to Python path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Different import styles
import network_utils
from network_utils import configure_interface, NetworkDevice
from network_utils.device_config import configure_vlan, backup_configuration
from network_utils.network_devices import Router, Switch, create_network_topology


def demonstrate_imports():
    """Demonstrate various import methods and usage."""
    print("=== Network Automation Module Import Demo ===\n")
    
    # 1. Using package-level imports
    print("1. Using package-level imports:")
    print(f"Network Utils version: {network_utils.__version__}")
    print(f"Description: {network_utils.__description__}\n")
    
    # 2. Using imported function directly
    print("2. Using directly imported function:")
    configure_interface("router-01", "GigabitEthernet0/0", "192.168.1.1", "255.255.255.0", "WAN Interface")
    print()
    
    # 3. Using module.function syntax
    print("3. Using module.function syntax:")
    network_utils.configure_vlan("switch-01", 100, "Production", ["FastEthernet0/1", "FastEthernet0/2"])
    print()
    
    # 4. Using imported classes
    print("4. Creating devices with imported classes:")
    router = Router("core-router", "10.0.0.1", "Cisco")
    switch = Switch("access-switch", "10.0.0.10", "Cisco")
    
    print(f"Created router: {router}")
    print(f"Created switch: {switch}")
    print()
    
    # 5. Configure the devices
    print("5. Configuring devices:")
    router.connect()
    router.configure_interface("GigabitEthernet0/0", "10.0.0.1", "255.255.255.0", "Management")
    router.add_static_route("0.0.0.0/0", "10.0.0.254")
    router.show_interfaces()
    
    switch.connect()
    switch.create_vlan(10, "Data")
    switch.create_vlan(20, "Voice")
    switch.configure_port("FastEthernet0/1", 10, "access", "User Port 1")
    switch.configure_port("FastEthernet0/2", 20, "access", "Phone Port 1")
    switch.show_vlans()
    
    # 6. Backup configurations
    print("\n6. Backing up configurations:")
    router_backup = router.backup_config()
    switch_backup = switch.backup_config()
    
    # Also use the imported backup function
    backup_configuration("firewall-01", "running", "backups")
    
    # 7. Create a full network topology
    print("\n7. Creating network topology:")
    devices = create_network_topology()
    
    print("Network topology created with the following devices:")
    for device in devices:
        print(f"  - {device}")
    
    # Connect to all devices and show their status
    print("\nConnecting to all devices:")
    for device in devices:
        device.connect()
        print(f"  {device.get_status()}")
    
    # Show configuration details for routers
    print("\nRouter configurations:")
    for device in devices:
        if isinstance(device, Router):
            device.show_interfaces()
            device.show_routing_table()
    
    # Show VLAN configurations for switches
    print("\nSwitch configurations:")
    for device in devices:
        if isinstance(device, Switch):
            device.show_vlans()


def demonstrate_best_practices():
    """Demonstrate import best practices."""
    print("\n=== Import Best Practices Demo ===\n")
    
    # Good practice: Import only what you need
    from network_utils.device_config import configure_ospf
    from network_utils.network_devices import NetworkDevice
    
    # Create a device and configure OSPF
    device = NetworkDevice("ospf-router", "10.0.0.5", "router", "Cisco")
    device.connect()
    
    ospf_networks = [
        {"network": "10.0.0.0/24", "area": "0"},
        {"network": "192.168.1.0/24", "area": "1"}
    ]
    
    configure_ospf("ospf-router", 1, "1.1.1.1", ospf_networks)
    
    # Good practice: Use aliasing for long module names
    import network_utils.device_config as device_cfg
    
    # Generate a configuration template
    template = device_cfg.generate_config_template("router", "template-router")
    print("\nGenerated configuration template:")
    print(template[:200] + "..." if len(template) > 200 else template)


if __name__ == "__main__":
    try:
        demonstrate_imports()
        demonstrate_best_practices()
        
        print("\n=== Demo completed successfully! ===")
        print("\nKey takeaways:")
        print("1. Import only what you need for better performance")
        print("2. Use package-level imports for convenience") 
        print("3. Organize related functionality into modules")
        print("4. Use __init__.py to control package interface")
        print("5. Follow consistent naming conventions")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure all module files are in the correct location")
    except Exception as e:
        print(f"Error during demo: {e}")
        import traceback
        traceback.print_exc()