"""
CSV Operations - Network Automation

This module demonstrates working with CSV (Comma Separated Values) files
for network automation. CSV is widely used for device inventories,
configuration imports, reporting, and data exchange.

Uses Python's built-in csv module for reading and writing CSV files.
"""

import csv
import os
from datetime import datetime, timedelta
import random


def create_sample_csv_files():
    """Create sample CSV files for demonstration."""
    print("=== Creating Sample CSV Files ===\n")
    
    # Device inventory CSV data
    device_inventory = [
        ['Hostname', 'IP_Address', 'Device_Type', 'Vendor', 'Model', 'OS_Version', 'Location', 'Status', 'Last_Backup'],
        ['core-router-01', '10.0.0.1', 'Router', 'Cisco', 'ISR 4331', '16.12.04', 'Data Center', 'Active', '2024-10-26'],
        ['core-switch-01', '10.0.0.10', 'Switch', 'Cisco', 'Catalyst 3850', '16.12.05', 'Data Center', 'Active', '2024-10-26'],
        ['access-switch-01', '10.0.0.11', 'Switch', 'Cisco', 'Catalyst 2960X', '15.2(7)E3', 'Floor 1 IDF', 'Active', '2024-10-25'],
        ['access-switch-02', '10.0.0.12', 'Switch', 'Cisco', 'Catalyst 2960X', '15.2(7)E3', 'Floor 2 IDF', 'Active', '2024-10-26'],
        ['branch-router-01', '10.1.0.1', 'Router', 'Cisco', 'ISR 2901', '15.9(3)M7', 'Branch Office', 'Active', '2024-10-25'],
        ['wireless-controller', '10.0.0.50', 'WLC', 'Cisco', 'WLC 5520', '8.10.185.0', 'Data Center', 'Active', '2024-10-26'],
        ['firewall-01', '10.0.0.100', 'Firewall', 'Fortinet', 'FortiGate 200F', '7.4.1', 'Data Center', 'Active', '2024-10-26'],
        ['old-switch-01', '10.0.0.99', 'Switch', 'HP', 'ProCurve 2524', '9.3.2', 'Storage Room', 'Deprecated', '2024-09-15'],
        ['backup-router-01', '10.2.0.1', 'Router', 'Juniper', 'SRX300', 'JUNOS 20.4R3', 'Branch Backup', 'Standby', '2024-10-20']
    ]
    
    # Interface status CSV data
    interface_status = [
        ['Device', 'Interface', 'Description', 'Status', 'VLAN', 'Speed', 'Duplex', 'Errors', 'Utilization_Percent'],
        ['core-router-01', 'GigabitEthernet0/0', 'WAN to ISP', 'up', 'N/A', '1000', 'full', '0', '25.4'],
        ['core-router-01', 'GigabitEthernet0/1', 'LAN to Core Switch', 'up', 'N/A', '1000', 'full', '0', '67.8'],
        ['core-switch-01', 'GigabitEthernet1/0/1', 'Uplink to Router', 'up', 'trunk', '1000', 'full', '0', '67.8'],
        ['core-switch-01', 'GigabitEthernet1/0/2', 'Link to Access SW 1', 'up', 'trunk', '1000', 'full', '0', '45.2'],
        ['core-switch-01', 'GigabitEthernet1/0/3', 'Link to Access SW 2', 'up', 'trunk', '1000', 'full', '0', '38.7'],
        ['access-switch-01', 'FastEthernet0/1', 'Workstation Port', 'up', '10', '100', 'full', '0', '12.3'],
        ['access-switch-01', 'FastEthernet0/2', 'Workstation Port', 'up', '10', '100', 'full', '0', '8.9'],
        ['access-switch-01', 'FastEthernet0/24', 'Phone Port', 'up', '20', '100', 'full', '0', '5.4'],
        ['access-switch-01', 'GigabitEthernet0/1', 'Uplink to Core', 'up', 'trunk', '1000', 'full', '0', '45.2'],
        ['access-switch-02', 'FastEthernet0/1', 'Workstation Port', 'down', '10', '100', 'auto', '3', '0.0'],
        ['access-switch-02', 'FastEthernet0/12', 'Server Port', 'up', '30', '1000', 'full', '0', '78.9']
    ]
    
    # VLAN database CSV data
    vlan_database = [
        ['VLAN_ID', 'Name', 'Description', 'Subnet', 'Gateway', 'DHCP_Server', 'Devices_Count'],
        ['1', 'default', 'Default VLAN', '192.168.1.0/24', '192.168.1.1', '192.168.1.1', '5'],
        ['10', 'Data', 'User Data Network', '192.168.10.0/24', '192.168.10.1', '192.168.10.5', '125'],
        ['20', 'Voice', 'VoIP Network', '192.168.20.0/24', '192.168.20.1', '192.168.20.5', '45'],
        ['30', 'Servers', 'Server Network', '192.168.30.0/24', '192.168.30.1', '192.168.30.10', '15'],
        ['40', 'Guest', 'Guest Access Network', '192.168.40.0/24', '192.168.40.1', '192.168.40.5', '8'],
        ['99', 'Management', 'Network Management', '192.168.99.0/24', '192.168.99.1', 'None', '12'],
        ['100', 'DMZ', 'Demilitarized Zone', '10.10.10.0/24', '10.10.10.1', 'None', '3']
    ]
    
    # Network performance data
    performance_data = [
        ['Timestamp', 'Device', 'CPU_Percent', 'Memory_Percent', 'Temperature_C', 'Power_W', 'Fan_Speed_RPM'],
        ['2024-10-26 09:00:00', 'core-router-01', '15.2', '42.8', '45', '85', '2100'],
        ['2024-10-26 09:15:00', 'core-router-01', '18.7', '43.1', '46', '87', '2150'],
        ['2024-10-26 09:30:00', 'core-router-01', '12.4', '42.5', '44', '84', '2050'],
        ['2024-10-26 09:00:00', 'core-switch-01', '8.9', '31.2', '38', '120', '1800'],
        ['2024-10-26 09:15:00', 'core-switch-01', '11.3', '32.7', '39', '122', '1850'],
        ['2024-10-26 09:30:00', 'core-switch-01', '7.6', '30.8', '37', '118', '1750'],
        ['2024-10-26 09:00:00', 'firewall-01', '25.4', '58.9', '52', '95', '2400'],
        ['2024-10-26 09:15:00', 'firewall-01', '28.1', '61.2', '54', '98', '2500'],
        ['2024-10-26 09:30:00', 'firewall-01', '22.8', '57.3', '50', '92', '2300']
    ]
    
    files_created = []
    
    # Write CSV files
    csv_data = [
        ("device_inventory.csv", device_inventory),
        ("interface_status.csv", interface_status),
        ("vlan_database.csv", vlan_database),
        ("performance_data.csv", performance_data)
    ]
    
    for filename, data in csv_data:
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"✓ Created {filename} ({len(data)-1} data rows)")
            files_created.append(filename)
        except Exception as e:
            print(f"✗ Failed to create {filename}: {e}")
    
    return files_created


