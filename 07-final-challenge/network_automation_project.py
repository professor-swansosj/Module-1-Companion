"""
Network Automation Project - Final Challenge

This is the capstone project that integrates all concepts learned in Module 1.
It demonstrates a complete network automation workflow combining:
- Functions and classes
- File operations
- Error handling
- Data format processing (JSON, CSV, YAML, XML)
- Object-oriented design principles

Project: Network Device Configuration Manager
"""

import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


class NetworkDevice:
    """Base class for network devices."""
    
    def __init__(self, hostname, ip_address, device_type, vendor="Unknown", model="Unknown"):
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.vendor = vendor
        self.model = model
        self.interfaces = []
        self.configuration = {}
        self.last_backup = None
        self.status = "Unknown"
    
    def __str__(self):
        return f"{self.device_type} {self.hostname} ({self.ip_address})"
    
    def __repr__(self):
        return f"NetworkDevice('{self.hostname}', '{self.ip_address}', '{self.device_type}')"
    
    def add_interface(self, interface_name, description="", vlan=None, ip_address=""):
        """Add an interface to the device."""
        interface = {
            "name": interface_name,
            "description": description,
            "vlan": vlan,
            "ip_address": ip_address,
            "status": "down",
            "enabled": False
        }
        self.interfaces.append(interface)
        return interface
    
    def configure_interface(self, interface_name, **kwargs):
        """Configure an existing interface."""
        for interface in self.interfaces:
            if interface["name"] == interface_name:
                interface.update(kwargs)
                return True
        return False
    
    def get_interface(self, interface_name):
        """Get interface by name."""
        for interface in self.interfaces:
            if interface["name"] == interface_name:
                return interface
        return None
    
    def set_configuration(self, config_key, config_value):
        """Set a configuration parameter."""
        self.configuration[config_key] = config_value
    
    def get_configuration(self, config_key, default=None):
        """Get a configuration parameter."""
        return self.configuration.get(config_key, default)
    
    def backup_config(self):
        """Mark device as backed up."""
        self.last_backup = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert device to dictionary for serialization."""
        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "device_type": self.device_type,
            "vendor": self.vendor,
            "model": self.model,
            "interfaces": self.interfaces.copy(),
            "configuration": self.configuration.copy(),
            "last_backup": self.last_backup,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create device from dictionary."""
        device = cls(
            hostname=data["hostname"],
            ip_address=data["ip_address"],
            device_type=data["device_type"],
            vendor=data.get("vendor", "Unknown"),
            model=data.get("model", "Unknown")
        )
        device.interfaces = data.get("interfaces", [])
        device.configuration = data.get("configuration", {})
        device.last_backup = data.get("last_backup")
        device.status = data.get("status", "Unknown")
        return device


class Router(NetworkDevice):
    """Router-specific functionality."""
    
    def __init__(self, hostname, ip_address, vendor="Unknown", model="Unknown"):
        super().__init__(hostname, ip_address, "Router", vendor, model)
        self.routing_protocols = []
        self.static_routes = []
    
    def add_routing_protocol(self, protocol, process_id=None, **kwargs):
        """Add a routing protocol configuration."""
        protocol_config = {
            "protocol": protocol,
            "process_id": process_id,
            "config": kwargs
        }
        self.routing_protocols.append(protocol_config)
        return protocol_config
    
    def add_static_route(self, destination, next_hop, metric=1):
        """Add a static route."""
        route = {
            "destination": destination,
            "next_hop": next_hop,
            "metric": metric
        }
        self.static_routes.append(route)
        return route
    
    def to_dict(self):
        """Convert router to dictionary including routing info."""
        data = super().to_dict()
        data.update({
            "routing_protocols": self.routing_protocols.copy(),
            "static_routes": self.static_routes.copy()
        })
        return data


class Switch(NetworkDevice):
    """Switch-specific functionality."""
    
    def __init__(self, hostname, ip_address, vendor="Unknown", model="Unknown"):
        super().__init__(hostname, ip_address, "Switch", vendor, model)
        self.vlans = []
        self.spanning_tree_config = {}
    
    def add_vlan(self, vlan_id, name, description=""):
        """Add a VLAN configuration."""
        vlan = {
            "id": vlan_id,
            "name": name,
            "description": description
        }
        self.vlans.append(vlan)
        return vlan
    
    def configure_port(self, port_name, mode="access", vlan=1, allowed_vlans=None):
        """Configure a switch port."""
        port_config = {
            "mode": mode,
            "vlan": vlan,
            "allowed_vlans": allowed_vlans or []
        }
        
        # Add or update interface
        interface = self.get_interface(port_name)
        if interface:
            interface.update(port_config)
        else:
            interface = self.add_interface(port_name)
            interface.update(port_config)
        
        return interface
    
    def to_dict(self):
        """Convert switch to dictionary including VLAN info."""
        data = super().to_dict()
        data.update({
            "vlans": self.vlans.copy(),
            "spanning_tree_config": self.spanning_tree_config.copy()
        })
        return data


