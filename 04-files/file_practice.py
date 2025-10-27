"""
🚀 File Operations Practice - Your Network Automation Workshop!

Ready to learn file handling for network automation? Let's start simple and build up!

TODO: Complete each section to build a device backup system step by step.
Hint: Run the program after each TODO to see your progress!
"""

def create_device_list():
    """
    Step 1: Create a simple device inventory file
    TODO: Write device information to a text file
    """
    print("=== Creating Device Inventory ===")
    
    # TODO: Create a simple device list (hint: use a multi-line string)
    device_data = """Router-01,192.168.1.1
Switch-01,192.168.1.10  
Firewall-01,192.168.1.100"""
    
    filename = "devices.txt"
    
    # TODO: Write the device data to a file
    # Hint: Use 'w' mode and don't forget encoding='utf-8'
    
    print(f"✓ Created {filename} with device list!")


def read_device_list():
    """
    Step 2: Read the device inventory back
    TODO: Open and read the file we just created
    """
    print("\n=== Reading Device Inventory ===")
    
    filename = "devices.txt"
    
    # TODO: Read and display the file contents
    # Hint: Use 'r' mode and the 'with' statement for safe file handling
    
    print("Device list loaded successfully!")


def backup_device_config():
    """
    Step 3: Create a configuration backup
    TODO: Create a backup file with current timestamp
    """
    print("\n=== Creating Config Backup ===")
    
    # Sample router configuration
    config = """!
hostname Router-01
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
end"""
    
    # TODO: Create a backup filename with timestamp
    # Hint: Use datetime to create unique backup names
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"router_backup_{timestamp}.cfg"
    
    # TODO: Save the configuration to the backup file
    
    print(f"✓ Backup saved as {backup_filename}")


def safe_file_operations():
    """
    Step 4: Handle file errors gracefully
    TODO: Add error handling to make your code bulletproof
    """
    print("\n=== Safe File Operations ===")
    
    # TODO: Try to read a file that might not exist
    # Hint: Use try/except to handle FileNotFoundError
    
    test_filename = "maybe_exists.txt"
    
    # Your error handling code goes here!
    
    print("Error handling complete!")


def main():
    """
    Your file operations workshop - run each step!
    """
    print("🚀 Welcome to File Operations Practice!\n")
    
    # Step by step file operations
    create_device_list()
    read_device_list() 
    backup_device_config()
    safe_file_operations()
    
    print("\n🎉 Great job! You're becoming a file operations expert!")
    print("\n💡 Try this: Modify the device list and run again!")


if __name__ == "__main__":
    main()