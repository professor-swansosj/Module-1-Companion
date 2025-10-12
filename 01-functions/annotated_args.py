"""
Annotated Arguments Examples (Type Hints)
Functions with Type Annotations for Network Automation

Type annotations help document expected data types, improve code readability,
catch errors early, and provide better IDE support. Essential for large
network automation projects.
"""

from typing import List, Dict, Tuple, Optional, Union
from ipaddress import IPv4Address, IPv4Network

def configure_interface_typed(
    hostname: str,
    interface: str, 
    ip_address: str,
    subnet_mask: str,
    description: Optional[str] = None,
    admin_up: bool = True
) -> Dict[str, Union[str, bool]]:
    """
    Configure network interface with type annotations.
    
    Args:
        hostname: Device hostname
        interface: Interface name (e.g., 'GigabitEthernet0/1')
        ip_address: IPv4 address as string
        subnet_mask: Subnet mask as string  
        description: Optional interface description
        admin_up: Administrative status (True=no shutdown)
    
    Returns:
        Dictionary containing configuration result
    """
    config = f"""
    Device: {hostname}
    Interface: {interface}
    IP Address: {ip_address} {subnet_mask}"""
    
    if description:
        config += f"\n    Description: {description}"
    
    config += f"\n    Status: {'Enabled' if admin_up else 'Disabled'}"
    
    print(config)
    
    return {
        'hostname': hostname,
        'interface': interface,
        'ip_configured': True,
        'admin_up': admin_up
    }

def configure_vlans_batch(
    switch_name: str,
    vlan_configs: List[Dict[str, Union[str, int, bool]]]
) -> List[str]:
    """
    Configure multiple VLANs from a list of configuration dictionaries.
    
    Args:
        switch_name: Switch hostname
        vlan_configs: List of VLAN configuration dictionaries
                     Each dict should contain: id, name, description (optional)
    
    Returns:
        List of configuration commands generated
    """
    commands = []
    
    print(f"Configuring VLANs on switch: {switch_name}")
    
    for vlan_config in vlan_configs:
        vlan_id = vlan_config['id']
        vlan_name = vlan_config['name']
        description = vlan_config.get('description', '')
        
        command = f"vlan {vlan_id}"
        commands.append(command)
        
        command = f" name {vlan_name}"
        commands.append(command)
        
        if description:
            command = f" description {description}"
            commands.append(command)
        
        print(f"  VLAN {vlan_id}: {vlan_name}")
    
    return commands

def setup_ospf_areas(
    router_name: str,
    router_id: IPv4Address,
    areas: Dict[int, List[IPv4Network]]
) -> Tuple[bool, List[str]]:
    """
    Configure OSPF areas with networks using IP address objects.
    
    Args:
        router_name: Router hostname
        router_id: OSPF Router ID as IPv4Address object
        areas: Dictionary mapping area IDs to lists of networks
    
    Returns:
        Tuple of (success: bool, commands: List[str])
    """
    try:
        commands = []
        
        print(f"Configuring OSPF on router: {router_name}")
        print(f"Router ID: {router_id}")
        
        commands.append("router ospf 1")
        commands.append(f"router-id {router_id}")
        
        for area_id, networks in areas.items():
            print(f"  Area {area_id}:")
            
            for network in networks:
                # Calculate wildcard mask from network
                wildcard = IPv4Address(int(IPv4Address('255.255.255.255')) ^ int(network.netmask))
                
                command = f"network {network.network_address} {wildcard} area {area_id}"
                commands.append(command)
                print(f"    Network: {network}")
        
        return True, commands
    
    except Exception as e:
        print(f"Error configuring OSPF: {e}")
        return False, []

def create_firewall_rules(
    device_name: str,
    rules: List[Tuple[str, str, str, str, Optional[int]]]
) -> Dict[str, Union[int, List[str]]]:
    """
    Create firewall rules from a list of tuples.
    
    Args:
        device_name: Firewall device name
        rules: List of tuples containing (action, protocol, source, dest, port)
               Port is optional (None for any port)
    
    Returns:
        Dictionary with rule count and generated commands
    """
    commands = []
    rule_count = 0
    
    print(f"Creating firewall rules for: {device_name}")
    
    for rule in rules:
        action, protocol, source, destination, port = rule
        
        if port:
            command = f"access-list 100 {action} {protocol} {source} {destination} eq {port}"
        else:
            command = f"access-list 100 {action} {protocol} {source} {destination}"
        
        commands.append(command)
        rule_count += 1
        
        print(f"  Rule {rule_count}: {action} {protocol} from {source} to {destination}" + 
              (f" port {port}" if port else ""))
    
    return {
        'rule_count': rule_count,
        'commands': commands
    }

