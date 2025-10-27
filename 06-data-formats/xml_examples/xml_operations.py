"""
XML Operations - Network Automation

This module demonstrates working with XML (eXtensible Markup Language) for
network automation. XML is commonly used in NETCONF, YANG models, and
network device APIs for configuration and monitoring.

Uses Python's built-in xml.etree.ElementTree module for parsing and creating XML.
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from datetime import datetime


def create_sample_xml_files():
    """Create sample XML files for demonstration."""
    print("=== Creating Sample XML Files ===\n")
    
    # Network device configuration XML
    device_config_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Network Device Configuration -->
<network-config xmlns="http://example.com/network-config">
    <metadata>
        <created-date>2024-10-26T10:00:00Z</created-date>
        <created-by>Network Team</created-by>
        <version>1.0</version>
    </metadata>
    
    <devices>
        <device id="router-01">
            <hostname>core-router-01</hostname>
            <vendor>Cisco</vendor>
            <model>ISR 4331</model>
            <ip-address>10.0.0.1</ip-address>
            <management-ip>192.168.100.1</management-ip>
            <location>Data Center</location>
            <status enabled="true">active</status>
            
            <interfaces>
                <interface name="GigabitEthernet0/0">
                    <description>WAN Interface to ISP</description>
                    <ip-address>203.0.113.10</ip-address>
                    <subnet-mask>255.255.255.252</subnet-mask>
                    <status>up</status>
                    <speed>1000</speed>
                    <duplex>full</duplex>
                </interface>
                <interface name="GigabitEthernet0/1">
                    <description>LAN Interface to Core Switch</description>
                    <ip-address>192.168.1.1</ip-address>
                    <subnet-mask>255.255.255.0</subnet-mask>
                    <status>up</status>
                    <speed>1000</speed>
                    <duplex>full</duplex>
                </interface>
            </interfaces>
            
            <routing>
                <ospf process-id="1">
                    <router-id>1.1.1.1</router-id>
                    <networks>
                        <network address="192.168.1.0" wildcard="0.0.0.255" area="0"/>
                        <network address="203.0.113.8" wildcard="0.0.0.3" area="0"/>
                    </networks>
                </ospf>
                <static-routes>
                    <route destination="0.0.0.0/0" next-hop="203.0.113.9" metric="1"/>
                </static-routes>
            </routing>
        </device>
        
        <device id="switch-01">
            <hostname>access-switch-01</hostname>
            <vendor>Cisco</vendor>
            <model>Catalyst 2960X</model>
            <ip-address>10.0.0.10</ip-address>
            <management-ip>192.168.100.10</management-ip>
            <location>Data Center</location>
            <status enabled="true">active</status>
            
            <vlans>
                <vlan id="1" name="default"/>
                <vlan id="10" name="Data"/>
                <vlan id="20" name="Voice"/>
                <vlan id="30" name="Guest"/>
                <vlan id="99" name="Management"/>
            </vlans>
            
            <interfaces>
                <interface name="FastEthernet0/1">
                    <description>Workstation Port</description>
                    <mode>access</mode>
                    <vlan>10</vlan>
                    <status>up</status>
                </interface>
                <interface name="FastEthernet0/24">
                    <description>Phone Port</description>
                    <mode>access</mode>
                    <vlan>20</vlan>
                    <voice-vlan>20</voice-vlan>
                    <status>up</status>
                </interface>
                <interface name="GigabitEthernet0/1">
                    <description>Trunk to Core Router</description>
                    <mode>trunk</mode>
                    <allowed-vlans>1,10,20,30,99</allowed-vlans>
                    <status>up</status>
                </interface>
            </interfaces>
        </device>
    </devices>
    
    <global-settings>
        <dns-servers>
            <server primary="true">8.8.8.8</server>
            <server primary="false">8.8.4.4</server>
        </dns-servers>
        <ntp-servers>
            <server>0.pool.ntp.org</server>
            <server>1.pool.ntp.org</server>
        </ntp-servers>
        <snmp>
            <community name="public" access="read-only"/>
            <community name="private" access="read-write"/>
        </snmp>
    </global-settings>
</network-config>'''

    # NETCONF response XML (typical from network devices)
    netconf_response_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
    <data>
        <interfaces xmlns="http://example.com/schema/interfaces">
            <interface>
                <name>GigabitEthernet0/0</name>
                <type>ethernet</type>
                <enabled>true</enabled>
                <ipv4>
                    <address>
                        <ip>203.0.113.10</ip>
                        <netmask>255.255.255.252</netmask>
                    </address>
                </ipv4>
                <statistics>
                    <rx-packets>12458963</rx-packets>
                    <tx-packets>11567842</tx-packets>
                    <rx-bytes>8734521045</rx-bytes>
                    <tx-bytes>7625981234</tx-bytes>
                    <rx-errors>0</rx-errors>
                    <tx-errors>0</tx-errors>
                </statistics>
            </interface>
            <interface>
                <name>GigabitEthernet0/1</name>
                <type>ethernet</type>
                <enabled>true</enabled>
                <ipv4>
                    <address>
                        <ip>192.168.1.1</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
                <statistics>
                    <rx-packets>45678912</rx-packets>
                    <tx-packets>43256789</tx-packets>
                    <rx-bytes>32145687900</rx-bytes>
                    <tx-bytes>29876543210</tx-bytes>
                    <rx-errors>2</rx-errors>
                    <tx-errors>1</tx-errors>
                </statistics>
            </interface>
        </interfaces>
        
        <routing-table xmlns="http://example.com/schema/routing">
            <route>
                <destination>0.0.0.0/0</destination>
                <next-hop>203.0.113.9</next-hop>
                <interface>GigabitEthernet0/0</interface>
                <metric>1</metric>
                <protocol>static</protocol>
            </route>
            <route>
                <destination>192.168.1.0/24</destination>
                <next-hop>0.0.0.0</next-hop>
                <interface>GigabitEthernet0/1</interface>
                <metric>0</metric>
                <protocol>connected</protocol>
            </route>
            <route>
                <destination>203.0.113.8/30</destination>
                <next-hop>0.0.0.0</next-hop>
                <interface>GigabitEthernet0/0</interface>
                <metric>0</metric>
                <protocol>connected</protocol>
            </route>
        </routing-table>
    </data>
</rpc-reply>'''

    # Network topology XML
    topology_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<network-topology xmlns="http://example.com/network-topology">
    <topology id="main-topology">
        <name>Corporate Network Topology</name>
        <description>Main office and branch office connectivity</description>
        
        <nodes>
            <node id="ISP-ROUTER">
                <name>ISP Gateway Router</name>
                <type>external</type>
                <location external="true"/>
            </node>
            
            <node id="CORE-RTR-01">
                <name>core-router-01</name>
                <type>router</type>
                <vendor>Cisco</vendor>
                <model>ISR 4331</model>
                <management-ip>192.168.100.1</management-ip>
                <location>
                    <building>Data Center</building>
                    <floor>1</floor>
                    <rack>A1</rack>
                </location>
            </node>
            
            <node id="CORE-SW-01">
                <name>core-switch-01</name>
                <type>switch</type>
                <vendor>Cisco</vendor>
                <model>Catalyst 3850</model>
                <management-ip>192.168.100.11</management-ip>
                <location>
                    <building>Data Center</building>
                    <floor>1</floor>
                    <rack>A1</rack>
                </location>
            </node>
            
            <node id="ACCESS-SW-01">
                <name>access-switch-01</name>
                <type>switch</type>
                <vendor>Cisco</vendor>
                <model>Catalyst 2960X</model>
                <management-ip>192.168.100.10</management-ip>
                <location>
                    <building>Office Building</building>
                    <floor>2</floor>
                    <closet>IDF-1</closet>
                </location>
            </node>
            
            <node id="FIREWALL-01">
                <name>perimeter-firewall</name>
                <type>firewall</type>
                <vendor>Fortinet</vendor>
                <model>FortiGate 200F</model>
                <management-ip>192.168.100.100</management-ip>
                <location>
                    <building>Data Center</building>
                    <floor>1</floor>
                    <rack>A2</rack>
                </location>
            </node>
        </nodes>
        
        <links>
            <link id="link-1">
                <source node="ISP-ROUTER" interface="unknown"/>
                <target node="CORE-RTR-01" interface="GigabitEthernet0/0"/>
                <type>wan</type>
                <bandwidth>100Mbps</bandwidth>
                <cost>10</cost>
            </link>
            
            <link id="link-2">
                <source node="CORE-RTR-01" interface="GigabitEthernet0/1"/>
                <target node="CORE-SW-01" interface="GigabitEthernet1/0/1"/>
                <type>lan</type>
                <bandwidth>1Gbps</bandwidth>
                <cost>1</cost>
            </link>
            
            <link id="link-3">
                <source node="CORE-SW-01" interface="GigabitEthernet1/0/2"/>
                <target node="ACCESS-SW-01" interface="GigabitEthernet0/1"/>
                <type>lan</type>
                <bandwidth>1Gbps</bandwidth>
                <cost>1</cost>
            </link>
            
            <link id="link-4">
                <source node="CORE-RTR-01" interface="GigabitEthernet0/2"/>
                <target node="FIREWALL-01" interface="port1"/>
                <type>dmz</type>
                <bandwidth>1Gbps</bandwidth>
                <cost>1</cost>
            </link>
        </links>
        
        <subnets>
            <subnet id="wan-subnet">
                <network>203.0.113.8/30</network>
                <description>WAN connection to ISP</description>
                <vlan>none</vlan>
            </subnet>
            
            <subnet id="lan-subnet">
                <network>192.168.1.0/24</network>
                <description>Main LAN network</description>
                <vlan>1</vlan>
                <gateway>192.168.1.1</gateway>
            </subnet>
            
            <subnet id="data-subnet">
                <network>192.168.10.0/24</network>
                <description>User data network</description>
                <vlan>10</vlan>
                <gateway>192.168.10.1</gateway>
            </subnet>
            
            <subnet id="voice-subnet">
                <network>192.168.20.0/24</network>
                <description>VoIP network</description>
                <vlan>20</vlan>
                <gateway>192.168.20.1</gateway>
            </subnet>
            
            <subnet id="management-subnet">
                <network>192.168.100.0/24</network>
                <description>Management network</description>
                <vlan>99</vlan>
                <gateway>192.168.100.1</gateway>
            </subnet>
        </subnets>
    </topology>
</network-topology>'''
    
    files_created = []
    
    # Write the XML files
    xml_files = [
        ("device_config.xml", device_config_xml),
        ("netconf_response.xml", netconf_response_xml),
        ("network_topology.xml", topology_xml)
    ]
    
    for filename, content in xml_files:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"✓ Created {filename}")
            files_created.append(filename)
        except Exception as e:
            print(f"✗ Failed to create {filename}: {e}")
    
    return files_created


def parse_xml_file(filename):
    """Parse XML file and display structure."""
    print(f"\n=== Parsing XML File: {filename} ===\n")
    
    if not os.path.exists(filename):
        print(f"✗ File {filename} not found")
        return None
    
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        print(f"Root element: {root.tag}")
        if root.attrib:
            print(f"Root attributes: {root.attrib}")
        
        # Display namespace information
        if root.tag.startswith('{'):
            namespace_end = root.tag.find('}')
            namespace = root.tag[1:namespace_end]
            local_name = root.tag[namespace_end + 1:]
            print(f"Namespace: {namespace}")
            print(f"Local name: {local_name}")
        
        print("\nTree structure:")
        print_xml_structure(root, 0)
        
        return tree
    
    except ET.ParseError as e:
        print(f"✗ XML Parse Error: {e}")
        return None
    except Exception as e:
        print(f"✗ Error parsing {filename}: {e}")
        return None


def print_xml_structure(element, level, max_level=3):
    """Recursively print XML structure with limited depth."""
    if level > max_level:
        return
    
    indent = "  " * level
    tag_name = element.tag
    
    # Clean up namespace in tag name for display
    if '}' in tag_name:
        tag_name = tag_name.split('}')[1]
    
    # Display element info
    text_content = element.text.strip() if element.text else ""
    if text_content and len(text_content) > 50:
        text_content = text_content[:47] + "..."
    
    print(f"{indent}<{tag_name}>", end="")
    
    if element.attrib:
        attrs = ", ".join([f"{k}={v}" for k, v in element.attrib.items()])
        print(f" [{attrs}]", end="")
    
    if text_content:
        print(f" '{text_content}'", end="")
    
    print()
    
    # Show child elements
    children = list(element)
    if children:
        child_counts = {}
        for child in children:
            child_tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
            child_counts[child_tag] = child_counts.get(child_tag, 0) + 1
        
        for child in children[:5]:  # Limit to first 5 children
            print_xml_structure(child, level + 1, max_level)
        
        if len(children) > 5:
            print(f"{indent}  ... and {len(children) - 5} more elements")


def extract_device_info(xml_file):
    """Extract specific device information from XML."""
    print(f"\n=== Extracting Device Information from {xml_file} ===\n")
    
    if not os.path.exists(xml_file):
        print(f"✗ File {xml_file} not found")
        return
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Handle namespace if present
        namespace = ""
        if root.tag.startswith('{'):
            namespace_end = root.tag.find('}')
            namespace = root.tag[1:namespace_end]
        
        # Find all devices
        if namespace:
            devices = root.findall(f".//{{{namespace}}}device")
        else:
            devices = root.findall(".//device")
        
        print(f"Found {len(devices)} devices:")
        
        for i, device in enumerate(devices, 1):
            device_id = device.get('id', f'device-{i}')
            print(f"\n--- Device {i}: {device_id} ---")
            
            # Extract basic info
            hostname_elem = device.find('.//hostname')
            vendor_elem = device.find('.//vendor')
            model_elem = device.find('.//model')
            ip_elem = device.find('.//ip-address')
            
            if hostname_elem is not None:
                print(f"  Hostname: {hostname_elem.text}")
            if vendor_elem is not None:
                print(f"  Vendor: {vendor_elem.text}")
            if model_elem is not None:
                print(f"  Model: {model_elem.text}")
            if ip_elem is not None:
                print(f"  IP Address: {ip_elem.text}")
            
            # Extract interface information
            interfaces = device.findall('.//interface')
            if interfaces:
                print(f"  Interfaces ({len(interfaces)}):")
                for interface in interfaces[:3]:  # Show first 3
                    name = interface.get('name', interface.find('name'))
                    if hasattr(name, 'text'):
                        name = name.text
                    description = interface.find('description')
                    status = interface.find('status')
                    
                    print(f"    - {name}", end="")
                    if description is not None:
                        print(f" ({description.text})", end="")
                    if status is not None:
                        print(f" [{status.text}]", end="")
                    print()
                
                if len(interfaces) > 3:
                    print(f"    ... and {len(interfaces) - 3} more interfaces")
    
    except Exception as e:
        print(f"✗ Error extracting device info: {e}")


def analyze_netconf_response(xml_file):
    """Analyze NETCONF response XML."""
    print(f"\n=== Analyzing NETCONF Response: {xml_file} ===\n")
    
    if not os.path.exists(xml_file):
        print(f"✗ File {xml_file} not found")
        return
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Check if this is a NETCONF RPC reply
        if 'rpc-reply' in root.tag:
            print("✓ Valid NETCONF RPC Reply detected")
            message_id = root.get('message-id')
            if message_id:
                print(f"  Message ID: {message_id}")
        
        # Find interface statistics
        interfaces = root.findall('.//interface')
        print(f"\nInterface Statistics ({len(interfaces)} interfaces):")
        
        for interface in interfaces:
            name_elem = interface.find('.//name')
            if name_elem is not None:
                name = name_elem.text
                print(f"\n  Interface: {name}")
                
                # Get statistics
                stats = interface.find('.//statistics')
                if stats is not None:
                    rx_packets = stats.find('rx-packets')
                    tx_packets = stats.find('tx-packets')
                    rx_bytes = stats.find('rx-bytes')
                    tx_bytes = stats.find('tx-bytes')
                    rx_errors = stats.find('rx-errors')
                    tx_errors = stats.find('tx-errors')
                    
                    if rx_packets is not None:
                        print(f"    RX Packets: {int(rx_packets.text):,}")
                    if tx_packets is not None:
                        print(f"    TX Packets: {int(tx_packets.text):,}")
                    if rx_bytes is not None:
                        print(f"    RX Bytes: {int(rx_bytes.text):,}")
                    if tx_bytes is not None:
                        print(f"    TX Bytes: {int(tx_bytes.text):,}")
                    if rx_errors is not None and tx_errors is not None:
                        print(f"    Errors: RX={rx_errors.text}, TX={tx_errors.text}")
        
        # Analyze routing table
        routes = root.findall('.//route')
        if routes:
            print(f"\nRouting Table ({len(routes)} routes):")
            for route in routes:
                dest = route.find('destination')
                next_hop = route.find('next-hop')
                protocol = route.find('protocol')
                metric = route.find('metric')
                
                route_info = []
                if dest is not None:
                    route_info.append(f"Dest: {dest.text}")
                if next_hop is not None:
                    route_info.append(f"Next-hop: {next_hop.text}")
                if protocol is not None:
                    route_info.append(f"Protocol: {protocol.text}")
                if metric is not None:
                    route_info.append(f"Metric: {metric.text}")
                
                print(f"  - {' | '.join(route_info)}")
    
    except Exception as e:
        print(f"✗ Error analyzing NETCONF response: {e}")


def create_xml_from_python_data():
    """Create XML from Python data structures."""
    print("\n=== Creating XML from Python Data ===\n")
    
    # Network monitoring data
    monitoring_data = {
        "timestamp": datetime.now().isoformat(),
        "devices": [
            {
                "hostname": "router-01",
                "ip": "10.0.0.1",
                "status": "up",
                "uptime": 86400,
                "cpu_usage": 15.7,
                "memory_usage": 42.3,
                "interfaces": [
                    {"name": "Gi0/0", "status": "up", "utilization": 25.4},
                    {"name": "Gi0/1", "status": "up", "utilization": 78.2}
                ]
            },
            {
                "hostname": "switch-01",
                "ip": "10.0.0.10",
                "status": "up",
                "uptime": 172800,
                "cpu_usage": 8.3,
                "memory_usage": 31.7,
                "interfaces": [
                    {"name": "Fa0/1", "status": "up", "utilization": 12.1},
                    {"name": "Fa0/24", "status": "down", "utilization": 0.0}
                ]
            }
        ]
    }
    
    try:
        # Create root element
        root = ET.Element("network-monitoring")
        root.set("xmlns", "http://example.com/monitoring")
        
        # Add metadata
        metadata = ET.SubElement(root, "metadata")
        timestamp = ET.SubElement(metadata, "timestamp")
        timestamp.text = monitoring_data["timestamp"]
        
        generated_by = ET.SubElement(metadata, "generated-by")
        generated_by.text = "Python XML Generator"
        
        # Add devices
        devices_elem = ET.SubElement(root, "devices")
        
        for device_data in monitoring_data["devices"]:
            device = ET.SubElement(devices_elem, "device")
            device.set("id", device_data["hostname"])
            
            # Add device properties
            hostname = ET.SubElement(device, "hostname")
            hostname.text = device_data["hostname"]
            
            ip_address = ET.SubElement(device, "ip-address")
            ip_address.text = device_data["ip"]
            
            status = ET.SubElement(device, "status")
            status.text = device_data["status"]
            
            # Add performance metrics
            metrics = ET.SubElement(device, "metrics")
            
            uptime = ET.SubElement(metrics, "uptime")
            uptime.text = str(device_data["uptime"])
            uptime.set("unit", "seconds")
            
            cpu = ET.SubElement(metrics, "cpu-usage")
            cpu.text = str(device_data["cpu_usage"])
            cpu.set("unit", "percent")
            
            memory = ET.SubElement(metrics, "memory-usage")
            memory.text = str(device_data["memory_usage"])
            memory.set("unit", "percent")
            
            # Add interfaces
            interfaces_elem = ET.SubElement(device, "interfaces")
            
            for intf_data in device_data["interfaces"]:
                interface = ET.SubElement(interfaces_elem, "interface")
                interface.set("name", intf_data["name"])
                
                intf_status = ET.SubElement(interface, "status")
                intf_status.text = intf_data["status"]
                
                utilization = ET.SubElement(interface, "utilization")
                utilization.text = str(intf_data["utilization"])
                utilization.set("unit", "percent")
        
        # Pretty print the XML
        xml_string = ET.tostring(root, encoding='unicode')
        parsed = minidom.parseString(xml_string)
        pretty_xml = parsed.toprettyxml(indent="  ")
        
        # Remove empty lines
        lines = [line for line in pretty_xml.split('\n') if line.strip()]
        pretty_xml = '\n'.join(lines)
        
        # Save to file
        output_file = "network_monitoring.xml"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(pretty_xml)
        
        print(f"✓ Generated network monitoring XML: {output_file}")
        print("Sample content:")
        print(pretty_xml[:600] + "..." if len(pretty_xml) > 600 else pretty_xml)
        
        return [output_file]
    
    except Exception as e:
        print(f"✗ XML generation failed: {e}")
        return []


def search_xml_elements(xml_file, search_term):
    """Search for specific elements or text in XML."""
    print(f"\n=== Searching XML for '{search_term}' in {xml_file} ===\n")
    
    if not os.path.exists(xml_file):
        print(f"✗ File {xml_file} not found")
        return
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        results = []
        
        def search_recursive(element, path=""):
            current_path = f"{path}/{element.tag.split('}')[-1]}" if path else element.tag.split('}')[-1]
            
            # Search in tag name
            if search_term.lower() in element.tag.lower():
                results.append(f"Tag match: {current_path}")
            
            # Search in text content
            if element.text and search_term.lower() in element.text.lower():
                results.append(f"Text match: {current_path} = '{element.text.strip()}'")
            
            # Search in attributes
            for attr_name, attr_value in element.attrib.items():
                if search_term.lower() in attr_name.lower() or search_term.lower() in attr_value.lower():
                    results.append(f"Attribute match: {current_path}@{attr_name} = '{attr_value}'")
            
            # Recursively search children
            for child in element:
                search_recursive(child, current_path)
        
        search_recursive(root)
        
        if results:
            print(f"Found {len(results)} matches:")
            for i, result in enumerate(results[:10], 1):  # Show first 10 matches
                print(f"  {i}. {result}")
            if len(results) > 10:
                print(f"  ... and {len(results) - 10} more matches")
        else:
            print(f"No matches found for '{search_term}'")
    
    except Exception as e:
        print(f"✗ Search failed: {e}")


def validate_xml_structure(xml_file):
    """Validate XML structure and provide analysis."""
    print(f"\n=== Validating XML Structure: {xml_file} ===\n")
    
    if not os.path.exists(xml_file):
        print(f"✗ File {xml_file} not found")
        return
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        print("✓ XML is well-formed")
        
        # Count elements
        all_elements = root.findall('.//*')
        element_counts = {}
        for elem in all_elements:
            tag_name = elem.tag.split('}')[-1]  # Remove namespace
            element_counts[tag_name] = element_counts.get(tag_name, 0) + 1
        
        print(f"\nStructure Analysis:")
        print(f"  Total elements: {len(all_elements) + 1}")  # +1 for root
        print(f"  Unique element types: {len(element_counts)}")
        
        # Check for namespaces
        if root.tag.startswith('{'):
            namespace_end = root.tag.find('}')
            namespace = root.tag[1:namespace_end]
            print(f"  Default namespace: {namespace}")
        
        # Show element distribution
        print("\nElement distribution:")
        for tag, count in sorted(element_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {tag}: {count} occurrences")
        
        # Check for common issues
        print("\nValidation checks:")
        
        # Check for empty elements
        empty_elements = [elem for elem in all_elements if not elem.text and not elem.attrib and not list(elem)]
        if empty_elements:
            print(f"  ⚠ Found {len(empty_elements)} empty elements")
        else:
            print("  ✓ No empty elements found")
        
        # Check for very long text content
        long_text_elements = [elem for elem in all_elements if elem.text and len(elem.text.strip()) > 500]
        if long_text_elements:
            print(f"  ⚠ Found {len(long_text_elements)} elements with very long text content")
        else:
            print("  ✓ No excessively long text content")
        
        # Check depth
        def get_depth(element, current_depth=0):
            if not list(element):
                return current_depth
            return max(get_depth(child, current_depth + 1) for child in element)
        
        max_depth = get_depth(root)
        print(f"  Maximum nesting depth: {max_depth}")
        if max_depth > 10:
            print("  ⚠ Very deep nesting detected (>10 levels)")
        
    except ET.ParseError as e:
        print(f"✗ XML Parse Error: {e}")
        print("  The XML file is not well-formed")
    except Exception as e:
        print(f"✗ Validation failed: {e}")


def cleanup_xml_files(*file_lists):
    """Clean up XML demonstration files."""
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
        print("XML Operations for Network Automation")
        print("=" * 42)
        
        # Create sample XML files
        xml_files = create_sample_xml_files()
        
        # Parse and analyze XML files
        for xml_file in xml_files:
            parse_xml_file(xml_file)
            validate_xml_structure(xml_file)
            
            if xml_file == "device_config.xml":
                extract_device_info(xml_file)
            elif xml_file == "netconf_response.xml":
                analyze_netconf_response(xml_file)
            
            # Search example
            if xml_file == "device_config.xml":
                search_xml_elements(xml_file, "interface")
        
        # Generate XML from Python data
        generated_files = create_xml_from_python_data()
        
        print("\n" + "="*50)
        response = input("Clean up demonstration files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_xml_files(xml_files, generated_files)
        
        print("\n=== XML Operations Demo Complete ===")
        print("\nKey takeaways:")
        print("• XML is hierarchical and self-describing")
        print("• Namespaces prevent element name conflicts")
        print("• NETCONF uses XML for network device communication")
        print("• ElementTree provides powerful XML parsing capabilities")
        print("• Always validate XML structure before processing")
        print("• Use XPath expressions for complex element selection")
        print("• XML is verbose but very structured and standardized")
        print("• Common in SOAP APIs and configuration files")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()