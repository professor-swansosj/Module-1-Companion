"""
Basic File Operations - Network Automation

This module demonstrates basic file operations using the open() function
for reading and writing network configuration files, device inventories,
and automation logs.
"""

import os


def demonstrate_file_modes():
    """Demonstrate different file opening modes."""
    print("=== File Opening Modes ===\n")
    
    modes = {
        'r': 'Read only (default) - file must exist',
        'w': 'Write only - creates new or overwrites existing file',
        'a': 'Append only - creates new or appends to existing file',
        'r+': 'Read and write - file must exist',
        'w+': 'Read and write - creates new or overwrites existing file',
        'a+': 'Read and append - creates new or appends to existing file',
        'x': 'Exclusive creation - fails if file already exists',
        'rb': 'Read binary mode',
        'wb': 'Write binary mode',
        'ab': 'Append binary mode'
    }
    
    print("Common file modes:")
    for mode, description in modes.items():
        print(f"  '{mode}': {description}")
    
    print("\nNote: Always specify encoding='utf-8' for text files to ensure compatibility")


def create_device_inventory():
    """Create a sample device inventory file."""
    print("\n=== Creating Device Inventory ===\n")
    
    inventory_data = """# Network Device Inventory
# Format: hostname,ip_address,device_type,vendor,location
core-router-01,10.0.0.1,router,Cisco,Data Center
core-router-02,10.0.0.2,router,Cisco,Data Center
access-switch-01,10.0.1.10,switch,Cisco,Floor 1
access-switch-02,10.0.1.11,switch,Cisco,Floor 2
access-switch-03,10.0.1.12,switch,Cisco,Floor 3
firewall-01,10.0.0.100,firewall,Fortinet,Data Center
wireless-controller,10.0.0.50,wireless_controller,Cisco,Data Center
"""
    
    filename = "device_inventory.txt"
    
    # Method 1: Using open() with explicit close
    print("Method 1: Manual file handling (NOT recommended)")
    try:
        file = open(filename, 'w', encoding='utf-8')
        file.write(inventory_data)
        file.close()  # Important: must close file manually
        print(f"✓ Created {filename} using manual file handling")
    except Exception as e:
        print(f"✗ Error creating file: {e}")
    
    return filename


def read_device_inventory(filename):
    """Read and parse device inventory file."""
    print(f"\n=== Reading Device Inventory from {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} does not exist")
        return []
    
    devices = []
    
    try:
        # Method 1: Read entire file at once
        print("Method 1: Reading entire file")
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        print(f"File content ({len(content)} characters):")
        print(content[:200] + "..." if len(content) > 200 else content)
        
        # Method 2: Read line by line
        print("\nMethod 2: Reading line by line")
        file = open(filename, 'r', encoding='utf-8')
        line_number = 1
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                # Parse CSV-like format
                parts = line.split(',')
                if len(parts) >= 5:
                    device = {
                        'hostname': parts[0],
                        'ip_address': parts[1],
                        'device_type': parts[2],
                        'vendor': parts[3],
                        'location': parts[4]
                    }
                    devices.append(device)
                    print(f"  Line {line_number}: {device['hostname']} ({device['device_type']})")
            line_number += 1
        file.close()
        
        # Method 3: Read all lines into a list
        print("\nMethod 3: Reading all lines")
        file = open(filename, 'r', encoding='utf-8')
        all_lines = file.readlines()
        file.close()
        print(f"Total lines read: {len(all_lines)}")
        
    except Exception as e:
        print(f"✗ Error reading file: {e}")
    
    return devices


def append_to_inventory(filename, new_device):
    """Append a new device to the inventory file."""
    print(f"\n=== Appending to {filename} ===\n")
    
    device_line = f"{new_device['hostname']},{new_device['ip_address']},{new_device['device_type']},{new_device['vendor']},{new_device['location']}\n"
    
    try:
        # Open in append mode
        file = open(filename, 'a', encoding='utf-8')
        file.write(device_line)
        file.close()
        print(f"✓ Added device: {new_device['hostname']}")
    except Exception as e:
        print(f"✗ Error appending to file: {e}")


def create_configuration_backup():
    """Create a sample configuration backup file."""
    print("\n=== Creating Configuration Backup ===\n")
    
    config_content = """!
! Configuration backup for core-router-01
! Backup date: 2024-10-26 14:30:00
! Backup by: network-admin
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname core-router-01
!
boot-start-marker
boot-end-marker
!
enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
!
no aaa new-model
ethernet lmi ce
!
interface GigabitEthernet0/0
 description WAN Interface to ISP
 ip address 203.0.113.1 255.255.255.252
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/1
 description LAN Interface to Core Switch
 ip address 192.168.1.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/2
 description Management Interface
 ip address 10.0.0.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
router ospf 1
 router-id 1.1.1.1
 log-adjacency-changes
 network 10.0.0.0 0.0.0.255 area 0
 network 192.168.1.0 0.0.0.255 area 0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip route 0.0.0.0 0.0.0.0 203.0.113.2
!
logging 10.0.0.5
logging trap notifications
!
snmp-server community public RO
snmp-server location "Data Center Rack 42"
snmp-server contact "Network Team <network@company.com>"
!
line con 0
 exec-timeout 30 0
 logging synchronous
line aux 0
line vty 0 4
 password cisco
 login
 transport input telnet ssh
!
end
"""
    
    backup_filename = "core-router-01_backup_20241026.cfg"
    
    try:
        # Create backup file
        file = open(backup_filename, 'w', encoding='utf-8')
        file.write(config_content)
        file.close()
        
        # Get file information
        file_size = os.path.getsize(backup_filename)
        print(f"✓ Created backup file: {backup_filename}")
        print(f"  File size: {file_size} bytes")
        print(f"  Lines in file: {len(config_content.splitlines())}")
        
        return backup_filename
        
    except Exception as e:
        print(f"✗ Error creating backup file: {e}")
        return None