def parse_device_inventory(
    inventory_data: Dict[str, Dict[str, Union[str, List[str]]]]
) -> List[Dict[str, str]]:
    """
    Parse device inventory data into a standardized format.
    
    Args:
        inventory_data: Nested dictionary with device information
                       Format: {device_name: {property: value}}
    
    Returns:
        List of standardized device dictionaries
    """
    standardized_devices = []
    
    print("Parsing device inventory:")
    
    for device_name, device_info in inventory_data.items():
        device_dict = {
            'hostname': device_name,
            'device_type': device_info.get('type', 'unknown'),
            'ip_address': device_info.get('ip', ''),
            'location': device_info.get('location', ''),
            'model': device_info.get('model', ''),
            'interfaces': ', '.join(device_info.get('interfaces', []))
        }
        
        standardized_devices.append(device_dict)
        print(f"  {device_name}: {device_dict['device_type']} at {device_dict['ip_address']}")
    
    return standardized_devices

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== Annotated Arguments (Type Hints) Practice ===\n")
    
    # Example 1: Basic interface configuration with types
    print("1. Interface Configuration with Type Hints:")
    result = configure_interface_typed(
        hostname="R1",
        interface="GigabitEthernet0/1", 
        ip_address="192.168.1.1",
        subnet_mask="255.255.255.0",
        description="LAN Interface",
        admin_up=True
    )
    print(f"Result type: {type(result)}")
    
    # Example 2: VLAN batch configuration
    print("\n2. Batch VLAN Configuration:")
    vlan_list = [
        {'id': 10, 'name': 'SALES', 'description': 'Sales Department'},
        {'id': 20, 'name': 'FINANCE', 'description': 'Finance Department'},
        {'id': 30, 'name': 'IT', 'description': 'IT Department'}
    ]
    commands = configure_vlans_batch("SW1", vlan_list)
    print(f"Generated {len(commands)} commands")
    
    # Example 3: OSPF configuration with IP objects
    print("\n3. OSPF Configuration with IP Address Objects:")
    from ipaddress import IPv4Address, IPv4Network
    
    router_id = IPv4Address('1.1.1.1')
    ospf_areas = {
        0: [IPv4Network('192.168.1.0/24'), IPv4Network('10.1.1.0/30')],
        1: [IPv4Network('172.16.0.0/24')]
    }
    
    success, ospf_commands = setup_ospf_areas("R1", router_id, ospf_areas)
    print(f"OSPF configuration successful: {success}")
    
    # Example 4: Firewall rules with tuples
    print("\n4. Firewall Rules Configuration:")
    firewall_rules = [
        ("permit", "tcp", "192.168.1.0 0.0.0.255", "any", 80),
        ("permit", "tcp", "192.168.1.0 0.0.0.255", "any", 443), 
        ("deny", "ip", "any", "192.168.100.0 0.0.0.255", None),
        ("permit", "ip", "any", "any", None)
    ]
    
    rule_result = create_firewall_rules("ASA1", firewall_rules)
    print(f"Created {rule_result['rule_count']} firewall rules")
    
    # Example 5: Device inventory parsing
    print("\n5. Device Inventory Parsing:")
    inventory = {
        "R1": {
            "type": "router",
            "ip": "192.168.1.1", 
            "location": "Main Office",
            "model": "ISR4331",
            "interfaces": ["Gi0/0", "Gi0/1", "Se0/0/0"]
        },
        "SW1": {
            "type": "switch",
            "ip": "192.168.1.2",
            "location": "Main Office", 
            "model": "Catalyst2960",
            "interfaces": ["Gi0/1", "Gi0/2", "Gi0/3", "Gi0/24"]
        }
    }
    
    parsed_devices = parse_device_inventory(inventory)
    print(f"Parsed {len(parsed_devices)} devices")
    
    print("\n=== TYPE CHECKING DEMONSTRATION ===")
    print("Type hints help catch errors during development:")
    print("• IDEs can warn about incorrect types")
    print("• Tools like mypy can validate type usage")
    print("• Documentation becomes clearer")
    
    # Demonstrate type checking (these would show warnings in IDEs)
    print("\n⚠️  These would show type warnings in IDEs:")
    print("configure_interface_typed(123, 'Gi0/1', '192.168.1.1', '255.255.255.0')  # hostname should be str")
    print("configure_vlans_batch('SW1', 'not_a_list')  # vlan_configs should be List")
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("1. Add type hints to your own functions")
    print("2. Use complex types like List, Dict, Tuple, Optional")
    print("3. Try using IPv4Address and IPv4Network from ipaddress module")
    print("4. Install mypy and check your code: pip install mypy && mypy yourfile.py")
    
