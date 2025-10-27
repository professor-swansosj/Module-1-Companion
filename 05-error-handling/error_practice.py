"""
🎯 Error Practice - Handle Problems Like a Pro!

Your mission: Learn to catch and handle errors gracefully so your network automation
keeps running even when things go wrong (and they will go wrong!).

📚 STUDY THE README FIRST! It shows you how to find error names and handle them.
"""

# ====================================================================
# PART 1: BASIC ERROR HANDLING - Your Safety Net
# ====================================================================

def basic_error_examples():
    """
    Learn the fundamentals of try-except error handling.
    
    Study the README section on "The Try-Except Pattern" first!
    """
    print("1️⃣ Basic Error Handling Examples:")
    print()
    
    # Example 1: Division by zero (we know this will break!)
    print("🔸 Handling division by zero:")
    try:
        result = 10 / 0  # This will cause ZeroDivisionError!
    except ZeroDivisionError:
        print("   ❌ Can't divide by zero - handled gracefully!")
        result = 0  # Set a safe default value
    print(f"   Result: {result}")
    print()
    
    # Example 2: Invalid number conversion
    print("🔸 Handling invalid number conversion:")
    bad_input = "not_a_number"
    try:
        number = int(bad_input)  # This will cause ValueError!
    except ValueError:
        print(f"   ❌ '{bad_input}' is not a valid number - using default")
        number = 0
    print(f"   Number: {number}")
    print()

def practice_basic_errors():
    """
    TODO: Practice basic error handling
    
    Complete the TODOs to practice handling common errors.
    """
    print("2️⃣ Your Turn - Practice Basic Error Handling:")
    print()
    
    # TODO: Handle list index errors
    print("🔸 Practice with list index errors:")
    devices = ["router1", "switch1", "firewall1"]
    
    try:
        # TODO: Try to access index 5 (doesn't exist!)
        device = devices[5]
        print(f"Device: {device}")
    except IndexError:
        # TODO: Print a helpful error message and use a safe default
        print("   ❌ Device index doesn't exist - using first device")
        device = devices[0]
    
    print(f"   Selected device: {device}")
    print()
    
    # TODO: Handle dictionary key errors  
    print("🔸 Practice with dictionary key errors:")
    device_info = {"hostname": "router1", "ip": "192.168.1.1"}
    
    try:
        # TODO: Try to access a key that doesn't exist
        location = device_info["location"]  # This key doesn't exist!
        print(f"Location: {location}")
    except KeyError:
        # TODO: Handle missing key gracefully
        print("   ❌ Location not found - using default")
        location = "Unknown"
    
    print(f"   Device location: {location}")
    print()

# ====================================================================
# PART 2: FILE HANDLING ERRORS - Missing Files and Permissions
# ====================================================================