def read_csv_file(filename):
    """Read and display CSV file contents."""
    print(f"\n=== Reading CSV File: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return None
    
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            # Read with csv.reader
            reader = csv.reader(file)
            rows = list(reader)
        
        if not rows:
            print("✗ File is empty")
            return None
        
        # Display header and sample data
        headers = rows[0]
        data_rows = rows[1:]
        
        print(f"Headers ({len(headers)} columns): {', '.join(headers)}")
        print(f"Data rows: {len(data_rows)}")
        
        # Display first few rows
        print("\nSample data (first 5 rows):")
        for i, row in enumerate(data_rows[:5], 1):
            print(f"  Row {i}: {dict(zip(headers, row))}")
        
        if len(data_rows) > 5:
            print(f"  ... and {len(data_rows) - 5} more rows")
        
        return {"headers": headers, "data": data_rows}
    
    except Exception as e:
        print(f"✗ Error reading {filename}: {e}")
        return None


def read_csv_as_dictionaries(filename):
    """Read CSV file as list of dictionaries using DictReader."""
    print(f"\n=== Reading CSV as Dictionaries: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return None
    
    try:
        devices = []
        
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            print(f"Field names: {reader.fieldnames}")
            
            for row_num, row in enumerate(reader, 1):
                devices.append(row)
                
                # Show first few rows
                if row_num <= 3:
                    print(f"\nRow {row_num}:")
                    for key, value in row.items():
                        print(f"  {key}: {value}")
        
        print(f"\n✓ Loaded {len(devices)} records as dictionaries")
        return devices
    
    except Exception as e:
        print(f"✗ Error reading {filename}: {e}")
        return None


def analyze_device_inventory(filename):
    """Analyze device inventory data from CSV."""
    print(f"\n=== Analyzing Device Inventory: {filename} ===\n")
    
    devices = read_csv_as_dictionaries(filename)
    if not devices:
        return
    
    # Analyze by vendor
    vendor_counts = {}
    device_type_counts = {}
    status_counts = {}
    location_counts = {}
    
    for device in devices:
        vendor = device.get('Vendor', 'Unknown')
        device_type = device.get('Device_Type', 'Unknown')
        status = device.get('Status', 'Unknown')
        location = device.get('Location', 'Unknown')
        
        vendor_counts[vendor] = vendor_counts.get(vendor, 0) + 1
        device_type_counts[device_type] = device_type_counts.get(device_type, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1
        location_counts[location] = location_counts.get(location, 0) + 1
    
    print("Analysis Results:")
    print(f"  Total devices: {len(devices)}")
    
    print(f"\n  By Vendor:")
    for vendor, count in sorted(vendor_counts.items()):
        print(f"    {vendor}: {count} devices")
    
    print(f"\n  By Device Type:")
    for device_type, count in sorted(device_type_counts.items()):
        print(f"    {device_type}: {count} devices")
    
    print(f"\n  By Status:")
    for status, count in sorted(status_counts.items()):
        print(f"    {status}: {count} devices")
    
    print(f"\n  By Location:")
    for location, count in sorted(location_counts.items()):
        print(f"    {location}: {count} devices")
    
    # Find devices needing attention
    print(f"\n  Devices Needing Attention:")
    outdated_backups = []
    non_active_devices = []
    
    for device in devices:
        hostname = device.get('Hostname', 'Unknown')
        status = device.get('Status', 'Unknown')
        last_backup = device.get('Last_Backup', '')
        
        if status != 'Active':
            non_active_devices.append(f"{hostname} ({status})")
        
        # Check backup date (simplified check)
        if last_backup and '2024-10-25' > last_backup:
            outdated_backups.append(f"{hostname} (last backup: {last_backup})")
    
    if non_active_devices:
        print(f"    Non-active devices: {', '.join(non_active_devices)}")
    
    if outdated_backups:
        print(f"    Outdated backups: {', '.join(outdated_backups)}")
    
    if not non_active_devices and not outdated_backups:
        print(f"    ✓ All devices are active with recent backups")


def analyze_interface_utilization(filename):
    """Analyze interface utilization from CSV data."""
    print(f"\n=== Analyzing Interface Utilization: {filename} ===\n")
    
    interfaces = read_csv_as_dictionaries(filename)
    if not interfaces:
        return
    
    # Analyze utilization
    high_utilization = []
    down_interfaces = []
    error_interfaces = []
    
    total_up = 0
    total_down = 0
    utilization_sum = 0
    
    for interface in interfaces:
        device = interface.get('Device', 'Unknown')
        intf_name = interface.get('Interface', 'Unknown')
        status = interface.get('Status', 'Unknown').lower()
        utilization = interface.get('Utilization_Percent', '0')
        errors = interface.get('Errors', '0')
        
        try:
            util_percent = float(utilization)
            error_count = int(errors)
        except (ValueError, TypeError):
            util_percent = 0
            error_count = 0
        
        if status == 'up':
            total_up += 1
            utilization_sum += util_percent
            
            if util_percent > 80:
                high_utilization.append(f"{device} {intf_name} ({util_percent}%)")
        elif status == 'down':
            total_down += 1
            down_interfaces.append(f"{device} {intf_name}")
        
        if error_count > 0:
            error_interfaces.append(f"{device} {intf_name} ({error_count} errors)")
    
    print("Interface Analysis Results:")
    print(f"  Total interfaces: {len(interfaces)}")
    print(f"  Up: {total_up}, Down: {total_down}")
    
    if total_up > 0:
        avg_utilization = utilization_sum / total_up
        print(f"  Average utilization (up interfaces): {avg_utilization:.1f}%")
    
    if high_utilization:
        print(f"\n  High utilization interfaces (>80%):")
        for interface in high_utilization:
            print(f"    ⚠ {interface}")
    
    if down_interfaces:
        print(f"\n  Down interfaces:")
        for interface in down_interfaces:
            print(f"    ⚠ {interface}")
    
    if error_interfaces:
        print(f"\n  Interfaces with errors:")
        for interface in error_interfaces:
            print(f"    ⚠ {interface}")
    
    if not high_utilization and not down_interfaces and not error_interfaces:
        print(f"\n  ✓ All interfaces operating normally")


def generate_network_report_csv():
    """Generate a network status report in CSV format."""
    print("\n=== Generating Network Status Report ===\n")
    
    # Simulate current network data
    current_time = datetime.now()
    report_data = [
        ['Report_Date', 'Device', 'Status', 'Uptime_Hours', 'CPU_Percent', 'Memory_Percent', 'Alerts']
    ]
    
    devices = [
        'core-router-01', 'core-switch-01', 'access-switch-01', 
        'access-switch-02', 'firewall-01', 'wireless-controller'
    ]
    
    for device in devices:
        # Simulate device data
        status = random.choice(['Online', 'Online', 'Online', 'Degraded'])  # Mostly online
        uptime = random.randint(24, 8760)  # 1 day to 1 year
        cpu = round(random.uniform(5.0, 95.0), 1)
        memory = round(random.uniform(20.0, 90.0), 1)
        
        alerts = []
        if cpu > 80:
            alerts.append('High CPU')
        if memory > 85:
            alerts.append('High Memory')
        if status == 'Degraded':
            alerts.append('Performance Issue')
        
        alert_string = '; '.join(alerts) if alerts else 'None'
        
        report_data.append([
            current_time.strftime('%Y-%m-%d %H:%M:%S'),
            device,
            status,
            str(uptime),
            str(cpu),
            str(memory),
            alert_string
        ])
    
    # Write report
    report_filename = f"network_status_report_{current_time.strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(report_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(report_data)
        
        print(f"✓ Generated report: {report_filename}")
        
        # Display summary
        online_count = sum(1 for row in report_data[1:] if row[2] == 'Online')
        total_devices = len(report_data) - 1
        
        print(f"  Devices online: {online_count}/{total_devices}")
        
        # Show alerts
        alert_devices = [row[1] for row in report_data[1:] if row[6] != 'None']
        if alert_devices:
            print(f"  Devices with alerts: {', '.join(alert_devices)}")
        else:
            print(f"  ✓ No alerts")
        
        return [report_filename]
    
    except Exception as e:
        print(f"✗ Failed to generate report: {e}")
        return []


def filter_and_export_csv(input_filename, output_filename, filter_criteria):
    """Filter CSV data and export to new file."""
    print(f"\n=== Filtering {input_filename} → {output_filename} ===\n")
    
    devices = read_csv_as_dictionaries(input_filename)
    if not devices:
        return []
    
    print(f"Filter criteria: {filter_criteria}")
    
    # Apply filters
    filtered_devices = []
    
    for device in devices:
        include_device = True
        
        for field, value in filter_criteria.items():
            device_value = device.get(field, '').lower()
            filter_value = str(value).lower()
            
            if filter_value not in device_value:
                include_device = False
                break
        
        if include_device:
            filtered_devices.append(device)
    
    print(f"Filtered results: {len(filtered_devices)}/{len(devices)} devices match criteria")
    
    if not filtered_devices:
        print("No devices match the filter criteria")
        return []
    
    # Write filtered data to new CSV
    try:
        with open(output_filename, "w", newline="", encoding="utf-8") as file:
            if filtered_devices:
                fieldnames = filtered_devices[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(filtered_devices)
        
        print(f"✓ Exported filtered data to: {output_filename}")
        
        # Show sample of filtered data
        print("\nFiltered devices:")
        for i, device in enumerate(filtered_devices[:3], 1):
            hostname = device.get('Hostname', 'Unknown')
            device_type = device.get('Device_Type', 'Unknown')
            vendor = device.get('Vendor', 'Unknown')
            print(f"  {i}. {hostname} ({vendor} {device_type})")
        
        if len(filtered_devices) > 3:
            print(f"  ... and {len(filtered_devices) - 3} more")
        
        return [output_filename]
    
    except Exception as e:
        print(f"✗ Failed to export filtered data: {e}")
        return []


def create_network_config_template():
    """Create a CSV template for bulk network configuration."""
    print("\n=== Creating Network Configuration Template ===\n")
    
    config_template = [
        ['Device', 'Interface', 'Action', 'VLAN', 'Description', 'IP_Address', 'Subnet_Mask', 'Enabled'],
        ['switch-01', 'FastEthernet0/1', 'configure', '10', 'Workstation Port 1', '', '', 'true'],
        ['switch-01', 'FastEthernet0/2', 'configure', '10', 'Workstation Port 2', '', '', 'true'],
        ['switch-01', 'FastEthernet0/24', 'configure', '20', 'Phone Port', '', '', 'true'],
        ['switch-01', 'GigabitEthernet0/1', 'configure', 'trunk', 'Uplink Port', '', '', 'true'],
        ['router-01', 'GigabitEthernet0/0', 'configure', '', 'WAN Interface', '203.0.113.10', '255.255.255.252', 'true'],
        ['router-01', 'GigabitEthernet0/1', 'configure', '', 'LAN Interface', '192.168.1.1', '255.255.255.0', 'true'],
        ['router-01', 'Loopback0', 'create', '', 'Management Interface', '1.1.1.1', '255.255.255.255', 'true']
    ]
    
    template_filename = "network_config_template.csv"
    
    try:
        with open(template_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(config_template)
        
        print(f"✓ Created configuration template: {template_filename}")
        print(f"  Template contains {len(config_template)-1} configuration entries")
        
        # Show template structure
        print("\nTemplate columns:")
        for i, column in enumerate(config_template[0], 1):
            print(f"  {i}. {column}")
        
        print("\nSample entries:")
        for i, row in enumerate(config_template[1:4], 1):
            print(f"  {i}. Device: {row[0]}, Interface: {row[1]}, Action: {row[2]}")
        
        return [template_filename]
    
    except Exception as e:
        print(f"✗ Failed to create template: {e}")
        return []


def validate_csv_data(filename):
    """Validate CSV data for common issues."""
    print(f"\n=== Validating CSV Data: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return
    
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if not rows:
            print("✗ File is empty")
            return
        
        headers = rows[0]
        data_rows = rows[1:]
        
        print("Validation Results:")
        print(f"  Total rows: {len(rows)} (1 header + {len(data_rows)} data)")
        print(f"  Columns: {len(headers)}")
        
        # Check for common issues
        issues = []
        
        # Check for empty rows
        empty_rows = [i+2 for i, row in enumerate(data_rows) if not any(cell.strip() for cell in row)]
        if empty_rows:
            issues.append(f"Empty rows found: {empty_rows}")
        
        # Check for inconsistent column counts
        inconsistent_rows = []
        expected_cols = len(headers)
        for i, row in enumerate(data_rows):
            if len(row) != expected_cols:
                inconsistent_rows.append(f"Row {i+2}: {len(row)} cols (expected {expected_cols})")
        
        if inconsistent_rows:
            issues.append(f"Inconsistent column counts: {inconsistent_rows[:3]}")
        
        # Check for duplicate headers
        duplicate_headers = [header for header in set(headers) if headers.count(header) > 1]
        if duplicate_headers:
            issues.append(f"Duplicate headers: {duplicate_headers}")
        
        # Check for missing values in critical fields (assume first column is critical)
        if headers:
            critical_field = headers[0]
            missing_critical = [i+2 for i, row in enumerate(data_rows) 
                              if not row or not row[0].strip()]
            if missing_critical:
                issues.append(f"Missing {critical_field}: rows {missing_critical[:5]}")
        
        # Report validation results
        if issues:
            print(f"\n  ⚠ Issues found:")
            for issue in issues:
                print(f"    - {issue}")
        else:
            print(f"\n  ✓ No validation issues found")
        
        # Show data quality summary
        if data_rows:
            non_empty_cells = sum(1 for row in data_rows for cell in row if cell.strip())
            total_cells = len(data_rows) * len(headers)
            completeness = (non_empty_cells / total_cells) * 100 if total_cells > 0 else 0
            print(f"  Data completeness: {completeness:.1f}%")
    
    except Exception as e:
        print(f"✗ Validation failed: {e}")


def cleanup_csv_files(*file_lists):
    """Clean up CSV demonstration files."""
    print("\n=== Cleanup ===\n")
    
    all_files = []
    for file_list in file_lists:
        if isinstance(file_list, list):
            all_files.extend(file_list)
        elif isinstance(file_list, str):
            all_files.append(file_list)
    
    for filename in all_files:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Removed: {filename}")
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")


if __name__ == "__main__":
    try:
        print("CSV Operations for Network Automation")
        print("=" * 40)
        
        # Create sample CSV files
        csv_files = create_sample_csv_files()
        
        # Demonstrate CSV reading and analysis
        for csv_file in csv_files:
            read_csv_file(csv_file)
            validate_csv_data(csv_file)
            
            if csv_file == "device_inventory.csv":
                analyze_device_inventory(csv_file)
            elif csv_file == "interface_status.csv":
                analyze_interface_utilization(csv_file)
        
        # Generate reports and templates
        report_files = generate_network_report_csv()
        template_files = create_network_config_template()
        
        # Demonstrate filtering
        if "device_inventory.csv" in csv_files:
            filter_criteria = {"Vendor": "Cisco", "Status": "Active"}
            filtered_files = filter_and_export_csv(
                "device_inventory.csv", 
                "cisco_active_devices.csv", 
                filter_criteria
            )
        else:
            filtered_files = []
        
        print("\n" + "="*50)
        response = input("Clean up demonstration files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_csv_files(csv_files, report_files, template_files, filtered_files)
        
        print("\n=== CSV Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• CSV is simple, universal format for tabular data")
        print("• Use csv.DictReader for easier data access by column name")
        print("• Always validate CSV data before processing")
        print("• Excel and database systems easily import/export CSV")
        print("• Good for device inventories, configuration imports, reports")
        print("• Use newline='' parameter to avoid extra blank lines")
        print("• Handle encoding properly (UTF-8 recommended)")
        print("• Consider data types when processing CSV values (all strings by default)")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()