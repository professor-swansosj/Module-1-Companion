"""
Default Arguments Examples
Network Configuration Functions with Default Values

Default arguments provide sensible fallbacks for parameters, making functions
easier to use while still allowing customization when needed.
"""

def configure_interface_ip(interface, ip_address, subnet_mask="255.255.255.0", 
                          description="", admin_status="up"):
    """
    Configure interface with IP address and optional parameters.
    
    Args:
        interface: Interface name (required)
        ip_address: IP address (required)
        subnet_mask: Subnet mask (default: 255.255.255.0)
        description: Interface description (default: empty)
        admin_status: Admin status - up or down (default: up)
    """
    config = f"""
    Interface Configuration:
    interface {interface}
     ip address {ip_address} {subnet_mask}"""
    
    if description:
        config += f"\n description {description}"
    
    if admin_status == "up":
        config += "\n no shutdown"
    else:
        config += "\n shutdown"
    
    print(config)
    return config

def create_access_list(acl_number, action="permit", protocol="ip", 
                      source="any", destination="any"):
    """
    Create an access list entry with common defaults.
    
    Args:
        acl_number: Access list number (required)
        action: permit or deny (default: permit)
        protocol: Protocol type (default: ip)
        source: Source address (default: any)
        destination: Destination address (default: any)
    """
    config = f"""
    Access List Configuration:
    access-list {acl_number} {action} {protocol} {source} {destination}
    """
    print(config)
    return config

def setup_snmp_community(community_string, access_level="ro", acl_number=None):
    """
    Configure SNMP community with default read-only access.
    
    Args:
        community_string: SNMP community string (required)
        access_level: ro (read-only) or rw (read-write) (default: ro)  
        acl_number: Optional ACL number for access control
    """
    config = f"""
    SNMP Configuration:
    snmp-server community {community_string} {access_level}"""
    
    if acl_number:
        config += f" {acl_number}"
    
    print(config)
    return config

def configure_logging(level="informational", facility="local7", 
                     server_ip=None, console=True):
    """
    Configure system logging with common defaults.
    
    Args:
        level: Logging level (default: informational)
        facility: Syslog facility (default: local7)
        server_ip: Optional syslog server IP
        console: Enable console logging (default: True)
    """
    config = """
    Logging Configuration:"""
    
    config += f"\n logging facility {facility}"
    config += f"\n logging trap {level}"
    
    if console:
        config += f"\n logging console {level}"
    
    if server_ip:
        config += f"\n logging host {server_ip}"
    
    print(config)
    return config

# Example usage and practice exercises  
if __name__ == "__main__":
    print("=== Default Arguments Practice ===\n")
    
    # Example 1: Using all defaults (only required parameters)
    print("1. Interface Configuration - Using Defaults:")
    configure_interface_ip("GigabitEthernet0/1", "192.168.1.1")
    
    # Example 2: Overriding some defaults
    print("2. Interface Configuration - Custom Subnet Mask:")
    configure_interface_ip(
        "GigabitEthernet0/2", 
        "10.1.1.1", 
        subnet_mask="255.255.255.252",
        description="WAN Interface to ISP"
    )
    
    # Example 3: Access list with defaults
    print("3. Access List - Using Defaults:")
    create_access_list(10)
    
    # Example 4: Access list with custom values  
    print("4. Access List - Custom Configuration:")
    create_access_list(
        acl_number=101,
        action="deny", 
        protocol="tcp",
        source="192.168.1.0 0.0.0.255",
        destination="any"
    )
    
    # Example 5: SNMP with defaults
    print("5. SNMP - Default Read-Only:")
    setup_snmp_community("public")
    
    # Example 6: SNMP with ACL restriction
    print("6. SNMP - With ACL Restriction:")
    setup_snmp_community("private", access_level="rw", acl_number=99)
    
    # Example 7: Logging with defaults
    print("7. Logging - Default Configuration:")
    configure_logging()
    
    # Example 8: Logging with syslog server
    print("8. Logging - With Syslog Server:")
    configure_logging(
        level="debugging",
        server_ip="192.168.1.100",
        console=False
    )
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Challenge: Create a switch port configuration function with defaults:")
    print("- Default VLAN: 1")
    print("- Default mode: access")  
    print("- Default speed: auto")
    print("- Default duplex: auto")
    
    # Challenge Exercise: Implement this function
    def configure_switchport(interface, vlan=1, mode="access", 
                           speed="auto", duplex="auto"):
        """
        Configure a switchport with common defaults.
        Complete this function!
        """
        # Your code here
        pass
    
    print("\nTry calling your function with:")
    print("1. Only the interface name")
    print("2. Interface and VLAN only") 
    print("3. All parameters customized")