def file_error_examples():
    """
    Learn to handle file-related errors gracefully.
    
    Study the README section on finding error names!
    """
    print("3️⃣ File Error Handling:")
    print()
    
    # Example 1: File not found
    print("🔸 Handling missing files:")
    try:
        with open("nonexistent_config.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("   ❌ Config file not found - creating default")
        content = "hostname DefaultRouter\n"
    print(f"   Config content preview: {content[:30]}...")
    print()
    
    # Example 2: Creating files safely
    print("🔸 Safe file creation:")
    try:
        with open("test_config.txt", "w") as file:
            file.write("hostname TestRouter\ninterface gi0/0\n no shutdown\n")
        print("   ✅ Test config file created successfully!")
    except PermissionError:
        print("   ❌ Permission denied - can't create file")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
    print()

def practice_file_errors():
    """
    TODO: Practice file error handling
    
    Complete the TODOs to handle file operations safely.
    """
    print("4️⃣ Your Turn - Practice File Error Handling:")
    print()
    
    # List of config files to try reading
    config_files = ["router1.cfg", "switch1.cfg", "missing.cfg"]
    
    for filename in config_files:
        print(f"🔸 Trying to read {filename}:")
        try:
            # TODO: Try to open and read the file
            with open(filename, "r") as file:
                content = file.read()
            print(f"   ✅ Read {len(content)} characters from {filename}")
            
        except FileNotFoundError:
            # TODO: Handle file not found error
            print(f"   ❌ {filename} not found - file doesn't exist")
            
        except PermissionError:
            # TODO: Handle permission denied error
            print(f"   ❌ {filename} permission denied - can't read file")
            
        except Exception as e:
            # TODO: Handle any other unexpected errors
            print(f"   ❌ {filename} unexpected error: {e}")
    
    print()

# ====================================================================
# PART 3: NETWORK SIMULATION ERRORS - Connection Problems  
# ====================================================================

def simulate_network_errors():
    """
    Simulate common network automation errors and handle them.
    
    These are the errors you'll see ALL THE TIME in network automation!
    """
    print("5️⃣ Network Error Simulation:")
    print()
    
    def fake_ping(ip_address):
        """Simulate pinging a device (sometimes it fails!)"""
        import random
        if random.choice([True, False]):  # 50% chance of success
            return f"{ip_address} is reachable"
        else:
            raise ConnectionError(f"Could not reach {ip_address}")
    
    def fake_ssh_connect(hostname):
        """Simulate SSH connection (sometimes it times out!)"""
        import random
        failure_type = random.choice(["success", "timeout", "auth_fail"])
        
        if failure_type == "success":
            return f"Connected to {hostname}"
        elif failure_type == "timeout":
            raise TimeoutError(f"Connection to {hostname} timed out")
        else:
            raise ConnectionError(f"Authentication failed for {hostname}")
    
    # Test network operations on multiple devices
    devices = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    hostnames = ["router1", "switch1", "firewall1"]
    
    print("🔸 Testing ping operations:")
    for ip in devices:
        try:
            result = fake_ping(ip)
            print(f"   ✅ {result}")
        except ConnectionError as e:
            print(f"   ❌ Ping failed: {e}")
    print()
    
    print("🔸 Testing SSH connections:")
    for hostname in hostnames:
        try:
            result = fake_ssh_connect(hostname)
            print(f"   ✅ {result}")
        except TimeoutError as e:
            print(f"   ⏱️ Timeout: {e}")
        except ConnectionError as e:
            print(f"   🔐 Auth error: {e}")
    print()

def practice_network_errors():
    """
    TODO: Practice handling network automation errors
    
    Complete the TODOs to handle network errors gracefully.
    """
    print("6️⃣ Your Turn - Practice Network Error Handling:")
    print()
    
    def backup_device(device_name):
        """
        Simulate backing up a device configuration.
        
        TODO: Add error handling for network operations
        """
        import random
        
        print(f"🔧 Attempting backup of {device_name}:")
        
        try:
            # Simulate different failure scenarios
            failure = random.choice(["success", "connection", "timeout", "file_error"])
            
            if failure == "connection":
                raise ConnectionError(f"Cannot connect to {device_name}")
            elif failure == "timeout":
                raise TimeoutError(f"Backup of {device_name} timed out")
            elif failure == "file_error":
                raise FileNotFoundError("Cannot save backup file")
            
            # Success case
            print(f"   ✅ {device_name} backup completed successfully!")
            return True
            
        except ConnectionError as e:
            # TODO: Handle connection errors
            print(f"   ❌ Connection failed: {e}")
            return False
            
        except TimeoutError as e:
            # TODO: Handle timeout errors
            print(f"   ⏱️ Operation timed out: {e}")
            return False
            
        except FileNotFoundError as e:
            # TODO: Handle file save errors
            print(f"   💾 File error: {e}")
            return False
            
        except Exception as e:
            # TODO: Handle any other unexpected errors
            print(f"   ❓ Unexpected error: {e}")
            return False
    
    # Test backup on multiple devices
    devices_to_backup = ["CORE-R1", "ACCESS-SW1", "BORDER-FW1", "MGMT-SW1"]
    successful_backups = 0
    
    for device in devices_to_backup:
        if backup_device(device):
            successful_backups += 1
        print()  # Add space between devices
    
    print(f"📊 Backup Summary: {successful_backups}/{len(devices_to_backup)} devices backed up successfully")
    print()

# ====================================================================
# PART 4: FINALLY BLOCKS - Always Clean Up!
# ====================================================================

def demonstrate_finally():
    """
    Learn when and how to use finally blocks for cleanup.
    
    Study the README section on "Always Clean Up with Finally"!
    """
    print("7️⃣ Finally Blocks - Cleanup No Matter What:")
    print()
    
    def configure_device_with_cleanup(device_name, should_fail=False):
        """
        Demonstrate finally block for cleanup operations.
        """
        connection = None
        temp_file = f"{device_name}_temp.cfg"
        
        try:
            print(f"🔧 Configuring {device_name}:")
            
            # Simulate establishing connection
            print(f"   📡 Connecting to {device_name}...")
            connection = f"SSH_connection_to_{device_name}"
            
            # Create temporary file
            print(f"   📄 Creating temp config file...")
            with open(temp_file, "w") as f:
                f.write(f"hostname {device_name}\n")
            
            # Simulate failure if requested
            if should_fail:
                raise ConnectionError(f"Lost connection to {device_name}")
            
            print(f"   ✅ {device_name} configured successfully!")
            
        except ConnectionError as e:
            print(f"   ❌ Configuration failed: {e}")
            
        finally:
            # This ALWAYS runs, even if there was an error!
            print(f"   🧹 Cleaning up resources for {device_name}:")
            
            # Close connection if it exists
            if connection:
                print(f"      🔌 Closing connection: {connection}")
            
            # Remove temporary file if it exists
            try:
                import os
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"      🗑️  Removed temp file: {temp_file}")
            except Exception:
                print(f"      ❌ Could not remove temp file: {temp_file}")
    
    # Test with success and failure scenarios
    print("🔸 Testing successful configuration:")
    configure_device_with_cleanup("ROUTER-SUCCESS", should_fail=False)
    print()
    
    print("🔸 Testing failed configuration (cleanup still happens!):")
    configure_device_with_cleanup("ROUTER-FAILURE", should_fail=True)
    print()

