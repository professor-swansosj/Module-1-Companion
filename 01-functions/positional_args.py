"""
Positional Arguments Examples
Network Configuration Functions with Positional Arguments

In network automation, positional arguments are commonly used when the order
of parameters is logical and consistent (like hostname, IP address, mask).
"""

def configure_interface(hostname, interface, ip_address, subnet_mask):
    """
    Configure a network interface with basic IP settings.
    
    Args:
        hostname: Device hostname
        interface: Interface name (e.g., 'GigabitEthernet0/1')  
        ip_address: Interface IP address
        subnet_mask: Subnet mask for the interface
    """
    config = f"""
    Device: {hostname}
    Interface Configuration:
    interface {interface}
     ip address {ip_address} {subnet_mask}
     no shutdown
    """
    print(config)
    return config

def setup_ospf_area(router_id, area_id, network, wildcard):
    """
    Configure OSPF for a specific network area.
    
    Args:
        router_id: OSPF router ID
        area_id: OSPF area number
        network: Network address
        wildcard: Wildcard mask
    """
    config = f"""
    OSPF Configuration:
    router ospf 1
     router-id {router_id}
     network {network} {wildcard} area {area_id}
    """
    print(config)
    return config

def create_vlan(switch_name, vlan_id, vlan_name):
    """
    Create a VLAN with a specific ID and name.
    
    Args:
        switch_name: Name of the switch
        vlan_id: VLAN ID number
        vlan_name: Descriptive name for the VLAN
    """
    config = f"""
    Switch: {switch_name}
    VLAN Configuration:
    vlan {vlan_id}
     name {vlan_name}
    """
    print(config)
    return config

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Positional Arguments Practice ===\n")
    
    # Example 1: Basic interface configuration
    print("1. Basic Interface Configuration:")
    configure_interface("R1", "GigabitEthernet0/1", "192.168.1.1", "255.255.255.0")
    
    # Example 2: OSPF configuration  
    print("2. OSPF Configuration:")
    setup_ospf_area("1.1.1.1", 0, "192.168.1.0", "0.0.0.255")
    
    # Example 3: VLAN creation
    print("3. VLAN Creation:")
    create_vlan("SW1", 10, "SALES")
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Modify configure_interface() to support different interface types")
    print("2. Create a function that takes 3 positional arguments for static route configuration")
    print("3. Call the functions above with different values")
    
    # Practice Exercise 1: Different interface types
    # Uncomment and complete:
    # configure_interface("R2", "Serial0/0/0", "10.1.1.1", "255.255.255.252")
    
    # Practice Exercise 2: Create your own function
    # def configure_static_route(destination, mask, next_hop):
    #     # Your code here
    #     pass
    
    # Practice Exercise 3: Try calling with wrong number of arguments
    # What happens if you call: configure_interface("R1", "Gi0/1")  # Missing arguments?