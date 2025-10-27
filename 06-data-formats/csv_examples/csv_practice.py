"""
🎯 CSV Practice - Master Spreadsheet Data!

Your mission: Learn to work with CSV files, the universal format for device inventories, 
reports, and bulk data operations that work perfectly with Excel!

🔥 What makes this exciting?
- CSV works with every spreadsheet program
- Perfect for device inventories and reports
- Super fast to read and write
- Great for bulk network operations

📚 Study the main README first to understand CSV basics!

💡 Pro Tip: CSV is like a simple table - rows and columns separated by commas.
"""

import csv

def read_device_csv():
    """
    TODO: Learn to read CSV files and work with device inventories.
    
    This simulates reading device reports from network monitoring systems.
    Most systems can export device lists as CSV files!
    """
    print("🔸 Reading CSV device list:")
    
    try:
        # TODO: Create an empty list to store devices
        devices = []
        
        # TODO: Open devices.csv file and create a CSV reader
        # Hint: Use csv.DictReader to automatically handle headers
        # Replace this comment with your code:
        
        # TODO: Read all rows into the devices list
        # Hint: Loop through the csv_reader and append each row
        
        # TODO: Print how many devices were loaded
        print(f"   ✅ Loaded ? devices from CSV")  # Replace ? with len(devices)
        
        return devices  # Return the list so other functions can use it
        
    except FileNotFoundError:
        print("   ❌ devices.csv file not found!")
        return []
    except Exception as e:
        print(f"   ❌ Error reading CSV: {e}")
        return []

def analyze_device_types(devices):
    """
    TODO: Count different types of devices from CSV data.
    
    Real-world scenario: Creating summary reports of your network inventory.
    """
    print("🔸 Device summary:")
    
    if not devices:
        print("   ❌ No device data available")
        return
    
    try:
        # TODO: Create an empty dictionary to count device types
        device_types = {}
        
        # TODO: Loop through all devices
        # For each device, get the 'type' field
        # Count how many of each type we have
        # Hint: Use device['type'] to get the type
        
        # TODO: Display the results
        # Format: "📊 router: 2 devices"
        
        pass  # Replace with your counting logic
        
    except Exception as e:
        print(f"   ❌ Error analyzing devices: {e}")

def find_offline_devices(devices):
    """
    TODO: Find devices that are offline and need attention.
    
    Network monitoring scenario: Quickly identify problem devices from status reports.
    """
    print("🔸 Checking device status:")
    
    if not devices:
        print("   ❌ No device data available")
        return
    
    try:
        # TODO: Create an empty list for offline devices
        offline_devices = []
        
        # TODO: Loop through all devices
        # Check if device['status'] == 'offline'
        # Add offline devices to the list
        
        # TODO: Display results
        if offline_devices:
            print(f"   ⚠️  ? offline devices:")  # Replace ? with count
            # TODO: Show each offline device
            # Format: "❌ router2 in branch"
        else:
            print("   ✅ All devices are online!")
            
    except Exception as e:
        print(f"   ❌ Error checking status: {e}")

def create_status_report(devices):
    """
    TODO: Generate a CSV report summarizing device status by location.
    
    Management scenario: Create executive reports from raw device data.
    """
    print("🔸 Creating status report:")
    
    if not devices:
        print("   ❌ No device data available")
        return
    
    try:
        # TODO: Create a dictionary to track statistics by location
        locations = {}
        
        # TODO: Process each device to count totals by location
        # For each location, track: total_devices, online_devices, offline_devices
        # Hint: Check if location already exists in dictionary
        
        # TODO: Write the report to status_report.csv
        # Use csv.writer to create the file
        # Include headers: location, total_devices, online_devices, offline_devices
        
        print("   ✅ Status report saved to status_report.csv")
        
    except Exception as e:
        print(f"   ❌ Error creating report: {e}")

def add_new_devices():
    """
    TODO: Learn to write new data to CSV files.
    
    Scenario: Adding new devices to your inventory system.
    """
    print("🔸 Adding new devices to inventory:")
    
    try:
        # TODO: Define new devices to add
        # Create a list with 2-3 new device dictionaries
        # Include: hostname, ip, type, location, status
        new_devices = [
            # TODO: Add device dictionaries here
            # Example: {"hostname": "switch3", "ip": "192.168.1.10", ...}
        ]
        
        # TODO: Append new devices to the CSV file
        # Hint: Open in 'a' (append) mode
        # Use csv.DictWriter with the proper fieldnames
        
        print(f"   ✅ Added ? new devices to devices_updated.csv")  # Replace ?
        
    except Exception as e:
        print(f"   ❌ Error adding devices: {e}")

def csv_tips():
    """
    Display helpful tips for working with CSV in network automation.
    """
    print("💡 CSV Pro Tips:")
    print("   • CSV files open directly in Excel and Google Sheets")
    print("   • Use DictReader/DictWriter for automatic header handling")
    print("   • Perfect for device inventories and monitoring reports")
    print("   • Always specify newline='' when writing to avoid blank rows")
    print("   • Use 'utf-8' encoding for special characters in device names")

def main():
    """
    Run all CSV practice exercises step by step.
    """
    print("=== 🎯 CSV Practice Challenge ===")
    print()
    print("Master CSV - the universal spreadsheet format!")
    print("=" * 50)
    print()
    
    # TODO: Learn to read CSV files
    
    # TODO: Analyze the data

    
    # TODO: Find problem devices

    
    # TODO: Create management reports

    
    # TODO: Add new data

    
    # Bonus: Tips for success
    csv_tips()
    print()
    
    print("🎉 CSV Practice Complete!")
    print("🚀 Next: Try YAML practice to learn configuration file formats!")

if __name__ == "__main__":
    main()