# ====================================================================
# MAIN PROGRAM - Put It All Together!
# ====================================================================

def main():
    """
    Run through all error handling examples and practice.
    """
    print("=== 🎯 Error Handling Practice Challenge ===")
    print()
    print("Learn to handle errors gracefully so your code keeps running!")
    print("=" * 60)
    print()
    
    # Run all the examples and practice exercises
    basic_error_examples()
    practice_basic_errors()
    file_error_examples()
    practice_file_errors()
    simulate_network_errors()
    practice_network_errors()
    demonstrate_finally()
    
    print("=" * 60)
    print("🎉 Error Handling Challenge Complete!")
    print()
    print("🏆 You've learned to handle:")
    print("   ✅ Basic errors (ZeroDivisionError, ValueError, IndexError)")
    print("   ✅ File errors (FileNotFoundError, PermissionError)")
    print("   ✅ Network errors (ConnectionError, TimeoutError)")
    print("   ✅ Cleanup with finally blocks")
    print()
    print("💡 Key Insights:")
    print("   • Always expect things to break in network automation!")
    print("   • Use specific error names from Python tracebacks")
    print("   • Handle errors gracefully to keep your scripts running")
    print("   • Use finally blocks for important cleanup operations")
    print()
    print("🚀 Next Steps:")
    print("   • Practice with real network libraries (like netmiko)")
    print("   • Add logging to capture errors for later review")
    print("   • Learn about retry logic for temporary failures")
    print("   • Build robust automation that handles partial failures")

if __name__ == "__main__":
    main()