class NetworkInventoryManager:
    """Manages network device inventory and configurations."""
    
    def __init__(self, data_directory="network_data"):
        self.devices = {}
        self.data_directory = Path(data_directory)
        self.data_directory.mkdir(exist_ok=True)
        
        # Create subdirectories
        (self.data_directory / "configs").mkdir(exist_ok=True)
        (self.data_directory / "backups").mkdir(exist_ok=True)
        (self.data_directory / "reports").mkdir(exist_ok=True)
    
    def add_device(self, device):
        """Add a device to the inventory."""
        if not isinstance(device, NetworkDevice):
            raise TypeError("Device must be a NetworkDevice instance")
        
        self.devices[device.hostname] = device
        return device
    
    def get_device(self, hostname):
        """Get a device by hostname."""
        return self.devices.get(hostname)
    
    def remove_device(self, hostname):
        """Remove a device from inventory."""
        if hostname in self.devices:
            del self.devices[hostname]
            return True
        return False
    
    def list_devices(self, device_type=None, vendor=None, status=None):
        """List devices with optional filters."""
        filtered_devices = []
        
        for device in self.devices.values():
            if device_type and device.device_type != device_type:
                continue
            if vendor and device.vendor != vendor:
                continue
            if status and device.status != status:
                continue
            
            filtered_devices.append(device)
        
        return filtered_devices
    
    def save_inventory_json(self, filename="inventory.json"):
        """Save inventory to JSON file."""
        filepath = self.data_directory / filename
        
        try:
            inventory_data = {
                "metadata": {
                    "export_date": datetime.now().isoformat(),
                    "total_devices": len(self.devices),
                    "format_version": "1.0"
                },
                "devices": {hostname: device.to_dict() 
                          for hostname, device in self.devices.items()}
            }
            
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(inventory_data, file, indent=2, ensure_ascii=False)
            
            print(f"✓ Saved inventory to {filepath}")
            return str(filepath)
        
        except Exception as e:
            print(f"✗ Failed to save inventory: {e}")
            raise
    
    def load_inventory_json(self, filename="inventory.json"):
        """Load inventory from JSON file."""
        filepath = self.data_directory / filename
        
        if not filepath.exists():
            print(f"✗ Inventory file {filepath} not found")
            return False
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                inventory_data = json.load(file)
            
            # Clear existing devices
            self.devices.clear()
            
            # Load devices
            devices_data = inventory_data.get("devices", {})
            for hostname, device_data in devices_data.items():
                device_type = device_data.get("device_type", "NetworkDevice")
                
                # Create appropriate device type
                if device_type == "Router":
                    device = Router.from_dict(device_data)
                    # Restore router-specific data
                    device.routing_protocols = device_data.get("routing_protocols", [])
                    device.static_routes = device_data.get("static_routes", [])
                elif device_type == "Switch":
                    device = Switch.from_dict(device_data)
                    # Restore switch-specific data
                    device.vlans = device_data.get("vlans", [])
                    device.spanning_tree_config = device_data.get("spanning_tree_config", {})
                else:
                    device = NetworkDevice.from_dict(device_data)
                
                self.devices[hostname] = device
            
            print(f"✓ Loaded {len(self.devices)} devices from {filepath}")
            return True
        
        except Exception as e:
            print(f"✗ Failed to load inventory: {e}")
            return False
    
    def export_csv_report(self, filename="device_report.csv"):
        """Export device inventory to CSV format."""
        filepath = self.data_directory / "reports" / filename
        
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # Write header
                headers = [
                    "Hostname", "IP_Address", "Device_Type", "Vendor", "Model",
                    "Interface_Count", "Status", "Last_Backup", "Configuration_Items"
                ]
                writer.writerow(headers)
                
                # Write device data
                for device in self.devices.values():
                    row = [
                        device.hostname,
                        device.ip_address,
                        device.device_type,
                        device.vendor,
                        device.model,
                        len(device.interfaces),
                        device.status,
                        device.last_backup or "Never",
                        len(device.configuration)
                    ]
                    writer.writerow(row)
            
            print(f"✓ Exported CSV report to {filepath}")
            return str(filepath)
        
        except Exception as e:
            print(f"✗ Failed to export CSV report: {e}")
            raise
    
    def import_csv_devices(self, filename):
        """Import devices from CSV file."""
        filepath = Path(filename)
        
        if not filepath.exists():
            print(f"✗ CSV file {filepath} not found")
            return False
        
        try:
            imported_count = 0
            
            with open(filepath, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    hostname = row.get("Hostname", "").strip()
                    ip_address = row.get("IP_Address", "").strip()
                    device_type = row.get("Device_Type", "NetworkDevice").strip()
                    vendor = row.get("Vendor", "Unknown").strip()
                    model = row.get("Model", "Unknown").strip()
                    
                    if not hostname or not ip_address:
                        print(f"⚠ Skipping row with missing hostname or IP: {row}")
                        continue
                    
                    # Create device based on type
                    if device_type == "Router":
                        device = Router(hostname, ip_address, vendor, model)
                    elif device_type == "Switch":
                        device = Switch(hostname, ip_address, vendor, model)
                    else:
                        device = NetworkDevice(hostname, ip_address, device_type, vendor, model)
                    
                    device.status = row.get("Status", "Unknown")
                    
                    self.add_device(device)
                    imported_count += 1
            
            print(f"✓ Imported {imported_count} devices from {filepath}")
            return True
        
        except Exception as e:
            print(f"✗ Failed to import CSV devices: {e}")
            return False
    
    def generate_xml_config(self, hostname, filename=None):
        """Generate XML configuration for a device."""
        device = self.get_device(hostname)
        if not device:
            print(f"✗ Device {hostname} not found")
            return None
        
        if not filename:
            filename = f"{hostname}_config.xml"
        
        filepath = self.data_directory / "configs" / filename
        
        try:
            # Create XML structure
            root = ET.Element("device-configuration")
            root.set("hostname", device.hostname)
            root.set("generated", datetime.now().isoformat())
            
            # Device info
            device_info = ET.SubElement(root, "device-info")
            
            ET.SubElement(device_info, "hostname").text = device.hostname
            ET.SubElement(device_info, "ip-address").text = device.ip_address
            ET.SubElement(device_info, "device-type").text = device.device_type
            ET.SubElement(device_info, "vendor").text = device.vendor
            ET.SubElement(device_info, "model").text = device.model
            
            # Interfaces
            if device.interfaces:
                interfaces_elem = ET.SubElement(root, "interfaces")
                
                for interface in device.interfaces:
                    intf_elem = ET.SubElement(interfaces_elem, "interface")
                    intf_elem.set("name", interface["name"])
                    
                    if interface.get("description"):
                        ET.SubElement(intf_elem, "description").text = interface["description"]
                    if interface.get("ip_address"):
                        ET.SubElement(intf_elem, "ip-address").text = interface["ip_address"]
                    if interface.get("vlan"):
                        ET.SubElement(intf_elem, "vlan").text = str(interface["vlan"])
                    
                    ET.SubElement(intf_elem, "enabled").text = str(interface.get("enabled", False)).lower()
            
            # Configuration parameters
            if device.configuration:
                config_elem = ET.SubElement(root, "configuration")
                
                for key, value in device.configuration.items():
                    param_elem = ET.SubElement(config_elem, "parameter")
                    param_elem.set("name", key)
                    param_elem.text = str(value)
            
            # Router-specific configuration
            if isinstance(device, Router):
                if device.routing_protocols:
                    routing_elem = ET.SubElement(root, "routing")
                    
                    for protocol in device.routing_protocols:
                        proto_elem = ET.SubElement(routing_elem, "protocol")
                        proto_elem.set("name", protocol["protocol"])
                        if protocol.get("process_id"):
                            proto_elem.set("process-id", str(protocol["process_id"]))
            
            # Switch-specific configuration
            elif isinstance(device, Switch):
                if device.vlans:
                    vlans_elem = ET.SubElement(root, "vlans")
                    
                    for vlan in device.vlans:
                        vlan_elem = ET.SubElement(vlans_elem, "vlan")
                        vlan_elem.set("id", str(vlan["id"]))
                        vlan_elem.set("name", vlan["name"])
                        if vlan.get("description"):
                            vlan_elem.text = vlan["description"]
            
            # Write XML file
            xml_string = ET.tostring(root, encoding='unicode')
            
            # Pretty print (simplified)
            lines = []
            depth = 0
            for char in xml_string:
                if char == '<':
                    if lines and not lines[-1].endswith('>'):
                        lines.append('\n' + '  ' * depth)
                    lines.append(char)
                elif char == '>':
                    lines.append(char)
                    if xml_string[xml_string.find(char):xml_string.find(char)+2] != '/>':
                        depth += 1
                else:
                    lines.append(char)
            
            with open(filepath, "w", encoding="utf-8") as file:
                file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                file.write(''.join(lines))
            
            print(f"✓ Generated XML configuration: {filepath}")
            return str(filepath)
        
        except Exception as e:
            print(f"✗ Failed to generate XML config: {e}")
            return None
    
    def backup_all_devices(self):
        """Perform backup operation on all devices."""
        print("\n=== Performing Device Backups ===\n")
        
        backup_results = {
            "successful": [],
            "failed": [],
            "timestamp": datetime.now().isoformat()
        }
        
        for hostname, device in self.devices.items():
            try:
                # Simulate backup operation
                print(f"Backing up {hostname}... ", end="")
                
                # Mark device as backed up
                device.backup_config()
                
                # Generate configuration file
                config_file = self.generate_xml_config(hostname)
                
                if config_file:
                    backup_results["successful"].append(hostname)
                    print("✓")
                else:
                    backup_results["failed"].append(hostname)
                    print("✗")
            
            except Exception as e:
                backup_results["failed"].append(f"{hostname}: {str(e)}")
                print(f"✗ Error: {e}")
        
        # Save backup report
        report_filename = f"backup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_filepath = self.data_directory / "reports" / report_filename
        
        try:
            with open(report_filepath, "w", encoding="utf-8") as file:
                json.dump(backup_results, file, indent=2)
            
            print(f"\n✓ Backup report saved: {report_filepath}")
        except Exception as e:
            print(f"\n✗ Failed to save backup report: {e}")
        
        print("\nBackup Summary:")
        print(f"  Successful: {len(backup_results['successful'])}")
        print(f"  Failed: {len(backup_results['failed'])}")
        
        return backup_results
    
    def get_inventory_statistics(self):
        """Get inventory statistics and summary."""
        stats = {
            "total_devices": len(self.devices),
            "by_type": {},
            "by_vendor": {},
            "by_status": {},
            "total_interfaces": 0,
            "backup_status": {
                "backed_up": 0,
                "never_backed_up": 0
            }
        }
        
        for device in self.devices.values():
            # Count by type
            device_type = device.device_type
            stats["by_type"][device_type] = stats["by_type"].get(device_type, 0) + 1
            
            # Count by vendor
            vendor = device.vendor
            stats["by_vendor"][vendor] = stats["by_vendor"].get(vendor, 0) + 1
            
            # Count by status
            status = device.status
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            
            # Count interfaces
            stats["total_interfaces"] += len(device.interfaces)
            
            # Backup status
            if device.last_backup:
                stats["backup_status"]["backed_up"] += 1
            else:
                stats["backup_status"]["never_backed_up"] += 1
        
        return stats


def demonstrate_network_automation_project():
    """Demonstrate the complete network automation project."""
    print("Network Device Configuration Manager")
    print("=" * 50)
    print("Integrating all Module 1 concepts:\n")
    
    try:
        # Initialize the inventory manager
        print("1. Initializing Network Inventory Manager...")
        manager = NetworkInventoryManager("demo_network_data")
        print("   ✓ Manager initialized with data directory structure\n")
        
        # Create sample devices
        print("2. Creating Network Devices...")
        
        # Create routers
        core_router = Router("core-router-01", "10.0.0.1", "Cisco", "ISR 4331")
        core_router.status = "Active"
        core_router.add_interface("GigabitEthernet0/0", "WAN to ISP", ip_address="203.0.113.10")
        core_router.add_interface("GigabitEthernet0/1", "LAN Interface", ip_address="192.168.1.1")
        core_router.add_routing_protocol("OSPF", process_id=1, router_id="1.1.1.1")
        core_router.add_static_route("0.0.0.0/0", "203.0.113.9")
        core_router.set_configuration("hostname", "core-router-01")
        core_router.set_configuration("domain_name", "company.local")
        
        branch_router = Router("branch-router-01", "10.1.0.1", "Cisco", "ISR 2901")
        branch_router.status = "Active"
        branch_router.add_interface("GigabitEthernet0/0", "Branch WAN")
        branch_router.add_interface("GigabitEthernet0/1", "Branch LAN")
        
        # Create switches
        core_switch = Switch("core-switch-01", "10.0.0.10", "Cisco", "Catalyst 3850")
        core_switch.status = "Active"
        core_switch.add_vlan(10, "Data", "User data network")
        core_switch.add_vlan(20, "Voice", "VoIP network")
        core_switch.add_vlan(99, "Management", "Network management")
        core_switch.configure_port("GigabitEthernet1/0/1", "access", 10)
        core_switch.configure_port("GigabitEthernet1/0/24", "trunk", allowed_vlans=[10, 20, 99])
        
        access_switch = Switch("access-switch-01", "10.0.0.11", "Cisco", "Catalyst 2960X")
        access_switch.status = "Active"
        access_switch.add_vlan(10, "Data")
        access_switch.add_vlan(20, "Voice")
        
        # Add devices to inventory
        manager.add_device(core_router)
        manager.add_device(branch_router)
        manager.add_device(core_switch)
        manager.add_device(access_switch)
        
        print(f"   ✓ Created and added {len(manager.devices)} devices to inventory\n")
        
        # Demonstrate file operations
        print("3. Demonstrating File Operations...")
        
        # Save inventory as JSON
        manager.save_inventory_json("network_inventory.json")
        
        # Export CSV report
        manager.export_csv_report("network_devices.csv")
        
        # Generate XML configs
        xml_files = []
        for hostname in manager.devices.keys():
            xml_file = manager.generate_xml_config(hostname)
            if xml_file:
                xml_files.append(xml_file)
        
        print(f"   ✓ Generated {len(xml_files)} XML configuration files\n")
        
        # Demonstrate error handling with backup operation
        print("4. Performing Device Backups (with error handling)...")
        manager.backup_all_devices()
        print()
        
        # Demonstrate data analysis
        print("5. Analyzing Inventory Data...")
        stats = manager.get_inventory_statistics()
        
        print("   Inventory Statistics:")
        print(f"     Total devices: {stats['total_devices']}")
        print(f"     Total interfaces: {stats['total_interfaces']}")
        
        print("   By Device Type:")
        for device_type, count in stats['by_type'].items():
            print(f"     {device_type}: {count}")
        
        print("   By Vendor:")
        for vendor, count in stats['by_vendor'].items():
            print(f"     {vendor}: {count}")
        
        print("   Backup Status:")
        print(f"     Backed up: {stats['backup_status']['backed_up']}")
        print(f"     Never backed up: {stats['backup_status']['never_backed_up']}")
        print()
        
        # Demonstrate filtering
        print("6. Filtering Devices...")
        cisco_devices = manager.list_devices(vendor="Cisco")
        routers = manager.list_devices(device_type="Router")
        active_devices = manager.list_devices(status="Active")
        
        print(f"   Cisco devices: {len(cisco_devices)}")
        print(f"   Routers: {len(routers)}")
        print(f"   Active devices: {len(active_devices)}")
        print()
        
        # Test loading from file
        print("7. Testing Data Persistence...")
        
        # Clear inventory and reload
        original_count = len(manager.devices)
        manager.devices.clear()
        print(f"   Cleared inventory ({original_count} → {len(manager.devices)} devices)")
        
        # Reload from JSON
        success = manager.load_inventory_json("network_inventory.json")
        if success:
            print(f"   Reloaded inventory ({len(manager.devices)} devices restored)")
            print("   ✓ Data persistence verified\n")
        
        # Final summary
        print("8. Project Summary...")
        print("   ✓ Object-oriented design with inheritance")
        print("   ✓ File operations (JSON, CSV, XML)")
        print("   ✓ Error handling and logging")
        print("   ✓ Data validation and analysis")
        print("   ✓ Configuration management")
        print("   ✓ Reporting and export functionality")
        print()
        
        # Cleanup option
        print("=" * 50)
        cleanup = input("Clean up demonstration files? (y/n): ").lower().strip()
        
        if cleanup in ['y', 'yes']:
            import shutil
            try:
                shutil.rmtree("demo_network_data")
                print("✓ Cleanup completed")
            except Exception as e:
                print(f"✗ Cleanup failed: {e}")
        else:
            print("Files preserved for inspection")
        
        print("\n🎉 Network Automation Project Complete!")
        print("\nKey achievements:")
        print("• Designed modular, extensible network device classes")
        print("• Implemented comprehensive inventory management")
        print("• Demonstrated multi-format data handling (JSON/CSV/XML)")
        print("• Applied proper error handling and validation")
        print("• Created automated backup and reporting workflows")
        print("• Integrated all Module 1 Python concepts successfully")
    
    except Exception as e:
        print(f"\n✗ Project error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    demonstrate_network_automation_project()