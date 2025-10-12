"""
JSON Operations Examples
Working with JSON Data in Network Automation

JSON (JavaScript Object Notation) is a lightweight, human-readable data format
commonly used for APIs, configuration files, and data exchange in network automation.
"""

import json
from pathlib import Path

# Get the path to the sample data file
SAMPLE_DATA_PATH = Path(__file__).parent.parent / "sample-data" / "network_devices.json"

def load_device_inventory():
    """
    Load network device inventory from JSON file.
    
    Returns:
        dict: Network device data
    """
    try:
        with open(SAMPLE_DATA_PATH, 'r') as file:
            data = json.load(file)
            print("✓ Successfully loaded device inventory from JSON")
            return data
    except FileNotFoundError:
        print(f"✗ Error: Could not find file {SAMPLE_DATA_PATH}")
        return {}
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON format - {e}")
        return {}

def display_device_summary(inventory_data):
    """
    Display a summary of network devices from JSON data.
    
    Args:
        inventory_data: Dictionary containing device inventory
    """
    if not inventory_data:
        print("No inventory data available")
        return
    
    devices = inventory_data.get('network_devices', [])
    topology = inventory_data.get('network_topology', {})
    
    print("\n=== Network Device Summary ===")
    print(f"Site: {topology.get('site_name', 'Unknown')}")
    print(f"Total Devices: {len(devices)}")
    
    # Count devices by type
    device_counts = {}
    for device in devices:
        device_type = device.get('device_type', 'unknown')
        device_counts[device_type] = device_counts.get(device_type, 0) + 1
    
    print("\nDevice Types:")
    for device_type, count in device_counts.items():
        print(f"  {device_type.title()}: {count}")

def find_devices_by_type(inventory_data, device_type):
    """
    Find all devices of a specific type.
    
    Args:
        inventory_data: Dictionary containing device inventory
        device_type: Type of device to find (router, switch, etc.)
    
    Returns:
        list: List of devices matching the type
    """
    devices = inventory_data.get('network_devices', [])
    matching_devices = []
    
    for device in devices:
        if device.get('device_type') == device_type:
            matching_devices.append(device)
    
    print(f"\nFound {len(matching_devices)} {device_type}(s):")
    for device in matching_devices:
        print(f"  - {device.get('hostname', 'Unknown')} ({device.get('model', 'Unknown')})")
    
    return matching_devices

def extract_interface_info(inventory_data):
    """
    Extract interface information from all devices.
    
    Args:
        inventory_data: Dictionary containing device inventory
        
    Returns:
        list: List of interface dictionaries
    """
    devices = inventory_data.get('network_devices', [])
    all_interfaces = []
    
    for device in devices:
        hostname = device.get('hostname', 'Unknown')
        interfaces = device.get('interfaces', [])
        
        for interface in interfaces:
            interface_info = {
                'device': hostname,
                'device_type': device.get('device_type'),
                'interface_name': interface.get('name'),
                'status': interface.get('status'),
                'ip_address': interface.get('ip_address'),
                'vlan': interface.get('vlan'),
                'speed': interface.get('speed'),
                'description': interface.get('description', '')
            }
            all_interfaces.append(interface_info)
    
    return all_interfaces

def create_device_config_json(hostname, device_type, management_ip, **kwargs):
    """
    Create a device configuration in JSON format.
    
    Args:
        hostname: Device hostname
        device_type: Type of device
        management_ip: Management IP address
        **kwargs: Additional configuration parameters
        
    Returns:
        str: JSON formatted device configuration
    """
    device_config = {
        "hostname": hostname,
        "device_type": device_type,
        "management_ip": management_ip,
        "timestamp": "2024-03-15T14:30:00Z",
        "configuration": kwargs
    }
    
    return json.dumps(device_config, indent=2)

def save_filtered_devices(inventory_data, device_type, output_file):
    """
    Save filtered devices to a new JSON file.
    
    Args:
        inventory_data: Dictionary containing device inventory
        device_type: Type of devices to filter
        output_file: Path to output file
    """
    devices = inventory_data.get('network_devices', [])
    filtered_devices = [device for device in devices 
                       if device.get('device_type') == device_type]
    
    output_data = {
        "filtered_device_type": device_type,
        "total_count": len(filtered_devices),
        "devices": filtered_devices
    }
    
    try:
        with open(output_file, 'w') as file:
            json.dump(output_data, file, indent=2)
        print(f"✓ Saved {len(filtered_devices)} {device_type}s to {output_file}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")

def parse_monitoring_data(inventory_data):
    """
    Parse monitoring and alert information from JSON data.
    
    Args:
        inventory_data: Dictionary containing device inventory
    """
    monitoring = inventory_data.get('monitoring_data', {})
    
    print("\n=== Network Monitoring Status ===")
    print(f"Last Updated: {monitoring.get('last_updated', 'Unknown')}")
    print(f"Overall Status: {monitoring.get('overall_status', 'Unknown').title()}")
    
    # Performance metrics
    metrics = monitoring.get('performance_metrics', {})
    if metrics:
        print("\nPerformance Metrics:")
        print(f"  Average CPU Usage: {metrics.get('average_cpu_usage', 0)}%")
        print(f"  Average Memory Usage: {metrics.get('average_memory_usage', 0)}%")
        print(f"  Interface Errors: {metrics.get('total_interface_errors', 0)}")
        print(f"  Unreachable Devices: {metrics.get('devices_unreachable', 0)}")
    
    # Alerts
    alerts = monitoring.get('alerts', [])
    if alerts:
        print(f"\nActive Alerts ({len(alerts)}):")
        for alert in alerts:
            print(f"  {alert.get('severity', 'info').upper()}: {alert.get('message', 'No message')}")
            print(f"    Device: {alert.get('device', 'Unknown')}")
            print(f"    Time: {alert.get('timestamp', 'Unknown')}")

