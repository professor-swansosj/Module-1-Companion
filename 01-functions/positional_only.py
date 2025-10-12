"""
Positional-Only Arguments Examples
Functions with Parameters that MUST be passed Positionally

Positional-only arguments (before /) force certain parameters to be passed
positionally only, preventing keyword usage. This ensures API consistency
and prevents breaking changes if parameter names change.
"""

def configure_ip_route(destination, mask, next_hop, /, 
                      administrative_distance=1, 
                      interface=None, 
                      permanent=False):
    """
    Configure a static IP route with core parameters as positional-only.
    
    Args:
        destination: Destination network (positional-only)
        mask: Network mask (positional-only)
        next_hop: Next hop IP address (positional-only)
        administrative_distance: Admin distance (keyword allowed, default: 1)
        interface: Outgoing interface (keyword allowed)
        permanent: Make route permanent (keyword allowed, default: False)
    """
    config = f"""
    Static Route Configuration:
    ip route {destination} {mask} {next_hop}"""
    
    if administrative_distance != 1:
        config += f" {administrative_distance}"
    
    if interface:
        config += f" {interface}"
    
    if permanent:
        config += " permanent"
    
    print(config)
    return config

def create_access_list_entry(acl_number, action, protocol, /, 
                           source="any", 
                           destination="any", 
                           port=None, 
                           log=False):
    """
    Create an access list entry with core parameters positional-only.
    
    Args:
        acl_number: ACL number (positional-only)
        action: permit or deny (positional-only)
        protocol: Protocol type (positional-only)
        source: Source address (keyword allowed, default: any)
        destination: Destination address (keyword allowed, default: any)
        port: Port specification (keyword allowed)
        log: Enable logging (keyword allowed, default: False)
    """
    config = f"""
    Access List Entry:
    access-list {acl_number} {action} {protocol} {source} {destination}"""
    
    if port:
        config += f" eq {port}"
    
    if log:
        config += " log"
    
    print(config)
    return config

def configure_vlan_basic(vlan_id, name, /, *, 
                        description="", 
                        shutdown=False, 
                        state="active"):
    """
    Configure basic VLAN with ID and name as positional-only,
    and all other parameters as keyword-only.
    
    Args:
        vlan_id: VLAN ID (positional-only)
        name: VLAN name (positional-only)
        description: VLAN description (keyword-only)
        shutdown: Administrative shutdown (keyword-only, default: False)
        state: VLAN state (keyword-only, default: active)
    """
    config = f"""
    VLAN Configuration:
    vlan {vlan_id}
     name {name}
     state {state}"""
    
    if description:
        config += f"\n     description {description}"
    
    if shutdown:
        config += "\n     shutdown"
    
    print(config)
    return config

def set_interface_ip(interface, ip_address, subnet_mask, /, 
                    description="", 
                    secondary=False):
    """
    Set interface IP address with core parameters positional-only.
    
    Args:
        interface: Interface name (positional-only)
        ip_address: IP address (positional-only)
        subnet_mask: Subnet mask (positional-only)
        description: Interface description (keyword allowed)
        secondary: Secondary IP address (keyword allowed, default: False)
    """
    config = f"""
    Interface IP Configuration:
    interface {interface}"""
    
    if description:
        config += f"\n     description {description}"
    
    ip_command = f"\n     ip address {ip_address} {subnet_mask}"
    if secondary:
        ip_command += " secondary"
    
    config += ip_command
    config += "\n     no shutdown"
    
    print(config)
    return config

