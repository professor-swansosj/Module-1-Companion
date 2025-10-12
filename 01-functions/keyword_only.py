"""
Keyword-Only Arguments Examples
Functions with Parameters that MUST be passed as Keywords

Keyword-only arguments (after *) force certain parameters to be passed
as keywords, making function calls more explicit and preventing errors.
"""

def configure_secure_connection(hostname, username, *, 
                              password=None, ssh_key=None, 
                              port=22, timeout=30, 
                              enable_password=None):
    """
    Establish a secure connection to a network device.
    
    Args:
        hostname: Device hostname or IP (positional)
        username: Username for authentication (positional)
        password: Password for authentication (keyword-only)
        ssh_key: Path to SSH key file (keyword-only)
        port: SSH port number (keyword-only, default: 22)
        timeout: Connection timeout (keyword-only, default: 30)
        enable_password: Enable mode password (keyword-only)
    """
    # Validate authentication method
    if not password and not ssh_key:
        raise ValueError("Either password or ssh_key must be provided")
    
    auth_method = "SSH Key" if ssh_key else "Password"
    
    connection_info = f"""
    Secure Connection Configuration:
    Target: {hostname}:{port}
    Username: {username}
    Authentication: {auth_method}
    Timeout: {timeout} seconds"""
    
    if ssh_key:
        connection_info += f"\n    SSH Key: {ssh_key}"
    
    if enable_password:
        connection_info += "\n    Enable Mode: Configured"
    
    print(connection_info)
    return {
        'hostname': hostname,
        'username': username,
        'port': port,
        'timeout': timeout,
        'auth_method': auth_method
    }

def create_vlan_with_security(vlan_id, vlan_name, *, 
                             shutdown=False,
                             private_vlan=False,
                             storm_control=False,
                             dhcp_snooping=True,
                             arp_inspection=False):
    """
    Create a VLAN with security features (all security options are keyword-only).
    
    Args:
        vlan_id: VLAN ID number (positional)
        vlan_name: VLAN name (positional)
        shutdown: Shutdown the VLAN (keyword-only, default: False)
        private_vlan: Enable private VLAN (keyword-only, default: False)
        storm_control: Enable storm control (keyword-only, default: False)
        dhcp_snooping: Enable DHCP snooping (keyword-only, default: True)
        arp_inspection: Enable ARP inspection (keyword-only, default: False)
    """
    config = f"""
    VLAN Configuration:
    vlan {vlan_id}
     name {vlan_name}"""
    
    security_features = []
    
    if shutdown:
        config += "\n     shutdown"
        security_features.append("Shutdown")
    
    if private_vlan:
        config += "\n     private-vlan community"
        security_features.append("Private VLAN")
    
    if dhcp_snooping:
        config += f"\n    ip dhcp snooping vlan {vlan_id}"
        security_features.append("DHCP Snooping")
    
    if arp_inspection:
        config += f"\n    ip arp inspection vlan {vlan_id}"
        security_features.append("ARP Inspection")
    
    if storm_control:
        config += """
    interface range switchport
     storm-control broadcast level 10.00
     storm-control multicast level 10.00"""
        security_features.append("Storm Control")
    
    config += f"\n\n    Security Features Enabled: {', '.join(security_features) if security_features else 'None'}"
    
    print(config)
    return config

def setup_qos_policy(policy_name, *, 
                    priority_queue=None,
                    bandwidth_limit=None,
                    dscp_marking=None,
                    policing_rate=None,
                    shaping_rate=None):
    """
    Configure Quality of Service (QoS) policy.
    All QoS parameters must be specified as keywords for clarity.
    
    Args:
        policy_name: Name of the QoS policy (positional)
        priority_queue: Priority queue number (keyword-only)
        bandwidth_limit: Bandwidth limit in Mbps (keyword-only)
        dscp_marking: DSCP value for packet marking (keyword-only)
        policing_rate: Police rate in bps (keyword-only)
        shaping_rate: Shaping rate in bps (keyword-only)
    """
    config = f"""
    QoS Policy Configuration:
    policy-map {policy_name}"""
    
    if priority_queue is not None:
        config += f"""
     class class-default
      priority level {priority_queue}"""
    
    if bandwidth_limit:
        config += f"""
      bandwidth {bandwidth_limit}"""
    
    if dscp_marking is not None:
        config += f"""
      set dscp {dscp_marking}"""
    
    if policing_rate:
        config += f"""
      police rate {policing_rate}"""
    
    if shaping_rate:
        config += f"""
      shape average {shaping_rate}"""
    
    if not any([priority_queue, bandwidth_limit, dscp_marking, policing_rate, shaping_rate]):
        config += """
     class class-default
      ! No QoS parameters specified"""
    
    print(config)
    return config

