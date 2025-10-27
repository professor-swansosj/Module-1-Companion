"""
YAML Operations - Network Automation

This module demonstrates working with YAML (YAML Ain't Markup Language) files
for network automation. YAML is human-readable and commonly used for configuration
files, Ansible playbooks, and infrastructure as code.

Note: This example uses basic string parsing for YAML-like format since PyYAML
may not be installed. In production, use the 'yaml' module after installing PyYAML.
"""

import os
import json
from datetime import datetime


def create_sample_yaml_files():
    """Create sample YAML files for demonstration."""
    print("=== Creating Sample YAML Files ===\n")
    
    # Network configuration YAML
    network_config = """# Network Infrastructure Configuration
# YAML format for network automation
---
network:
  domain_name: "company.local"
  dns_servers:
    - "8.8.8.8"
    - "8.8.4.4"
    - "1.1.1.1"
  
  ntp_servers:
    - "0.pool.ntp.org"
    - "1.pool.ntp.org"
    - "time.google.com"

vlans:
  - id: 10
    name: "Data"
    description: "User data network"
    subnet: "192.168.10.0/24"
    gateway: "192.168.10.1"
  
  - id: 20
    name: "Voice"
    description: "VoIP network"
    subnet: "192.168.20.0/24"
    gateway: "192.168.20.1"
  
  - id: 30
    name: "Guest"
    description: "Guest access network"
    subnet: "192.168.30.0/24"
    gateway: "192.168.30.1"

devices:
  routers:
    - hostname: "core-router-01"
      model: "Cisco ISR 4331"
      ip_address: "10.0.0.1"
      interfaces:
        - name: "GigabitEthernet0/0"
          description: "WAN Interface"
          ip_address: "203.0.113.10"
          subnet_mask: "255.255.255.252"
        - name: "GigabitEthernet0/1"
          description: "LAN Interface"
          ip_address: "192.168.1.1"
          subnet_mask: "255.255.255.0"
      
      routing:
        ospf:
          process_id: 1
          router_id: "1.1.1.1"
          networks:
            - network: "192.168.1.0"
              wildcard: "0.0.0.255"
              area: 0
    
    - hostname: "branch-router-01"
      model: "Cisco ISR 2901"
      ip_address: "10.0.0.2"
      interfaces:
        - name: "GigabitEthernet0/0"
          description: "Branch WAN"
          ip_address: "203.0.113.20"
          subnet_mask: "255.255.255.252"
        - name: "GigabitEthernet0/1"
          description: "Branch LAN"
          ip_address: "192.168.100.1"
          subnet_mask: "255.255.255.0"

  switches:
    - hostname: "access-switch-01"
      model: "Cisco Catalyst 2960X"
      ip_address: "10.0.0.10"
      management_vlan: 99
      vlans: [10, 20, 30, 99]
      
      port_config:
        - ports: "1-12"
          vlan: 10
          description: "Workstation ports"
        - ports: "13-24"
          vlan: 20
          description: "Phone ports"
        - ports: "25-26"
          mode: "trunk"
          allowed_vlans: "10,20,30,99"
          description: "Uplink ports"

monitoring:
  snmp:
    enabled: true
    community: "public"
    version: "2c"
    
  syslog:
    enabled: true
    servers:
      - ip: "10.0.0.100"
        port: 514
        facility: "local0"
    
  netflow:
    enabled: false
    collector_ip: "10.0.0.101"
    port: 2055

security:
  access_lists:
    - name: "BLOCK_P2P"
      type: "extended"
      rules:
        - action: "deny"
          protocol: "tcp"
          source: "any"
          destination: "any"
          port_range: "1024-65535"
        - action: "permit" 
          protocol: "ip"
          source: "any"
          destination: "any"
  
  authentication:
    enable_password: "encrypted_password_hash"
    username: "admin"
    privilege_level: 15
    
backup:
  schedule: "daily"
  retention_days: 30
  storage_location: "/backup/configs/"
  encryption: true
"""

    # Ansible-style playbook YAML
    ansible_playbook = """---
- name: "Configure Network Infrastructure"
  hosts: network_devices
  gather_facts: false
  connection: network_cli
  
  vars:
    dns_servers:
      - "8.8.8.8"
      - "8.8.4.4"
    
    ntp_servers:
      - "0.pool.ntp.org"
      - "1.pool.ntp.org"
    
    snmp_community: "network_monitoring"
    
  tasks:
    - name: "Configure hostname"
      ios_config:
        lines:
          - "hostname {{ inventory_hostname }}"
      
    - name: "Configure DNS servers"
      ios_config:
        lines:
          - "ip name-server {{ item }}"
      loop: "{{ dns_servers }}"
      
    - name: "Configure NTP servers"
      ios_config:
        lines:
          - "ntp server {{ item }}"
      loop: "{{ ntp_servers }}"
      
    - name: "Configure SNMP"
      ios_config:
        lines:
          - "snmp-server community {{ snmp_community }} RO"
          - "snmp-server location {{ device_location | default('Unknown') }}"
          - "snmp-server contact Network Team"
      
    - name: "Configure interfaces"
      ios_config:
        lines:
          - "description {{ item.description }}"
          - "ip address {{ item.ip_address }} {{ item.subnet_mask }}"
          - "no shutdown"
        parents: "interface {{ item.name }}"
      loop: "{{ device_interfaces }}"
      when: device_interfaces is defined
      
    - name: "Save configuration"
      ios_config:
        save_when: always

- name: "Configure VLANs on switches"
  hosts: switches
  gather_facts: false
  connection: network_cli
  
  vars:
    vlans:
      - { id: 10, name: "Data" }
      - { id: 20, name: "Voice" }
      - { id: 30, name: "Guest" }
      - { id: 99, name: "Management" }
  
  tasks:
    - name: "Create VLANs"
      ios_config:
        lines:
          - "name {{ item.name }}"
        parents: "vlan {{ item.id }}"
      loop: "{{ vlans }}"
      
    - name: "Configure access ports"
      ios_config:
        lines:
          - "switchport mode access"
          - "switchport access vlan {{ item.vlan }}"
          - "description {{ item.description }}"
        parents: "interface range {{ item.ports }}"
      loop: "{{ port_configurations }}"
      when: port_configurations is defined and item.mode != 'trunk'
"""

    # Device inventory YAML
    device_inventory = """---
# Network Device Inventory
# Format: YAML for easy human editing

inventory:
  created_date: "2024-10-26"
  created_by: "Network Team"
  version: "1.2"
  
locations:
  datacenter:
    name: "Primary Data Center"
    address: "123 Server Lane, Tech City"
    contact: "datacenter@company.com"
    
  branch_office:
    name: "Branch Office - Downtown"
    address: "456 Business Ave, Downtown"
    contact: "branch@company.com"

device_categories:
  routers:
    - hostname: "dc-core-rtr-01"
      vendor: "Cisco"
      model: "ASR 1001-X"
      serial: "ABC123456789"
      ip_address: "10.0.0.1"
      management_ip: "192.168.100.1"
      location: "datacenter"
      rack: "A1"
      position: "1U"
      purchase_date: "2023-01-15"
      warranty_expires: "2026-01-14"
      os_version: "16.12.04"
      config_backup: true
      monitoring: true
      
    - hostname: "branch-edge-rtr-01"
      vendor: "Cisco"
      model: "ISR 4331"
      serial: "DEF987654321"
      ip_address: "10.0.1.1"
      management_ip: "192.168.101.1"
      location: "branch_office"
      rack: "B1"
      position: "2U"
      purchase_date: "2023-06-20"
      warranty_expires: "2026-06-19"
      os_version: "16.09.05"
      config_backup: true
      monitoring: true
  
  switches:
    - hostname: "dc-access-sw-01"
      vendor: "Cisco"
      model: "Catalyst 2960X-48FPS-L"
      serial: "GHI123456789"
      ip_address: "10.0.0.10"
      management_ip: "192.168.100.10"
      location: "datacenter"
      rack: "A1"
      position: "10U"
      port_count: 48
      poe_ports: 48
      stack_member: false
      vlans: [1, 10, 20, 30, 99]
      
    - hostname: "dc-access-sw-02"
      vendor: "Cisco"
      model: "Catalyst 2960X-48FPS-L" 
      serial: "GHI987654321"
      ip_address: "10.0.0.11"
      management_ip: "192.168.100.11"
      location: "datacenter"
      rack: "A1"
      position: "11U"
      port_count: 48
      poe_ports: 48
      stack_member: false
      vlans: [1, 10, 20, 30, 99]

  firewalls:
    - hostname: "dc-firewall-01"
      vendor: "Fortinet"
      model: "FortiGate 200F"
      serial: "FGT200F1234567890"
      ip_address: "10.0.0.100"
      management_ip: "192.168.100.100"
      location: "datacenter"
      rack: "A1"
      position: "5U"
      license_expires: "2025-12-31"
      firmware_version: "7.4.1"
      
  wireless:
    - hostname: "dc-wlc-01"
      vendor: "Cisco"
      model: "WLC 5520"
      serial: "WLC123456789"
      ip_address: "10.0.0.50"
      management_ip: "192.168.100.50"
      location: "datacenter"
      rack: "A2"
      position: "3U"
      max_aps: 500
      current_aps: 45

maintenance:
  schedules:
    weekly:
      - day: "Sunday"
        time: "02:00"
        tasks: ["config_backup", "log_rotation"]
        
    monthly:
      - day: "first_sunday"
        time: "03:00"
        tasks: ["firmware_check", "license_audit", "performance_report"]
        
    quarterly:
      - tasks: ["security_audit", "capacity_planning", "disaster_recovery_test"]

contacts:
  network_team:
    - name: "Alice Johnson"
      role: "Senior Network Engineer"
      email: "alice.johnson@company.com"
      phone: "+1-555-0101"
      
  vendors:
    cisco:
      support_contract: "CON-SNT-12345"
      phone: "+1-800-553-6387"
      email: "support@cisco.com"
      
    fortinet:
      support_contract: "FC-10-12345-900-02-12"
      phone: "+1-866-648-4638"
      email: "support@fortinet.com"
"""
    
    files_created = []
    
    # Write the YAML files
    yaml_files = [
        ("network_config.yaml", network_config),
        ("ansible_playbook.yaml", ansible_playbook), 
        ("device_inventory.yaml", device_inventory)
    ]
    
    for filename, content in yaml_files:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"✓ Created {filename}")
            files_created.append(filename)
        except Exception as e:
            print(f"✗ Failed to create {filename}: {e}")
    
    return files_created


