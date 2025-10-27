"""
OS Module Operations - Network Automation

This module demonstrates how to use the os module for file system operations
commonly needed in network automation tasks such as organizing configuration
files, creating backup directories, and managing device inventories.
"""

import os
import platform
from pathlib import Path


def demonstrate_os_basics():
    """Demonstrate basic os module functionality."""
    print("=== OS Module Basics ===\n")
    
    # Get current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    # Get user information
    print(f"Current user: {os.getenv('USERNAME') or os.getenv('USER', 'Unknown')}")
    print(f"Operating system: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    
    # List directory contents
    print(f"\nContents of current directory:")
    for item in os.listdir('.'):
        item_path = os.path.join('.', item)
        if os.path.isdir(item_path):
            print(f"  📁 {item}/")
        else:
            size = os.path.getsize(item_path)
            print(f"  📄 {item} ({size} bytes)")


def manage_network_directories():
    """Create and manage directory structure for network automation."""
    print("\n=== Network Directory Management ===\n")
    
    # Define directory structure for network automation
    base_dirs = [
        "network_configs",
        "backups",
        "templates", 
        "inventories",
        "logs",
        "scripts"
    ]
    
    device_dirs = [
        "network_configs/routers",
        "network_configs/switches",
        "network_configs/firewalls",
        "backups/daily",
        "backups/weekly", 
        "backups/monthly"
    ]
    
    print("Creating network automation directory structure...")
    
    # Create base directories
    for dir_name in base_dirs:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"✓ Created directory: {dir_name}")
        except OSError as e:
            print(f"✗ Failed to create {dir_name}: {e}")
    
    # Create subdirectories
    for dir_name in device_dirs:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"✓ Created subdirectory: {dir_name}")
        except OSError as e:
            print(f"✗ Failed to create {dir_name}: {e}")
    
    return base_dirs + device_dirs