def configure_interface_advanced(interface, ip_address, *, 
                               subnet_mask="255.255.255.0",
                               mtu=1500,
                               bandwidth=None,
                               delay=None,
                               load_interval=300,
                               keepalive=10):
    """
    Configure interface with advanced parameters that must be keywords.
    
    Args:
        interface: Interface name (positional)
        ip_address: IP address (positional)
        subnet_mask: Subnet mask (keyword-only, default: 255.255.255.0)
        mtu: Maximum Transmission Unit (keyword-only, default: 1500)
        bandwidth: Interface bandwidth in Kbps (keyword-only)
        delay: Interface delay in microseconds (keyword-only)
        load_interval: Load calculation interval (keyword-only, default: 300)
        keepalive: Keepalive timer in seconds (keyword-only, default: 10)
    """
    config = f"""
    Advanced Interface Configuration:
    interface {interface}
     ip address {ip_address} {subnet_mask}
     mtu {mtu}
     load-interval {load_interval}
     keepalive {keepalive}"""
    
    if bandwidth:
        config += f"\n     bandwidth {bandwidth}"
    
    if delay:
        config += f"\n     delay {delay}"
    
    config += "\n     no shutdown"
    
    print(config)
    return config

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Keyword-Only Arguments Practice ===\n")
    
    # Example 1: Secure connection with password
    print("1. Secure Connection - Password Authentication:")
    try:
        configure_secure_connection(
            "192.168.1.1", 
            "admin",
            password="cisco123",
            enable_password="enable123",
            timeout=60
        )
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example 2: Secure connection with SSH key
    print("\n2. Secure Connection - SSH Key Authentication:")
    configure_secure_connection(
        "router.company.com",
        "netadmin", 
        ssh_key="/home/user/.ssh/id_rsa",
        port=2022
    )
    
    # Example 3: VLAN with security features
    print("\n3. VLAN with Security Features:")
    create_vlan_with_security(
        100, 
        "SECURE_FINANCE",
        dhcp_snooping=True,
        arp_inspection=True,
        storm_control=True
    )
    
    # Example 4: QoS policy configuration
    print("\n4. QoS Policy Configuration:")
    setup_qos_policy(
        "VOICE_POLICY",
        priority_queue=1,
        bandwidth_limit=256,
        dscp_marking=46
    )
    
    # Example 5: Advanced interface configuration
    print("\n5. Advanced Interface Configuration:")
    configure_interface_advanced(
        "GigabitEthernet0/1",
        "10.1.1.1",
        subnet_mask="255.255.255.252",
        mtu=1500,
        bandwidth=1000000,
        delay=100
    )
    
    print("\n=== DEMONSTRATING KEYWORD-ONLY ENFORCEMENT ===")
    
    # This will work - using keywords for keyword-only parameters
    print("\n✓ Correct Usage:")
    configure_secure_connection("192.168.1.1", "admin", password="test123")
    
    # Uncomment the following to see errors:
    print("\n✗ These will cause errors if uncommented:")
    print("# configure_secure_connection('192.168.1.1', 'admin', 'test123')  # TypeError!")
    print("# create_vlan_with_security(200, 'TEST', True)  # TypeError!")
    
    # Try uncommenting these lines to see the errors:
    # configure_secure_connection("192.168.1.1", "admin", "test123")  # Will fail!
    # create_vlan_with_security(200, "TEST", True)  # Will fail!
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("1. Try calling functions with positional arguments where keywords are required")
    print("2. Create a function that forces security settings to be keyword-only")
    print("3. Experiment with the error messages you get")
    
    # Challenge: Create your own keyword-only function
    def configure_firewall_rule(rule_name, action, *, 
                               source="any", 
                               destination="any", 
                               protocol="ip",
                               logging=False):
        """
        Configure firewall rule with keyword-only parameters.
        Complete this function!
        """
        # Your code here
        pass
    
    print("\nChallenge: Complete the configure_firewall_rule function above!")
    print("Then test it with both correct and incorrect parameter usage")