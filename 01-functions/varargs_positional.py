"""
Variable-Length Positional Arguments (*args) Examples
Functions that Accept Any Number of Positional Arguments

*args allows functions to accept any number of positional arguments,
making them flexible for batch operations common in network automation.
"""

def configure_multiple_vlans(switch_name, *vlan_ids):
    """
    Configure multiple VLANs on a switch using *args.
    
    Args:
        switch_name: Name of the switch (required)
        *vlan_ids: Variable number of VLAN IDs to configure
    """
    if not vlan_ids:
        print(f"No VLANs specified for switch {switch_name}")
        return
    
    config = f"""
    Switch: {switch_name}
    VLAN Configuration:"""
    
    for vlan_id in vlan_ids:
        config += f"""
    vlan {vlan_id}
     name VLAN_{vlan_id}"""
    
    print(config)
    return config

def backup_device_configs(*device_hostnames):
    """
    Simulate backing up configurations for multiple devices.
    
    Args:
        *device_hostnames: Variable number of device hostnames
    """
    if not device_hostnames:
        print("No devices specified for backup")
        return
    
    print("Starting backup process...")
    backup_results = []
    
    for hostname in device_hostnames:
        # Simulate backup process
        result = f"✓ Successfully backed up configuration for {hostname}"
        print(f"  {result}")
        backup_results.append(result)
    
    print(f"\nBackup completed for {len(device_hostnames)} device(s)")
    return backup_results

def configure_static_routes(router_name, *route_info):
    """
    Configure multiple static routes on a router.
    
    Args:
        router_name: Router hostname (required)
        *route_info: Tuples of (destination, mask, next_hop)
    """
    if not route_info:
        print(f"No routes specified for router {router_name}")
        return
    
    config = f"""
    Router: {router_name}
    Static Route Configuration:"""
    
    for route in route_info:
        if len(route) >= 3:  # Ensure tuple has at least 3 elements
            destination, mask, next_hop = route[:3]  # Take first 3 elements
            config += f"\n    ip route {destination} {mask} {next_hop}"
        else:
            print(f"Warning: Invalid route tuple {route} - skipping")
    
    print(config)
    return config

def ping_test(*ip_addresses):
    """
    Simulate ping tests to multiple IP addresses.
    
    Args:
        *ip_addresses: Variable number of IP addresses to ping
    """
    if not ip_addresses:
        print("No IP addresses specified for ping test")
        return
    
    print("Network Connectivity Test Results:")
    results = {}
    
    for ip in ip_addresses:
        # Simulate ping test (randomly successful or failed for demo)
        import random
        success = random.choice([True, True, True, False])  # 75% success rate
        
        if success:
            print(f"  {ip} - ✓ Reachable (Response time: {random.randint(1, 50)}ms)")
            results[ip] = "Reachable"
        else:
            print(f"  {ip} - ✗ Unreachable (Request timeout)")
            results[ip] = "Unreachable"
    
    return results

def show_interface_status(*interface_names):
    """
    Display status information for multiple interfaces.
    
    Args:
        *interface_names: Variable number of interface names
    """
    if not interface_names:
        print("No interfaces specified")
        return
    
    print("Interface Status Report:")
    print("-" * 60)
    print(f"{'Interface':<20} {'Status':<10} {'Protocol':<10} {'Speed':<15}")
    print("-" * 60)
    
    import random
    statuses = ["up", "down", "administratively down"]
    protocols = ["up", "down"]
    speeds = ["1000", "100", "10", "auto"]
    
    for interface in interface_names:
        status = random.choice(statuses)
        protocol = random.choice(protocols) if status == "up" else "down"
        speed = random.choice(speeds) if status == "up" else "n/a"
        
        print(f"{interface:<20} {status:<10} {protocol:<10} {speed:<15}")

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Variable-Length Positional Arguments (*args) Practice ===\n")
    
    # Example 1: Configure multiple VLANs
    print("1. Configure Multiple VLANs:")
    configure_multiple_vlans("SW1", 10, 20, 30, 40)
    
    # Example 2: Backup multiple devices
    print("\n2. Backup Multiple Device Configurations:")
    backup_device_configs("R1", "R2", "SW1", "SW2", "ASA1")
    
    # Example 3: Configure static routes (using tuples)
    print("\n3. Configure Multiple Static Routes:")
    routes = [
        ("192.168.10.0", "255.255.255.0", "10.1.1.2"),
        ("192.168.20.0", "255.255.255.0", "10.1.1.2"),
        ("0.0.0.0", "0.0.0.0", "203.0.113.1")  # Default route
    ]
    # Unpack the list into individual arguments
    configure_static_routes("R1", *routes)
    
    # Example 4: Ping test multiple addresses
    print("\n4. Network Connectivity Tests:")
    ping_results = ping_test("8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.0.1")
    
    # Example 5: Show interface status
    print("\n5. Interface Status Check:")
    show_interface_status("GigabitEthernet0/1", "GigabitEthernet0/2", 
                         "Serial0/0/0", "Loopback0")
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Call configure_multiple_vlans with just one VLAN")
    print("2. Call backup_device_configs with no arguments")
    print("3. Create your own function that accepts *args")
    
    # Practice Exercise 1: Single VLAN
    print("\nPractice 1 - Single VLAN:")
    configure_multiple_vlans("SW2", 100)
    
    # Practice Exercise 2: No arguments  
    print("\nPractice 2 - No Device Arguments:")
    backup_device_configs()
    
    # Practice Exercise 3: Your turn!
    print("\nPractice 3 - Create Your Own *args Function:")
    print("Challenge: Create a function that configures access-lists on multiple interfaces")
    
    def apply_acl_to_interfaces(acl_name, direction, *interfaces):
        """
        Apply an ACL to multiple interfaces.
        
        Args:
            acl_name: Name or number of the ACL
            direction: 'in' or 'out'  
            *interfaces: Variable number of interface names
        """
        # Your code here!
        pass
    
    # Uncomment to test your function:
    # apply_acl_to_interfaces("BLOCK_HTTP", "in", "Gi0/1", "Gi0/2", "Gi0/3")