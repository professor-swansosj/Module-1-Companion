"""
Variable-Length Keyword Arguments (**kwargs) Examples
Functions that Accept Any Number of Keyword Arguments

**kwargs allows functions to accept any number of keyword arguments,
perfect for flexible device configuration where different devices
may support different parameters.
"""

def configure_device_settings(hostname, **config_options):
    """
    Configure a network device with flexible configuration options.
    
    Args:
        hostname: Device hostname (required)
        **config_options: Any number of configuration key-value pairs
    """
    print(f"\nConfiguring device: {hostname}")
    print("Configuration Settings:")
    
    if not config_options:
        print("  No additional configuration specified")
        return
    
    config = f"\nDevice: {hostname}\nConfiguration:"
    
    # Handle common configuration options
    for option, value in config_options.items():
        if option == "enable_secret":
            config += f"\n  enable secret {value}"
        elif option == "hostname":
            config += f"\n  hostname {value}"  
        elif option == "domain_name":
            config += f"\n  ip domain-name {value}"
        elif option == "ntp_server":
            config += f"\n  ntp server {value}"
        elif option == "timezone":
            config += f"\n  clock timezone {value}"
        elif option == "logging_server":
            config += f"\n  logging host {value}"
        elif option == "snmp_community":
            config += f"\n  snmp-server community {value}"
        else:
            # Generic option
            config += f"\n  {option} {value}"
    
    print(config)
    return config

def create_interface_config(interface_name, **interface_settings):
    """
    Configure an interface with flexible settings.
    
    Args:
        interface_name: Name of the interface
        **interface_settings: Flexible interface configuration options
    """
    config = f"""
    Interface: {interface_name}
    interface {interface_name}"""
    
    # Process interface settings
    for setting, value in interface_settings.items():
        if setting == "ip_address" and "subnet_mask" in interface_settings:
            config += f"\n     ip address {value} {interface_settings['subnet_mask']}"
        elif setting == "subnet_mask":
            continue  # Already handled with ip_address
        elif setting == "description":
            config += f"\n     description {value}"
        elif setting == "speed":
            config += f"\n     speed {value}"
        elif setting == "duplex":
            config += f"\n     duplex {value}"
        elif setting == "access_vlan":
            config += f"\n     switchport access vlan {value}"
        elif setting == "trunk_vlans":
            config += f"\n     switchport trunk allowed vlan {value}"
        elif setting == "port_security":
            if value:
                config += "\n     switchport port-security"
        elif setting == "shutdown":
            if value:
                config += "\n     shutdown"
            else:
                config += "\n     no shutdown"
        else:
            config += f"\n     {setting} {value}"
    
    print(config)
    return config

def setup_routing_protocol(router_name, protocol_type, **protocol_settings):
    """
    Configure routing protocols with flexible parameters.
    
    Args:
        router_name: Router hostname
        protocol_type: Type of routing protocol (ospf, eigrp, bgp)
        **protocol_settings: Protocol-specific settings
    """
    config = f"""
    Router: {router_name}
    Routing Protocol: {protocol_type.upper()}"""
    
    if protocol_type.lower() == "ospf":
        process_id = protocol_settings.get("process_id", 1)
        config += f"\n    router ospf {process_id}"
        
        if "router_id" in protocol_settings:
            config += f"\n     router-id {protocol_settings['router_id']}"
        
        if "networks" in protocol_settings:
            for network_info in protocol_settings["networks"]:
                network, wildcard, area = network_info
                config += f"\n     network {network} {wildcard} area {area}"
    
    elif protocol_type.lower() == "eigrp":
        as_number = protocol_settings.get("as_number", 100)
        config += f"\n    router eigrp {as_number}"
        
        if "networks" in protocol_settings:
            for network in protocol_settings["networks"]:
                config += f"\n     network {network}"
    
    elif protocol_type.lower() == "bgp":
        as_number = protocol_settings.get("as_number", 65000)
        config += f"\n    router bgp {as_number}"
        
        if "router_id" in protocol_settings:
            config += f"\n     bgp router-id {protocol_settings['router_id']}"
        
        if "neighbors" in protocol_settings:
            for neighbor_info in protocol_settings["neighbors"]:
                neighbor_ip, remote_as = neighbor_info
                config += f"\n     neighbor {neighbor_ip} remote-as {remote_as}"
    
    print(config)
    return config

