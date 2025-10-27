"""
Context Manager (with open()) - Network Automation

This module demonstrates the preferred way to handle files in Python using
context managers (with statements). Context managers ensure files are properly
closed even if errors occur, making code more robust and reliable.
"""

import os
import json
from datetime import datetime


def why_use_context_managers():
    """Explain why context managers are important."""
    print("=== Why Use Context Managers? ===\n")
    
    print("Context managers (with statements) provide several benefits:")
    print("✓ Automatic file closing - even if errors occur")
    print("✓ Cleaner, more readable code")
    print("✓ Better resource management")
    print("✓ Exception safety")
    print("✓ Pythonic best practice")
    
    print("\nComparison:")
    print("❌ Manual approach:")
    print("   file = open('config.txt', 'r')")
    print("   data = file.read()  # If this fails...")
    print("   file.close()       # ...this might never execute!")
    
    print("\n✅ Context manager approach:")
    print("   with open('config.txt', 'r') as file:")
    print("       data = file.read()  # File automatically closed")


def basic_context_manager_examples():
    """Demonstrate basic context manager usage."""
    print("\n=== Basic Context Manager Examples ===\n")
    
    # Example 1: Reading a file
    print("1. Reading with context manager:")
    sample_content = "hostname router-01\nip address 192.168.1.1 255.255.255.0\n"
    
    # First create a sample file
    with open("sample_config.txt", "w", encoding="utf-8") as file:
        file.write(sample_content)
    
    # Now read it back
    with open("sample_config.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"File content: {repr(content)}")
    
    print("✓ File automatically closed after with block")
    
    # Example 2: Writing a file
    print("\n2. Writing with context manager:")
    router_config = """!
! Router Configuration
!
hostname edge-router-01
!
interface GigabitEthernet0/0
 ip address 10.0.1.1 255.255.255.0
 no shutdown
!
end
"""
    
    with open("router_config.cfg", "w", encoding="utf-8") as file:
        file.write(router_config)
        print("✓ Router configuration written")
    
    # Verify the file was written
    if os.path.exists("router_config.cfg"):
        file_size = os.path.getsize("router_config.cfg")
        print(f"✓ File created successfully ({file_size} bytes)")


def advanced_context_manager_examples():
    """Demonstrate advanced context manager patterns."""
    print("\n=== Advanced Context Manager Examples ===\n")
    
    # Example 1: Multiple files
    print("1. Working with multiple files:")
    
    device_list = [
        {"hostname": "router-01", "ip": "10.0.1.1", "type": "router"},
        {"hostname": "switch-01", "ip": "10.0.1.10", "type": "switch"},
        {"hostname": "firewall-01", "ip": "10.0.1.100", "type": "firewall"}
    ]
    
    # Write to one file and read from another
    with open("devices.json", "w", encoding="utf-8") as output_file:
        json.dump(device_list, output_file, indent=2)
        print("✓ Device list written to JSON")
    
    with open("devices.json", "r", encoding="utf-8") as input_file:
        loaded_devices = json.load(input_file)
        print(f"✓ Loaded {len(loaded_devices)} devices from JSON")
    
    # Example 2: Append mode
    print("\n2. Appending to log files:")
    log_entries = [
        "2024-10-26 14:30:00 - Router-01 interface GigE0/0 up",
        "2024-10-26 14:31:15 - Switch-01 VLAN 10 created", 
        "2024-10-26 14:32:30 - Firewall-01 policy updated"
    ]
    
    # Create initial log
    with open("network.log", "w", encoding="utf-8") as log_file:
        log_file.write("Network Operations Log\n")
        log_file.write("=" * 25 + "\n")
    
    # Append entries
    for entry in log_entries:
        with open("network.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"{entry}\n")
    
    print("✓ Log entries appended")
    
    # Read back and display
    with open("network.log", "r", encoding="utf-8") as log_file:
        log_content = log_file.read()
        print("Log file contents:")
        print(log_content)


def context_manager_with_error_handling():
    """Demonstrate context managers with error handling."""
    print("\n=== Context Managers with Error Handling ===\n")
    
    print("1. Handling file not found:")
    try:
        with open("nonexistent_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("✓ Gracefully handled missing file")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    print("\n2. Handling permission errors:")
    try:
        # Create a test file first
        with open("test_file.txt", "w", encoding="utf-8") as file:
            file.write("test content")
        
        # The context manager will still work properly even with errors
        with open("test_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(f"✓ Successfully read: {content.strip()}")
            # Simulate an error within the context
            if len(content) > 0:
                print("✓ File processing completed normally")
    
    except Exception as e:
        print(f"✗ Error occurred: {e}")
    finally:
        # Clean up test file
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")
    
    print("\n3. Demonstrating automatic cleanup on exception:")
    try:
        with open("error_test.txt", "w", encoding="utf-8") as file:
            file.write("Starting write operation...\n")
            # Simulate an error
            raise ValueError("Simulated processing error")
            file.write("This line should not be written\n")  # Won't execute
    
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
        print("✓ File was still properly closed despite the error")
        
        # Verify file was properly closed and content written
        if os.path.exists("error_test.txt"):
            with open("error_test.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(f"File contents after error: {repr(content)}")
            os.remove("error_test.txt")


def practical_network_automation_examples():
    """Practical examples for network automation tasks."""
    print("\n=== Practical Network Automation Examples ===\n")
    
    # Example 1: Configuration template processing
    print("1. Processing configuration templates:")
    
    # Template with placeholders
    template = """!
! Configuration for {hostname}
! Generated on {date}
!
hostname {hostname}
!
interface GigabitEthernet0/0
 description {wan_description}
 ip address {wan_ip} {wan_mask}
 no shutdown
!
interface GigabitEthernet0/1  
 description {lan_description}
 ip address {lan_ip} {lan_mask}
 no shutdown
!
router ospf 1
 router-id {router_id}
 network {lan_network} {lan_wildcard} area 0
!
end
"""
    
    # Device parameters
    devices = [
        {
            "hostname": "branch-router-01",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "wan_description": "WAN to ISP",
            "wan_ip": "203.0.113.10",
            "wan_mask": "255.255.255.252",
            "lan_description": "LAN Interface",
            "lan_ip": "192.168.10.1",
            "lan_mask": "255.255.255.0",
            "router_id": "10.10.10.1",
            "lan_network": "192.168.10.0",
            "lan_wildcard": "0.0.0.255"
        },
        {
            "hostname": "branch-router-02", 
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "wan_description": "WAN to ISP",
            "wan_ip": "203.0.113.14",
            "wan_mask": "255.255.255.252", 
            "lan_description": "LAN Interface",
            "lan_ip": "192.168.20.1",
            "lan_mask": "255.255.255.0",
            "router_id": "20.20.20.1",
            "lan_network": "192.168.20.0",
            "lan_wildcard": "0.0.0.255"
        }
    ]
    
    # Generate configurations for each device
    for device in devices:
        config = template.format(**device)
        filename = f"{device['hostname']}_config.cfg"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(config)
        
        print(f"✓ Generated configuration for {device['hostname']}")
    
    # Example 2: Backup verification
    print("\n2. Backup file verification:")
    
    backup_files = [f"{device['hostname']}_config.cfg" for device in devices]
    
    for backup_file in backup_files:
        if os.path.exists(backup_file):
            with open(backup_file, "r", encoding="utf-8") as file:
                lines = file.readlines()
                
                # Verify backup integrity
                has_hostname = any("hostname" in line for line in lines)
                has_interfaces = any("interface" in line for line in lines)
                has_end = any("end" in line.strip() for line in lines)
                
                if has_hostname and has_interfaces and has_end:
                    print(f"✓ {backup_file}: Backup verified ({len(lines)} lines)")
                else:
                    print(f"✗ {backup_file}: Backup may be incomplete")
        else:
            print(f"✗ {backup_file}: File not found")
    
    # Example 3: Log analysis
    print("\n3. Log file analysis:")
    
    # Create a sample log file
    log_entries = [
        "Oct 26 14:30:01 router-01 %OSPF-5-ADJCHG: Process 1, Nbr 192.168.1.2 on GigabitEthernet0/1 from LOADING to FULL",
        "Oct 26 14:30:15 router-01 %SYS-5-CONFIG_I: Configured from console by admin on vty0",
        "Oct 26 14:31:00 router-01 %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up",
        "Oct 26 14:31:01 router-01 %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up",
        "Oct 26 14:32:15 router-01 %OSPF-5-ADJCHG: Process 1, Nbr 192.168.1.3 on GigabitEthernet0/2 from LOADING to FULL"
    ]
    
    with open("router_logs.txt", "w", encoding="utf-8") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
    
    # Analyze the logs
    with open("router_logs.txt", "r", encoding="utf-8") as file:
        error_count = 0
        warning_count = 0
        info_count = 0
        
        for line in file:
            if "%-3-" in line:  # Error level
                error_count += 1
            elif "%-4-" in line:  # Warning level  
                warning_count += 1
            elif "%-5-" in line:  # Info level
                info_count += 1
    
    print(f"Log analysis results:")
    print(f"  Error messages: {error_count}")
    print(f"  Warning messages: {warning_count}")
    print(f"  Info messages: {info_count}")
    
    return backup_files + ["devices.json", "network.log", "router_logs.txt", "sample_config.txt", "router_config.cfg"]


def cleanup_demo_files(files_to_clean):
    """Clean up demonstration files."""
    print("\n=== Cleanup ===\n")
    
    for filename in files_to_clean:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Removed: {filename}")
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")


if __name__ == "__main__":
    try:
        why_use_context_managers()
        basic_context_manager_examples()
        advanced_context_manager_examples()
        context_manager_with_error_handling()
        demo_files = practical_network_automation_examples()
        
        print("\n" + "="*50)
        response = input("Clean up demo files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_demo_files(demo_files)
        
        print("\n=== Context Manager Demo Complete ===")
        print("\nKey takeaways:")
        print("• Always use 'with open()' instead of manual open/close")
        print("• Context managers handle cleanup automatically")
        print("• Files are closed even if exceptions occur")
        print("• More readable and maintainable code")
        print("• Pythonic best practice for resource management")
        print("• Specify encoding='utf-8' for text files")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()