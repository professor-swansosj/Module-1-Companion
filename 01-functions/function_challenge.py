"""
🌟 Function Challenge - Take Your Skills Further! (Optional)

Ready for a bit more challenge? These exercises build on everything you learned!

If you completed function_basics.py, you now know:
✅ How to create basic functions
✅ How to use default parameters  
✅ How to handle multiple arguments (*args)
✅ How to use keyword arguments (**kwargs)

Now let's use those skills for some real network automation challenges!

TODO: Complete these functions using your new function skills.
Hint: Apply what you learned in the README and function_basics.py!
"""

def validate_ip_address(ip):
    """
    Bonus 1: Create a function that checks if an IP address looks valid
    TODO: Check if the IP has 4 numbers separated by dots
    """
    # TODO: Split the IP address by '.' and check if there are 4 parts
    # TODO: Check if each part is a number between 0 and 255
    # Hint: You can use split('.') and len() and int()
    
    # Return True if valid, False if not
    return False


def backup_device_config(device_name, config_type="running"):
    """
    Bonus 2: Create a backup filename with timestamp
    TODO: Generate a unique backup filename
    """
    # TODO: Import datetime at the top of the file
    # TODO: Create a timestamp string like "20241027_143000"
    # TODO: Create filename like "Router01_running_20241027_143000.cfg"
    
    filename = f"{device_name}_{config_type}_backup.cfg"
    print(f"✓ Backup saved as {filename}")
    return filename


def calculate_subnet_info(ip_address, subnet_mask):
    """
    Bonus 3: Calculate network information (Advanced!)
    TODO: Try to figure out network address and broadcast address
    """
    # This one is tricky! Try your best or just print the inputs for now
    print(f"Network: {ip_address} with mask {subnet_mask}")
    
    # TODO: If you're feeling ambitious, try to calculate:
    # - Network address
    # - Broadcast address  
    # - Number of host addresses
    
    return "Network info calculated!"


def main():
    """
    Test your bonus functions!
    """
    print("🌟 Welcome to Function Challenge!")
    print("These are optional - have fun with them!\n")
    
    # Test IP validation
    print("=== Testing IP Validation ===")
    test_ips = ["192.168.1.1", "10.0.0.256", "not.an.ip", "172.16.1.1"]
    for ip in test_ips:
        result = validate_ip_address(ip)
        print(f"{ip} is {'valid' if result else 'invalid'}")
    
    # Test backup function
    print("\n=== Testing Backup Function ===")
    backup_device_config("Router-01")
    backup_device_config("Switch-01", "startup")
    
    # Test subnet calculation
    print("\n=== Testing Subnet Function ===")
    calculate_subnet_info("192.168.1.10", "255.255.255.0")
    
    print("\n🎉 Excellent work on the bonus challenges!")
    print("💡 These functions would be really useful in network automation!")


if __name__ == "__main__":
    main()