def analyze_configuration_file(filename):
    """Analyze a configuration file for specific patterns."""
    print(f"\n=== Analyzing Configuration File: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} does not exist")
        return
    
    try:
        # Read and analyze the configuration
        file = open(filename, 'r', encoding='utf-8')
        
        # Statistics
        line_count = 0
        interface_count = 0
        comment_count = 0
        command_count = 0
        
        interfaces = []
        commands = []
        
        for line in file:
            line = line.strip()
            line_count += 1
            
            if line.startswith('!'):
                comment_count += 1
            elif line.startswith('interface '):
                interface_count += 1
                interfaces.append(line)
            elif line and not line.startswith('!'):
                command_count += 1
                commands.append(line)
        
        file.close()
        
        # Display analysis results
        print(f"Configuration Analysis Results:")
        print(f"  Total lines: {line_count}")
        print(f"  Comment lines: {comment_count}")
        print(f"  Command lines: {command_count}")
        print(f"  Interface definitions: {interface_count}")
        
        print(f"\nInterfaces found:")
        for interface in interfaces:
            print(f"  - {interface}")
        
        print(f"\nSample commands (first 5):")
        for i, command in enumerate(commands[:5]):
            print(f"  {i+1}. {command}")
        
        if len(commands) > 5:
            print(f"  ... and {len(commands) - 5} more commands")
    
    except Exception as e:
        print(f"✗ Error analyzing file: {e}")


def demonstrate_file_exceptions():
    """Demonstrate file operation exception handling."""
    print("\n=== File Exception Handling ===\n")
    
    print("Testing various file operation errors:")
    
    # Test 1: File not found
    print("\n1. Testing FileNotFoundError:")
    try:
        file = open("non_existent_file.txt", 'r')
        content = file.read()
        file.close()
    except FileNotFoundError:
        print("  ✓ Caught FileNotFoundError - file does not exist")
    except Exception as e:
        print(f"  Unexpected error: {e}")
    
    # Test 2: Permission error (simulate by trying to write to read-only)
    print("\n2. Testing PermissionError:")
    try:
        # Create a file first
        test_file = "test_readonly.txt"
        file = open(test_file, 'w')
        file.write("test content")
        file.close()
        
        # Try to modify file permissions (Unix/Linux only)
        if hasattr(os, 'chmod'):
            os.chmod(test_file, 0o444)  # Read-only
            
        # Try to write to read-only file
        file = open(test_file, 'w')
        file.write("new content")
        file.close()
        
        # Clean up
        if os.path.exists(test_file):
            os.chmod(test_file, 0o666)  # Restore permissions
            os.remove(test_file)
        
    except PermissionError:
        print("  ✓ Caught PermissionError - insufficient permissions")
        # Clean up
        if os.path.exists("test_readonly.txt"):
            try:
                os.chmod("test_readonly.txt", 0o666)
                os.remove("test_readonly.txt")
            except:
                pass
    except AttributeError:
        print("  ℹ Permission test not available on this platform")
    except Exception as e:
        print(f"  Unexpected error: {e}")
    
    # Test 3: Invalid mode
    print("\n3. Testing ValueError (invalid mode):")
    try:
        file = open("test.txt", 'invalid_mode')
    except ValueError as e:
        print(f"  ✓ Caught ValueError: {e}")
    except Exception as e:
        print(f"  Unexpected error: {e}")


def cleanup_demo_files():
    """Clean up files created during the demonstration."""
    print("\n=== Cleanup ===\n")
    
    files_to_remove = [
        "device_inventory.txt",
        "core-router-01_backup_20241026.cfg",
        "test_readonly.txt"
    ]
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Removed: {filename}")
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")


if __name__ == "__main__":
    try:
        demonstrate_file_modes()
        
        # Create and work with device inventory
        inventory_file = create_device_inventory()
        devices = read_device_inventory(inventory_file)
        
        # Add a new device
        new_device = {
            'hostname': 'backup-server-01',
            'ip_address': '10.0.0.200',
            'device_type': 'server',
            'vendor': 'Dell',
            'location': 'Data Center'
        }
        append_to_inventory(inventory_file, new_device)
        
        # Re-read to show the addition
        print("\nRe-reading inventory after addition:")
        updated_devices = read_device_inventory(inventory_file)
        print(f"Total devices: {len(updated_devices)}")
        
        # Create and analyze configuration backup
        backup_file = create_configuration_backup()
        if backup_file:
            analyze_configuration_file(backup_file)
        
        # Demonstrate exception handling
        demonstrate_file_exceptions()
        
        print("\n" + "="*50)
        response = input("Clean up demo files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_demo_files()
        
        print("\n=== Basic File Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• Always close files when done (or use context managers)")
        print("• Specify encoding='utf-8' for text files")
        print("• Handle exceptions for robust file operations")
        print("• Use appropriate file modes for your needs")
        print("• Check if files exist before trying to read them")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()