def demonstrate_path_operations():
    """Demonstrate path manipulation operations."""
    print("\n=== Path Operations ===\n")
    
    # Join paths (works across different operating systems)
    config_path = os.path.join("network_configs", "routers", "core-router-01.cfg")
    print(f"Config path: {config_path}")
    
    backup_path = os.path.join("backups", "daily", "switch-backup-20241026.cfg")
    print(f"Backup path: {backup_path}")
    
    # Split paths
    directory, filename = os.path.split(config_path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    
    # Split filename and extension
    name, extension = os.path.splitext(filename)
    print(f"Name: {name}")
    print(f"Extension: {extension}")
    
    # Get absolute paths
    abs_config_path = os.path.abspath(config_path)
    print(f"Absolute config path: {abs_config_path}")
    
    # Check if paths exist
    print(f"\nPath existence checks:")
    print(f"'{config_path}' exists: {os.path.exists(config_path)}")
    print(f"'{directory}' exists: {os.path.exists(directory)}")
    print(f"Current directory exists: {os.path.exists('.')}")


def create_sample_files():
    """Create sample network configuration files."""
    print("\n=== Creating Sample Files ===\n")
    
    # Sample configurations
    router_config = """!
! Router Configuration - Core-Router-01
! Generated: 2024-10-26
!
version 15.1
service timestamps debug datetime msec
!
hostname Core-Router-01
!
interface GigabitEthernet0/0
 description WAN Interface
 ip address 203.0.113.1 255.255.255.252
 no shutdown
!
interface GigabitEthernet0/1
 description LAN Interface
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
router ospf 1
 router-id 1.1.1.1
 network 192.168.1.0 0.0.0.255 area 0
!
end
"""
    
    switch_config = """!
! Switch Configuration - Access-Switch-01
! Generated: 2024-10-26
!
version 15.2
!
hostname Access-Switch-01
!
vlan 10
 name Data
!
vlan 20
 name Voice
!
interface range FastEthernet0/1-12
 switchport mode access
 switchport access vlan 10
!
interface range FastEthernet0/13-24
 switchport mode access
 switchport access vlan 20
!
interface GigabitEthernet0/1
 description Uplink to Core
 switchport mode trunk
!
end
"""
    
    # Create the files
    files_created = []
    
    router_path = os.path.join("network_configs", "routers", "core-router-01.cfg")
    try:
        with open(router_path, 'w', encoding='utf-8') as f:
            f.write(router_config)
        print(f"✓ Created router config: {router_path}")
        files_created.append(router_path)
    except OSError as e:
        print(f"✗ Failed to create router config: {e}")
    
    switch_path = os.path.join("network_configs", "switches", "access-switch-01.cfg")
    try:
        with open(switch_path, 'w', encoding='utf-8') as f:
            f.write(switch_config)
        print(f"✓ Created switch config: {switch_path}")
        files_created.append(switch_path)
    except OSError as e:
        print(f"✗ Failed to create switch config: {e}")
    
    return files_created


def analyze_file_information():
    """Analyze file information using os module."""
    print("\n=== File Information Analysis ===\n")
    
    # Create sample files first
    sample_files = create_sample_files()
    
    for file_path in sample_files:
        if os.path.exists(file_path):
            stat = os.stat(file_path)
            
            print(f"File: {file_path}")
            print(f"  Size: {stat.st_size} bytes")
            print(f"  Created: {os.path.getctime(file_path)}")
            print(f"  Modified: {os.path.getmtime(file_path)}")
            print(f"  Accessed: {os.path.getatime(file_path)}")
            print(f"  Is file: {os.path.isfile(file_path)}")
            print(f"  Is directory: {os.path.isdir(file_path)}")
            
            # Check permissions (Unix-like systems)
            try:
                print(f"  Readable: {os.access(file_path, os.R_OK)}")
                print(f"  Writable: {os.access(file_path, os.W_OK)}")
                print(f"  Executable: {os.access(file_path, os.X_OK)}")
            except AttributeError:
                print("  Permission checks not available on this system")
            
            print()


def demonstrate_environment_variables():
    """Demonstrate working with environment variables."""
    print("\n=== Environment Variables ===\n")
    
    # Common environment variables
    env_vars = ['PATH', 'HOME', 'USER', 'USERNAME', 'COMPUTERNAME', 'HOSTNAME']
    
    print("Common environment variables:")
    for var in env_vars:
        value = os.getenv(var)
        if value:
            # Truncate long values like PATH
            if len(str(value)) > 60:
                value = str(value)[:60] + "..."
            print(f"  {var}: {value}")
    
    # Set custom environment variables for network automation
    print("\nSetting custom environment variables:")
    os.environ['NETWORK_CONFIG_PATH'] = os.path.abspath('network_configs')
    os.environ['BACKUP_PATH'] = os.path.abspath('backups')
    os.environ['SCRIPT_VERSION'] = '1.0.0'
    
    print(f"  NETWORK_CONFIG_PATH: {os.getenv('NETWORK_CONFIG_PATH')}")
    print(f"  BACKUP_PATH: {os.getenv('BACKUP_PATH')}")
    print(f"  SCRIPT_VERSION: {os.getenv('SCRIPT_VERSION')}")


def walk_directory_tree():
    """Walk through directory tree to find all configuration files."""
    print("\n=== Directory Tree Walk ===\n")
    
    print("Walking through network_configs directory:")
    
    if os.path.exists('network_configs'):
        for root, dirs, files in os.walk('network_configs'):
            level = root.replace('network_configs', '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}📁 {os.path.basename(root)}/")
            
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                print(f"{subindent}📄 {file} ({file_size} bytes)")
    else:
        print("network_configs directory not found")


def cleanup_demo_files():
    """Clean up demo files and directories."""
    print("\n=== Cleanup ===\n")
    
    # Remove files first
    files_to_remove = [
        os.path.join("network_configs", "routers", "core-router-01.cfg"),
        os.path.join("network_configs", "switches", "access-switch-01.cfg")
    ]
    
    for file_path in files_to_remove:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"✓ Removed file: {file_path}")
            except OSError as e:
                print(f"✗ Failed to remove {file_path}: {e}")
    
    # Remove directories (in reverse order)
    dirs_to_remove = [
        "network_configs/switches",
        "network_configs/routers", 
        "network_configs/firewalls",
        "network_configs",
        "backups/monthly",
        "backups/weekly",
        "backups/daily",
        "backups",
        "templates",
        "inventories", 
        "logs",
        "scripts"
    ]
    
    for dir_path in dirs_to_remove:
        if os.path.exists(dir_path):
            try:
                os.rmdir(dir_path)
                print(f"✓ Removed directory: {dir_path}")
            except OSError as e:
                print(f"✗ Failed to remove {dir_path}: {e}")


if __name__ == "__main__":
    try:
        demonstrate_os_basics()
        created_dirs = manage_network_directories()
        demonstrate_path_operations()
        analyze_file_information()
        demonstrate_environment_variables()
        walk_directory_tree()
        
        # Ask user if they want to clean up
        print("\n" + "="*50)
        response = input("Clean up demo files and directories? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_demo_files()
        else:
            print("Demo files left in place for examination")
        
        print("\n=== OS Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• Use os.makedirs() with exist_ok=True for safe directory creation")
        print("• Always use os.path.join() for cross-platform path handling")
        print("• Check file/directory existence before operations")
        print("• Use os.walk() to recursively process directory trees")
        print("• Handle OSError exceptions for robust file operations")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()