def modify_json_data(inventory_data):
    """
    Demonstrate modifying JSON data and converting back to JSON.
    
    Args:
        inventory_data: Dictionary containing device inventory
        
    Returns:
        str: Modified JSON data
    """
    # Create a copy to avoid modifying original data
    modified_data = inventory_data.copy()
    
    # Add a new device
    new_device = {
        "hostname": "NEW-SW1",
        "device_type": "switch",
        "model": "Catalyst9200-24P",
        "management_ip": "192.168.1.25",
        "location": "Floor 3 - New IDF",
        "ios_version": "16.12.05",
        "uptime_hours": 0,
        "interfaces": [
            {
                "name": "GigabitEthernet0/1",
                "status": "down",
                "vlan": 1,
                "speed": "auto",
                "duplex": "auto"
            }
        ],
        "vlans": [
            {
                "id": 1,
                "name": "default",
                "description": "Default VLAN"
            }
        ]
    }
    
    # Add the new device to the inventory
    if 'network_devices' in modified_data:
        modified_data['network_devices'].append(new_device)
    
    # Update the device count in topology
    if 'network_topology' in modified_data:
        total_devices = len(modified_data['network_devices'])
        modified_data['network_topology']['total_devices'] = total_devices
    
    return json.dumps(modified_data, indent=2)

# Example usage and practice exercises
if __name__ == "__main__":
    print("=== JSON Operations Practice ===\n")
    
    # Example 1: Load JSON data
    print("1. Loading JSON Device Inventory:")
    inventory = load_device_inventory()
    
    if inventory:
        # Example 2: Display summary
        print("\n2. Device Inventory Summary:")
        display_device_summary(inventory)
        
        # Example 3: Find devices by type
        print("\n3. Finding Routers:")
        routers = find_devices_by_type(inventory, "router")
        
        print("\n4. Finding Switches:")
        switches = find_devices_by_type(inventory, "switch")
        
        # Example 4: Extract interface information
        print("\n5. Extracting Interface Information:")
        interfaces = extract_interface_info(inventory)
        
        print(f"Total interfaces found: {len(interfaces)}")
        print("\nFirst few interfaces:")
        for interface in interfaces[:5]:
            device = interface['device']
            name = interface['interface_name']
            status = interface['status']
            ip = interface.get('ip_address', 'No IP')
            print(f"  {device} - {name}: {status} ({ip})")
        
        # Example 5: Parse monitoring data
        print("\n6. Monitoring Data:")
        parse_monitoring_data(inventory)
        
        # Example 6: Create new device configuration
        print("\n7. Creating New Device Configuration:")
        new_config = create_device_config_json(
            "TEST-RTR1",
            "router",
            "192.168.1.99",
            interfaces=["Gi0/0", "Gi0/1"],
            routing_protocol="OSPF",
            enabled_features=["SSH", "SNMP"]
        )
        print("New device configuration (JSON):")
        print(new_config)
        
        # Example 7: Save filtered data
        print("\n8. Saving Filtered Device Data:")
        output_file = Path(__file__).parent / "switches_only.json"
        save_filtered_devices(inventory, "switch", output_file)
        
        # Example 8: Modify and convert back to JSON
        print("\n9. Modifying JSON Data:")
        modified_json = modify_json_data(inventory)
        print("Added new device to inventory (first 500 characters):")
        print(modified_json[:500] + "...")
    
    print("\n=== YOUR TURN TO PRACTICE ===")
    print("Try these exercises:")
    print("1. Load the JSON file and extract all IP addresses")
    print("2. Find all devices in a specific location")
    print("3. Create a summary of VLAN usage across all switches")
    print("4. Add a new VLAN to an existing switch")
    print("5. Export interface errors to a separate JSON file")
    
    # Practice Exercise Templates
    print("\n=== Practice Exercise Templates ===")
    
    print("\nExercise 1: Extract all IP addresses")
    """
    def get_all_ip_addresses(inventory_data):
        ip_addresses = []
        # Your code here: Loop through devices and interfaces
        # Extract all IP addresses and return as a list
        return ip_addresses
    """
    
    print("\nExercise 2: Find devices by location")
    """
    def find_devices_by_location(inventory_data, location_keyword):
        matching_devices = []
        # Your code here: Search device locations for the keyword
        # Return list of matching devices
        return matching_devices
    """
    
    print("\nExercise 3: VLAN usage summary")
    """
    def analyze_vlan_usage(inventory_data):
        vlan_summary = {}
        # Your code here: Count how many devices use each VLAN
        # Return dictionary: {vlan_id: device_count}
        return vlan_summary
    """
    
    print("\nExercise 4: Add VLAN to switch")
    """
    def add_vlan_to_switch(inventory_data, switch_hostname, vlan_id, vlan_name):
        # Your code here: Find the switch and add a new VLAN
        # Return updated inventory data
        pass
    """
    
    print("\nRemember:")
    print("• JSON data becomes Python dictionaries and lists")
    print("• Use json.load() to read from files")
    print("• Use json.dump() to write to files") 
    print("• Use json.loads() for JSON strings")
    print("• Use json.dumps() to create JSON strings")
    print("• Always handle FileNotFoundError and JSONDecodeError")