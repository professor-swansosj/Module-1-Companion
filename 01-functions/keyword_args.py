"""
Keyword Arguments Examples
Network Configuration Functions with Keyword Arguments

Keyword arguments make function calls more readable and allow parameters
to be passed in any order. Very useful for network device configuration
where you might have many optional parameters.
"""

def configure_vlan_advanced(switch_name, vlan_id, vlan_name, description="", shutdown=False):
    """
    Configure a VLAN with advanced options using keyword arguments.
    
    Args:
        switch_name: Name of the switch
        vlan_id: VLAN ID number
        vlan_name: Name for the VLAN
        description: Optional VLAN description
        shutdown: Whether to shutdown the VLAN (default: False)
    """
    config = f"""
    Switch: {switch_name}
    VLAN Configuration:
    vlan {vlan_id}
     name {vlan_name}"""
    
    if description:
        config += f"\n description {description}"
    if shutdown:
        config += "\n shutdown"
    
    print(config)
    return config

def setup_interface_security(interface, port_security=True, max_addresses=1, 
                           violation_action="shutdown", aging_time=0):
    """
    Configure port security settings using keyword arguments.
    
    Args:
        interface: Interface name
        port_security: Enable port security (default: True)
        max_addresses: Maximum MAC addresses allowed (default: 1)
        violation_action: Action on violation - shutdown, restrict, protect
        aging_time: Aging time in minutes (0 = disabled)
    """
    config = f"\nInterface {interface} Security Configuration:"
    
    if port_security:
        config += f"""
    interface {interface}
     switchport port-security
     switchport port-security maximum {max_addresses}
     switchport port-security violation {violation_action}"""
        
        if aging_time > 0:
            config += f"\n switchport port-security aging time {aging_time}"
    
    print(config)
    return config

def configure_ospf_network(router_id, process_id=1, area=0, network="", 
                          wildcard="", passive_interfaces=None):
    """
    Configure OSPF with flexible keyword arguments.
    
    Args:
        router_id: OSPF Router ID
        process_id: OSPF process ID (default: 1)
        area: OSPF area (default: 0) 
        network: Network to advertise
        wildcard: Wildcard mask
        passive_interfaces: List of passive interfaces
    """
    if passive_interfaces is None:
        passive_interfaces = []
    
    config = f"""
    OSPF Configuration:
    router ospf {process_id}
     router-id {router_id}"""
    
    if network and wildcard:
        config += f"\n network {network} {wildcard} area {area}"
    
    for interface in passive_interfaces:
        config += f"\n passive-interface {interface}"
    
    print(config)
    return config

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Keyword Arguments Practice ===\n")
    
    # Example 1: VLAN configuration with keywords
    print("1. VLAN Configuration with Keywords:")
    configure_vlan_advanced(
        switch_name="SW1",
        vlan_id=20, 
        vlan_name="FINANCE",
        description="Finance Department VLAN"
    )
    
    # Example 2: Same function, different parameter order
    print("\n2. Same Function, Different Order:")
    configure_vlan_advanced(
        vlan_name="GUEST_WIFI",
        vlan_id=99,
        switch_name="SW2",
        shutdown=True,
        description="Guest WiFi Network"
    )
    
    # Example 3: Port security configuration
    print("\n3. Port Security Configuration:")
    setup_interface_security(
        interface="GigabitEthernet0/1",
        max_addresses=2,
        violation_action="restrict",
        aging_time=30
    )
    
    # Example 4: OSPF with passive interfaces
    print("\n4. OSPF with Passive Interfaces:")
    configure_ospf_network(
        router_id="1.1.1.1",
        network="192.168.10.0",
        wildcard="0.0.0.255",
        passive_interfaces=["GigabitEthernet0/0", "Loopback0"]
    )
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Call configure_vlan_advanced() with parameters in different orders")
    print("2. Create an OSPF function that uses only keyword arguments")
    print("3. Experiment with omitting optional parameters")
    
    # Practice Exercise 1: Different parameter orders
    # Try calling the same function with parameters in different orders
    
    # Practice Exercise 2: Create your own keyword-based function
    # def configure_access_list(acl_name, permit_deny, protocol, source, destination="any"):
    #     # Your code here
    #     pass
    
    # Practice Exercise 3: What happens with typos in keyword names?
    # Try: configure_vlan_advanced(switch="SW1", vlan_id=30, vlan_name="TEST")