def deploy_security_policy(device_name, **security_settings):
    """
    Apply security policies with flexible options.
    
    Args:
        device_name: Name of the device
        **security_settings: Various security configuration options
    """
    print(f"\nApplying security policy to: {device_name}")
    
    applied_policies = []
    
    for policy, setting in security_settings.items():
        if policy == "password_encryption" and setting:
            print("  ✓ Enabling password encryption")
            applied_policies.append("service password-encryption")
        
        elif policy == "ssh_version" and setting:
            print(f"  ✓ Configuring SSH version {setting}")
            applied_policies.append(f"ip ssh version {setting}")
        
        elif policy == "login_banner" and setting:
            print("  ✓ Configuring login banner")
            applied_policies.append(f'banner login ^{setting}^')
        
        elif policy == "exec_timeout" and setting:
            print(f"  ✓ Setting exec timeout to {setting}")
            applied_policies.append(f"line console 0\n exec-timeout {setting}")
        
        elif policy == "max_login_attempts" and setting:
            print(f"  ✓ Setting max login attempts to {setting}")
            applied_policies.append(f"login block-for 60 attempts {setting} within 120")
    
    return applied_policies

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Variable-Length Keyword Arguments (**kwargs) Practice ===\n")
    
    # Example 1: Basic device configuration
    print("1. Basic Device Configuration:")
    configure_device_settings(
        "R1",
        enable_secret="cisco123",
        domain_name="company.com",
        ntp_server="192.168.1.100",
        timezone="EST -5 0"
    )
    
    # Example 2: Interface configuration - Layer 3
    print("\n2. Layer 3 Interface Configuration:")
    create_interface_config(
        "GigabitEthernet0/1",
        ip_address="192.168.1.1",
        subnet_mask="255.255.255.0",
        description="LAN Interface",
        shutdown=False
    )
    
    # Example 3: Interface configuration - Layer 2
    print("\n3. Layer 2 Interface Configuration:")
    create_interface_config(
        "GigabitEthernet0/2",
        description="Access Port for PC",
        access_vlan=10,
        speed="100",
        duplex="full",
        port_security=True
    )
    
    # Example 4: OSPF configuration
    print("\n4. OSPF Protocol Configuration:")
    ospf_networks = [
        ("192.168.1.0", "0.0.0.255", "0"),
        ("10.1.1.0", "0.0.0.3", "0")
    ]
    setup_routing_protocol(
        "R1", 
        "ospf",
        process_id=1,
        router_id="1.1.1.1",
        networks=ospf_networks
    )
    
    # Example 5: BGP configuration
    print("\n5. BGP Protocol Configuration:")
    bgp_neighbors = [
        ("10.1.1.2", "65001"),
        ("203.0.113.1", "65002")
    ]
    setup_routing_protocol(
        "R1",
        "bgp", 
        as_number=65000,
        router_id="1.1.1.1",
        neighbors=bgp_neighbors
    )
    
    # Example 6: Security policy deployment
    print("\n6. Security Policy Deployment:")
    deploy_security_policy(
        "R1",
        password_encryption=True,
        ssh_version=2,
        login_banner="Authorized Access Only!",
        exec_timeout="5 0",
        max_login_attempts=3
    )
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Configure a device with logging and SNMP settings")
    print("2. Create a trunk interface configuration")
    print("3. Set up EIGRP with multiple networks")
    
    # Practice Exercise 1
    print("\nPractice 1 - Device with Logging:")
    configure_device_settings(
        "SW1",
        logging_server="192.168.1.200",
        snmp_community="private",
        enable_secret="switch123"
    )
    
    # Practice Exercise 2 - Your turn!
    print("\nPractice 2 - Trunk Interface:")
    # create_interface_config("GigabitEthernet0/24", ...)  # Complete this
    
    # Practice Exercise 3 - Your turn!
    print("\nPractice 3 - EIGRP Configuration:")
    # eigrp_networks = ["192.168.0.0", "10.0.0.0"]
    # setup_routing_protocol("R2", "eigrp", as_number=100, networks=eigrp_networks)
    
    print("\nChallenge: Create your own **kwargs function!")
    print("Try creating a function that configures multiple VLANs with flexible properties")