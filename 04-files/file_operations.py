"""
File Operations: Create, Read, and Append - Network Automation

This module demonstrates the three fundamental file operations (create, read, append)
commonly used in network automation for configuration management, logging, and
device inventory tracking.
"""

import os
import json
from datetime import datetime
import csv


def demonstrate_create_operations():
    """Demonstrate creating files with different content types."""
    print("=== File Creation Operations ===\n")
    
    # Create 1: Simple text configuration
    print("1. Creating simple router configuration:")
    basic_config = """!
! Basic Router Configuration
!
version 15.1
!
hostname BasicRouter
!
interface GigabitEthernet0/0
 no ip address
 shutdown
!
interface GigabitEthernet0/1
 no ip address
 shutdown
!
line con 0
line vty 0 4
 login
!
end
"""
    
    with open("basic_router.cfg", "w", encoding="utf-8") as file:
        file.write(basic_config)
    print("✓ Created basic_router.cfg")
    
    # Create 2: JSON device inventory
    print("\n2. Creating JSON device inventory:")
    inventory = {
        "network_devices": [
            {
                "hostname": "core-switch-01",
                "ip_address": "10.0.0.10",
                "device_type": "switch",
                "vendor": "Cisco",
                "model": "Catalyst 2960X",
                "location": "Rack 1A",
                "vlan_count": 5,
                "port_count": 48,
                "managed": True
            },
            {
                "hostname": "access-point-01", 
                "ip_address": "10.0.0.50",
                "device_type": "wireless_ap",
                "vendor": "Cisco",
                "model": "Aironet 2802I",
                "location": "Floor 2 East",
                "ssid_count": 3,
                "max_clients": 200,
                "managed": True
            },
            {
                "hostname": "edge-router-01",
                "ip_address": "10.0.0.1", 
                "device_type": "router",
                "vendor": "Cisco",
                "model": "ISR 4331",
                "location": "Main Distribution Frame",
                "interface_count": 4,
                "routing_protocols": ["OSPF", "BGP"],
                "managed": True
            }
        ],
        "metadata": {
            "created_date": datetime.now().isoformat(),
            "created_by": "network_automation_script",
            "version": "1.0",
            "total_devices": 3
        }
    }
    
    with open("device_inventory.json", "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)
    print("✓ Created device_inventory.json")
    
    # Create 3: CSV port mapping
    print("\n3. Creating CSV port mapping file:")
    port_data = [
        ["Switch", "Port", "VLAN", "Description", "Status"],
        ["SW01", "Fa0/1", "10", "Workstation-PC01", "up"],
        ["SW01", "Fa0/2", "10", "Workstation-PC02", "up"],
        ["SW01", "Fa0/3", "20", "Printer-PR01", "up"],
        ["SW01", "Fa0/4", "10", "Workstation-PC03", "down"],
        ["SW01", "Fa0/5", "30", "Server-SRV01", "up"],
        ["SW02", "Fa0/1", "10", "Workstation-PC04", "up"],
        ["SW02", "Fa0/2", "20", "Phone-PH01", "up"]
    ]
    
    with open("port_mapping.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(port_data)
    print("✓ Created port_mapping.csv")
    
    # Create 4: Binary backup simulation
    print("\n4. Creating binary backup file simulation:")
    backup_header = b"CISCO_BACKUP_V1.0"
    backup_timestamp = datetime.now().strftime("%Y%m%d%H%M%S").encode('ascii')
    backup_data = b"Configuration data would go here in a real backup"
    
    with open("router_backup.bin", "wb") as file:
        file.write(backup_header + b"\n")
        file.write(backup_timestamp + b"\n")
        file.write(backup_data)
    print("✓ Created router_backup.bin (binary)")
    
    return ["basic_router.cfg", "device_inventory.json", "port_mapping.csv", "router_backup.bin"]


def demonstrate_read_operations():
    """Demonstrate different ways to read files."""
    print("\n=== File Read Operations ===\n")
    
    # Read 1: Read entire configuration file
    print("1. Reading entire configuration file:")
    if os.path.exists("basic_router.cfg"):
        with open("basic_router.cfg", "r", encoding="utf-8") as file:
            config_content = file.read()
        
        line_count = len(config_content.splitlines())
        char_count = len(config_content)
        print(f"✓ Read configuration: {line_count} lines, {char_count} characters")
        
        # Show first few lines
        lines = config_content.splitlines()
        print("First 5 lines:")
        for i, line in enumerate(lines[:5], 1):
            print(f"  {i}: {line}")
    
    # Read 2: Read JSON and parse
    print("\n2. Reading and parsing JSON inventory:")
    if os.path.exists("device_inventory.json"):
        with open("device_inventory.json", "r", encoding="utf-8") as file:
            inventory_data = json.load(file)
        
        devices = inventory_data["network_devices"]
        metadata = inventory_data["metadata"]
        
        print(f"✓ Loaded inventory created on {metadata['created_date']}")
        print(f"Device summary:")
        for device in devices:
            print(f"  - {device['hostname']}: {device['device_type']} ({device['vendor']} {device['model']})")
    
    # Read 3: Read CSV line by line
    print("\n3. Reading CSV file line by line:")
    if os.path.exists("port_mapping.csv"):
        with open("port_mapping.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read header row
            
            print(f"CSV Headers: {', '.join(header)}")
            print("Port mappings:")
            
            port_count = 0
            for row in csv_reader:
                if len(row) >= 5:
                    switch, port, vlan, description, status = row
                    status_icon = "🟢" if status == "up" else "🔴"
                    print(f"  {status_icon} {switch}:{port} → VLAN {vlan} ({description})")
                    port_count += 1
            
            print(f"Total ports: {port_count}")
    
    # Read 4: Read binary file
    print("\n4. Reading binary backup file:")
    if os.path.exists("router_backup.bin"):
        with open("router_backup.bin", "rb") as file:
            binary_content = file.read()
        
        # Parse the binary content
        lines = binary_content.split(b'\n')
        if len(lines) >= 3:
            header = lines[0].decode('ascii')
            timestamp = lines[1].decode('ascii')
            data_preview = lines[2][:50].decode('ascii', errors='ignore')
            
            print(f"✓ Binary backup read successfully")
            print(f"  Header: {header}")
            print(f"  Timestamp: {timestamp}")
            print(f"  Data preview: {data_preview}...")
    
    # Read 5: Read file line by line (memory efficient)
    print("\n5. Reading configuration line by line (memory efficient):")
    if os.path.exists("basic_router.cfg"):
        interface_count = 0
        command_count = 0
        
        with open("basic_router.cfg", "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line.startswith("interface "):
                    interface_count += 1
                    print(f"  Found interface at line {line_num}: {line}")
                elif line and not line.startswith("!"):
                    command_count += 1
        
        print(f"Analysis: {interface_count} interfaces, {command_count} commands")


def demonstrate_append_operations():
    """Demonstrate appending to existing files."""
    print("\n=== File Append Operations ===\n")
    
    # Append 1: Add entries to log file
    print("1. Creating and appending to network log:")
    
    # Create initial log file
    with open("network_operations.log", "w", encoding="utf-8") as file:
        file.write("Network Operations Log\n")
        file.write("=" * 30 + "\n")
        file.write(f"Log started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Simulate network events and append them
    events = [
        "Interface GigE0/1 on SW01 changed state to UP",
        "OSPF neighbor 192.168.1.2 established on R01",
        "VLAN 50 created on SW01",
        "Configuration backup completed for R01",
        "Port Fa0/5 on SW01 assigned to VLAN 10",
        "BGP session with 203.0.113.1 established on R01"
    ]
    
    for i, event in enumerate(events, 1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Event {i:03d}: {event}\n"
        
        with open("network_operations.log", "a", encoding="utf-8") as file:
            file.write(log_entry)
    
    print(f"✓ Appended {len(events)} events to log")
    
    # Append 2: Add new device to inventory
    print("\n2. Appending new device to JSON inventory:")
    
    # Read existing inventory
    with open("device_inventory.json", "r", encoding="utf-8") as file:
        inventory = json.load(file)
    
    # Add new device
    new_device = {
        "hostname": "security-camera-01",
        "ip_address": "10.0.0.75",
        "device_type": "ip_camera",
        "vendor": "Axis",
        "model": "P3367-VE",
        "location": "Building Entrance",
        "resolution": "1080p",
        "poe_required": True,
        "managed": False
    }
    
    inventory["network_devices"].append(new_device)
    inventory["metadata"]["total_devices"] += 1
    inventory["metadata"]["last_updated"] = datetime.now().isoformat()
    
    # Write back to file (this replaces the entire file)
    with open("device_inventory.json", "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)
    
    print("✓ Added new device to inventory")
    
    # Append 3: Add entries to CSV
    print("\n3. Appending new port mappings to CSV:")
    
    new_ports = [
        ["SW02", "Fa0/3", "10", "Workstation-PC05", "up"],
        ["SW02", "Fa0/4", "20", "Phone-PH02", "up"],
        ["SW03", "Fa0/1", "30", "Server-SRV02", "down"]
    ]
    
    with open("port_mapping.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(new_ports)
    
    print(f"✓ Appended {len(new_ports)} new port mappings")
    
    # Append 4: Add configuration to existing file
    print("\n4. Appending additional configuration:")
    
    additional_config = """!
! Additional Configuration Added
!
ip domain-name company.local
ip name-server 8.8.8.8
ip name-server 8.8.4.4
!
ntp server 0.pool.ntp.org
ntp server 1.pool.ntp.org
!
logging 10.0.0.5
logging trap informational
!
"""
    
    with open("basic_router.cfg", "a", encoding="utf-8") as file:
        file.write(additional_config)
    
    print("✓ Added DNS, NTP, and logging configuration")
    
    return ["network_operations.log"]


def verify_file_operations():
    """Verify all file operations worked correctly."""
    print("\n=== Verification of File Operations ===\n")
    
    files_to_check = [
        "basic_router.cfg",
        "device_inventory.json", 
        "port_mapping.csv",
        "router_backup.bin",
        "network_operations.log"
    ]
    
    for filename in files_to_check:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            
            # Get line count for text files
            if filename.endswith(('.cfg', '.json', '.csv', '.log')):
                try:
                    with open(filename, "r", encoding="utf-8") as file:
                        lines = len(file.readlines())
                    print(f"✓ {filename}: {size} bytes, {lines} lines")
                except:
                    print(f"✓ {filename}: {size} bytes (binary or read error)")
            else:
                print(f"✓ {filename}: {size} bytes (binary)")
        else:
            print(f"✗ {filename}: Not found")
    
    # Detailed verification of log file
    print("\nDetailed log file analysis:")
    if os.path.exists("network_operations.log"):
        with open("network_operations.log", "r", encoding="utf-8") as file:
            log_lines = file.readlines()
        
        event_lines = [line for line in log_lines if "Event" in line]
        print(f"  Total log lines: {len(log_lines)}")
        print(f"  Event entries: {len(event_lines)}")
        
        if event_lines:
            print("  Sample events:")
            for line in event_lines[:3]:
                print(f"    {line.strip()}")


def cleanup_demonstration_files(created_files, appended_files):
    """Clean up all demonstration files."""
    print("\n=== Cleanup ===\n")
    
    all_files = created_files + appended_files
    
    for filename in all_files:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Removed: {filename}")
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")


if __name__ == "__main__":
    try:
        # Demonstrate all three operations
        created_files = demonstrate_create_operations()
        demonstrate_read_operations()
        appended_files = demonstrate_append_operations()
        
        # Verify everything worked
        verify_file_operations()
        
        print("\n" + "="*50)
        response = input("Clean up demonstration files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_demonstration_files(created_files, appended_files)
        else:
            print("Files left in place for examination")
        
        print("\n=== File Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• CREATE: Use 'w' mode to create new files (overwrites existing)")
        print("• READ: Use 'r' mode to read files, handle different formats appropriately")
        print("• APPEND: Use 'a' mode to add content to existing files")
        print("• Always use context managers (with statements)")
        print("• Specify encoding='utf-8' for text files")
        print("• Handle exceptions for robust file operations")
        print("• Use appropriate file formats (JSON, CSV, binary) for different data types")
        print("• Verify file operations completed successfully")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()