def parse_yaml_manually(filename):
    """Parse YAML-like content manually (simplified parser for demonstration)."""
    print(f"\n=== Parsing YAML File: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return None
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        parsed_data = {}
        current_section = None
        indent_stack = []
        
        for line_num, line in enumerate(lines, 1):
            original_line = line
            line = line.rstrip()
            
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                continue
            
            # Skip YAML document markers
            if line.strip() in ['---', '...']:
                continue
            
            # Calculate indentation
            indent = len(line) - len(line.lstrip())
            content = line.lstrip()
            
            # Simple key-value parsing
            if ':' in content and not content.startswith('-'):
                key, value = content.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                
                print(f"Line {line_num}: Key='{key}', Value='{value}', Indent={indent}")
                
                # Store in parsed data (simplified structure)
                if not value:  # Section header
                    current_section = key
                    if current_section not in parsed_data:
                        parsed_data[current_section] = {}
                else:  # Key-value pair
                    if current_section:
                        parsed_data[current_section][key] = value
                    else:
                        parsed_data[key] = value
            
            elif content.startswith('-'):
                # List item
                item = content[1:].strip()
                print(f"Line {line_num}: List item='{item}', Indent={indent}")
        
        print(f"\nParsed {len(parsed_data)} top-level sections")
        return parsed_data
    
    except Exception as e:
        print(f"✗ Error parsing {filename}: {e}")
        return None


def demonstrate_yaml_to_json_conversion():
    """Demonstrate converting YAML-like structure to JSON."""
    print("\n=== YAML to JSON Conversion ===\n")
    
    # Simple YAML-like data structure
    yaml_like_data = {
        "network": {
            "domain_name": "company.local",
            "dns_servers": ["8.8.8.8", "8.8.4.4"],
            "vlans": [
                {"id": 10, "name": "Data", "subnet": "192.168.10.0/24"},
                {"id": 20, "name": "Voice", "subnet": "192.168.20.0/24"}
            ]
        },
        "devices": {
            "routers": [
                {
                    "hostname": "core-router-01",
                    "ip_address": "10.0.0.1",
                    "model": "Cisco ISR 4331"
                }
            ]
        }
    }
    
    # Convert to JSON
    try:
        json_output = json.dumps(yaml_like_data, indent=2)
        
        # Save to file
        with open("converted_config.json", "w", encoding="utf-8") as file:
            file.write(json_output)
        
        print("✓ Converted YAML-like data to JSON format:")
        print(json_output[:300] + "..." if len(json_output) > 300 else json_output)
        
        return ["converted_config.json"]
    
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        return []


def analyze_yaml_structure(filename):
    """Analyze YAML file structure and provide statistics."""
    print(f"\n=== Analyzing YAML Structure: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        stats = {
            "total_lines": len(lines),
            "comment_lines": 0,
            "empty_lines": 0,
            "content_lines": 0,
            "max_indent": 0,
            "sections": [],
            "keys": [],
            "list_items": 0
        }
        
        for line in lines:
            original_line = line
            line = line.rstrip()
            
            if not line.strip():
                stats["empty_lines"] += 1
            elif line.strip().startswith('#'):
                stats["comment_lines"] += 1  
            else:
                stats["content_lines"] += 1
                
                # Calculate indentation
                indent = len(line) - len(line.lstrip())
                stats["max_indent"] = max(stats["max_indent"], indent)
                
                content = line.lstrip()
                
                # Identify sections, keys, and list items
                if content.startswith('-'):
                    stats["list_items"] += 1
                elif ':' in content:
                    key = content.split(':', 1)[0].strip()
                    value = content.split(':', 1)[1].strip()
                    
                    if not value:  # Section header
                        stats["sections"].append(key)
                    else:  # Regular key
                        stats["keys"].append(key)
        
        # Display analysis
        print("File Statistics:")
        print(f"  Total lines: {stats['total_lines']}")
        print(f"  Content lines: {stats['content_lines']}")
        print(f"  Comment lines: {stats['comment_lines']}")
        print(f"  Empty lines: {stats['empty_lines']}")
        print(f"  Maximum indentation: {stats['max_indent']} spaces")
        print(f"  List items: {stats['list_items']}")
        
        print(f"\nSections found ({len(stats['sections'])}):")
        for section in stats["sections"][:10]:  # Show first 10
            print(f"  - {section}")
        if len(stats["sections"]) > 10:
            print(f"  ... and {len(stats['sections']) - 10} more")
        
        print(f"\nKeys found ({len(stats['keys'])}):")
        for key in stats["keys"][:15]:  # Show first 15
            print(f"  - {key}")
        if len(stats["keys"]) > 15:
            print(f"  ... and {len(stats['keys']) - 15} more")
    
    except Exception as e:
        print(f"✗ Analysis failed: {e}")


def create_yaml_from_python_data():
    """Create YAML content from Python data structures."""
    print("\n=== Creating YAML from Python Data ===\n")
    
    # Network device data
    device_data = {
        "hostname": "test-router-01",
        "vendor": "Cisco",
        "model": "ISR 4331",
        "ip_address": "192.168.1.1",
        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "description": "WAN Interface",
                "ip_address": "203.0.113.10",
                "subnet_mask": "255.255.255.252",
                "enabled": True
            },
            {
                "name": "GigabitEthernet0/1", 
                "description": "LAN Interface",
                "ip_address": "192.168.1.1",
                "subnet_mask": "255.255.255.0",
                "enabled": True
            }
        ],
        "routing": {
            "protocols": ["OSPF", "BGP"],
            "ospf": {
                "process_id": 1,
                "router_id": "1.1.1.1",
                "networks": [
                    {"network": "192.168.1.0/24", "area": "0"},
                    {"network": "203.0.113.8/30", "area": "0"}
                ]
            }
        },
        "management": {
            "snmp": {
                "enabled": True,
                "community": "public",
                "location": "Data Center Rack 1"
            },
            "logging": {
                "enabled": True,
                "server": "10.0.0.100",
                "level": "informational"
            }
        }
    }
    
    def dict_to_yaml(data, indent=0):
        """Convert dictionary to YAML format (simplified)."""
        yaml_lines = []
        indent_str = "  " * indent
        
        for key, value in data.items():
            if isinstance(value, dict):
                yaml_lines.append(f"{indent_str}{key}:")
                yaml_lines.extend(dict_to_yaml(value, indent + 1))
            elif isinstance(value, list):
                yaml_lines.append(f"{indent_str}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        yaml_lines.append(f"{indent_str}  -")
                        for subkey, subvalue in item.items():
                            if isinstance(subvalue, (str, int, float, bool)):
                                yaml_lines.append(f"{indent_str}    {subkey}: {subvalue}")
                    else:
                        yaml_lines.append(f"{indent_str}  - {item}")
            else:
                yaml_lines.append(f"{indent_str}{key}: {value}")
        
        return yaml_lines
    
    try:
        # Convert to YAML format
        yaml_lines = ["---", "# Generated YAML configuration", f"# Created: {datetime.now().isoformat()}", ""]
        yaml_lines.extend(dict_to_yaml(device_data))
        
        yaml_content = "\n".join(yaml_lines)
        
        # Save to file
        output_file = "generated_config.yaml"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(yaml_content)
        
        print(f"✓ Generated YAML configuration: {output_file}")
        print("Sample content:")
        print(yaml_content[:400] + "..." if len(yaml_content) > 400 else yaml_content)
        
        return [output_file]
    
    except Exception as e:
        print(f"✗ YAML generation failed: {e}")
        return []


def cleanup_yaml_files(*file_lists):
    """Clean up YAML demonstration files."""
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
        print("YAML Operations for Network Automation")
        print("=" * 45)
        
        # Create sample files
        yaml_files = create_sample_yaml_files()
        
        # Parse and analyze YAML files
        for yaml_file in yaml_files:
            parse_yaml_manually(yaml_file)
            analyze_yaml_structure(yaml_file)
        
        # Demonstrate conversions
        json_files = demonstrate_yaml_to_json_conversion()
        generated_files = create_yaml_from_python_data()
        
        print("\n" + "="*50)
        response = input("Clean up demonstration files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_yaml_files(yaml_files, json_files, generated_files)
        
        print("\n=== YAML Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• YAML is human-readable and great for configuration files")
        print("• Indentation is significant in YAML (use spaces, not tabs)")
        print("• YAML supports complex data structures (lists, dictionaries)")
        print("• Common in Ansible, Kubernetes, and CI/CD pipelines")
        print("• Use PyYAML library for production parsing: pip install pyyaml")
        print("• Always validate YAML syntax before deployment")
        print("• YAML is more readable than JSON for configuration files")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()