def configure_ospf_network(router_id, process_id, network, wildcard, area, /,
                          auto_cost=True,
                          passive_default=False):
    """
    Configure OSPF with core parameters positional-only.
    
    Args:
        router_id: OSPF Router ID (positional-only)
        process_id: OSPF process ID (positional-only)
        network: Network to advertise (positional-only)
        wildcard: Wildcard mask (positional-only)
        area: OSPF area (positional-only)
        auto_cost: Enable auto-cost reference bandwidth (keyword allowed)
        passive_default: Set passive-interface default (keyword allowed)
    """
    config = f"""
    OSPF Configuration:
    router ospf {process_id}
     router-id {router_id}
     network {network} {wildcard} area {area}"""
    
    if auto_cost:
        config += "\n     auto-cost reference-bandwidth 1000"
    
    if passive_default:
        config += "\n     passive-interface default"
    
    print(config)
    return config

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Positional-Only Arguments Practice ===\n")
    
    # Example 1: Static route with positional-only core parameters
    print("1. Static Route Configuration:")
    configure_ip_route("192.168.10.0", "255.255.255.0", "10.1.1.2")
    
    # Example 2: Static route with optional parameters
    print("\n2. Static Route with Admin Distance:")
    configure_ip_route(
        "0.0.0.0", "0.0.0.0", "203.0.113.1",
        administrative_distance=5,
        permanent=True
    )
    
    # Example 3: Access list entry
    print("\n3. Access List Entry:")
    create_access_list_entry(101, "permit", "tcp")
    
    # Example 4: Access list with specific source and destination
    print("\n4. Detailed Access List Entry:")
    create_access_list_entry(
        102, "deny", "tcp",
        source="192.168.1.0 0.0.0.255",
        destination="any", 
        port="80",
        log=True
    )
    
    # Example 5: VLAN with positional-only and keyword-only mix
    print("\n5. VLAN Configuration:")
    configure_vlan_basic(
        100, "FINANCE",
        description="Finance Department VLAN",
        state="active"
    )
    
    # Example 6: Interface IP configuration
    print("\n6. Interface IP Configuration:")
    set_interface_ip(
        "GigabitEthernet0/1", 
        "192.168.1.1", 
        "255.255.255.0",
        description="LAN Interface"
    )
    
    # Example 7: OSPF network configuration
    print("\n7. OSPF Network Configuration:")
    configure_ospf_network(
        "1.1.1.1", 1, "192.168.1.0", "0.0.0.255", 0,
        auto_cost=True,
        passive_default=False
    )
    
    print("\n=== DEMONSTRATING POSITIONAL-ONLY ENFORCEMENT ===")
    
    # This will work - using positional arguments for positional-only parameters
    print("\n✓ Correct Usage:")
    configure_ip_route("10.0.0.0", "255.0.0.0", "192.168.1.1")
    
    print("\n✗ These will cause errors if uncommented:")
    print("# configure_ip_route(destination='10.0.0.0', mask='255.0.0.0', next_hop='192.168.1.1')  # TypeError!")
    print("# create_access_list_entry(acl_number=110, action='permit', protocol='ip')  # TypeError!")
    
    # Try uncommenting these lines to see the errors:
    # configure_ip_route(destination="10.0.0.0", mask="255.0.0.0", next_hop="192.168.1.1")  # Will fail!
    # create_access_list_entry(acl_number=110, action="permit", protocol="ip")  # Will fail!
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Attempt to use keyword arguments for positional-only parameters")
    print("2. Create a function with mixed positional-only and keyword-only parameters")
    print("3. Understand why this restriction might be useful for network device APIs")
    
    # Practice scenarios
    print("\n=== WHEN TO USE POSITIONAL-ONLY ===")
    print("Use positional-only when:")
    print("• Parameter order is logical and unlikely to change")
    print("• You want to prevent keyword usage for core parameters") 
    print("• API consistency is important (like device IP, mask order)")
    print("• Parameter names might change in future versions")
    
    # Challenge: Create your own positional-only function
    def configure_bgp_neighbor(neighbor_ip, remote_as, /, 
                             description="",
                             password=None,
                             update_source=None):
        """
        Configure BGP neighbor with IP and AS as positional-only.
        Complete this function!
        """
        # Your code here
        pass
    
    print("\nChallenge: Complete the configure_bgp_neighbor function above!")
    print("Test it with correct positional usage and try using keywords for the")
    print("positional-only parameters to see the error.")