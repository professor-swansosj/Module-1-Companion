"""
🎯 XML Practice - Master Legacy System Data!

Your mission: Learn to work with XML, the structured format used by enterprise network 
management systems, SOAP APIs, and configuration backups!

🔥 What makes this exciting?
- XML handles complex structured data perfectly
- Many enterprise network systems still use XML
- Essential for SOAP APIs and legacy integrations
- Great for configuration backups and exports

📚 Study the main README first to understand XML basics!

💡 Pro Tip: XML uses tags with angle brackets - think of it like HTML for data!

✅ Good news: XML support is built into Python - no extra installation needed!
"""

import xml.etree.ElementTree as ET

def read_network_xml():
    """
    TODO: Learn to read and parse XML files.
    
    This simulates reading data from enterprise network management systems 
    that export device information in XML format.
    """
    print("🔸 Reading XML network data:")
    
    try:
        # TODO: Parse the XML file using ET.parse()
        # Hint: tree = ET.parse("network.xml")
        # Then get the root: root = tree.getroot()
        
        tree = None  # TODO: Replace with ET.parse("network.xml")
        root = None  # TODO: Replace with tree.getroot()
        
        print("   ✅ Loaded XML data successfully!")
        
        # TODO: Get the site name from XML
        # Hint: Use root.find("site_name").text
        site_name = "Unknown"  # TODO: Replace with actual XML data
        print(f"   🏢 Site: {site_name}")
        
        return tree, root  # Return both for other functions
        
    except FileNotFoundError:
        print("   ❌ network.xml file not found!")
        return None, None
    except ET.ParseError as e:
        print(f"   ❌ Invalid XML format: {e}")
        return None, None
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None, None

def display_xml_devices(root):
    """
    TODO: Extract device information from XML structure.
    
    Enterprise scenario: Processing device exports from network management systems.
    """
    print("🔸 Network devices from XML:")
    
    if root is None:
        print("   ❌ No XML data available")
        return
    
    try:
        # TODO: Find the devices section
        # Hint: devices = root.find("devices")
        devices = None  # TODO: Replace this
        
        if devices is None:
            print("   ❌ No devices section found in XML")
            return
        
        # TODO: Loop through each device element
        # Hint: Use devices.findall("device") to get all device elements
        # For each device, extract: hostname, type, ip
        # Use device.find("hostname").text to get text content
        
        pass  # Replace with your XML parsing loop
        
    except Exception as e:
        print(f"   ❌ Error processing devices: {e}")

def display_xml_vlans(root):
    """
    TODO: Extract VLAN configuration from XML.
    
    Network scenario: Reading VLAN configs from XML backup files.
    """
    print("🔸 VLAN configuration from XML:")
    
    if root is None:
        print("   ❌ No XML data available")
        return
    
    try:
        # TODO: Find the VLANs section
        vlans = None  # TODO: Replace with root.find("vlans")
        
        if vlans is None:
            print("   ❌ No VLANs section found in XML")
            return
        
        # TODO: Loop through each VLAN element
        # For each VLAN:
        # - Get the ID from the attribute: vlan.get("id")
        # - Get name and description from child elements
        # Format: "🔗 VLAN 10: Sales - Sales Department"
        
        pass  # Replace with your VLAN parsing loop
        
    except Exception as e:
        print(f"   ❌ Error processing VLANs: {e}")

def add_xml_device(tree, root):
    """
    TODO: Add new device to XML structure and save.
    
    Management scenario: Adding new devices to XML configuration files.
    """
    print("🔸 Adding new device to XML:")
    
    if tree is None or root is None:
        print("   ❌ No XML data available")
        return
    
    try:
        # TODO: Find the devices section to add to
        devices = None  # TODO: Replace with root.find("devices")
        
        if devices is None:
            print("   ❌ No devices section found")
            return
        
        # TODO: Create a new device element
        # Hint: Use ET.SubElement(devices, "device") to create the device
        # Then add child elements for hostname, ip, type, location
        # Use ET.SubElement(device_element, "hostname").text = "server1"
        
        # Example device to add:
        # hostname: server1, ip: 192.168.1.5, type: server, location: datacenter
        
        pass  # Replace with your XML creation code
        
        # TODO: Save the updated XML file
        # Hint: Use tree.write("network_updated.xml", encoding="UTF-8", xml_declaration=True)
        
        print("   ✅ Added server and saved to network_updated.xml")
        
    except Exception as e:
        print(f"   ❌ Error adding device: {e}")

def show_xml_structure():
    """
    Show XML structure and explain the format.
    """
    print("📖 Understanding XML Structure:")
    print()
    print("<?xml version='1.0' encoding='UTF-8'?>")
    print("<network>")
    print("  <site_name>Main Office</site_name>")
    print("  <devices>")
    print("    <device>")
    print("      <hostname>router1</hostname>")
    print("      <ip>192.168.1.1</ip>")
    print("      <type>router</type>")
    print("    </device>")
    print("  </devices>")
    print("  <vlans>")
    print("    <vlan id='10'>")
    print("      <name>Sales</name>")
    print("      <description>Sales Department</description>")
    print("    </vlan>")
    print("  </vlans>")
    print("</network>")
    print()
    print("💡 Key XML Concepts:")
    print("   • Tags define structure: <hostname>router1</hostname>")
    print("   • Attributes store extra info: <vlan id='10'>")
    print("   • Must be well-formed (all tags properly closed)")
    print("   • Root element contains everything")

def xml_tips():
    """
    Display helpful tips for working with XML in network automation.
    """
    print("💡 XML Pro Tips:")
    print("   • Use ET.parse() for files, ET.fromstring() for strings")
    print("   • .find() gets first match, .findall() gets all matches")
    print("   • .text gets element content, .get() gets attributes")
    print("   • Always handle None when elements might not exist")
    print("   • XML is verbose but handles complex nested structures well")
    print("   • Perfect for enterprise systems and SOAP APIs")

def main():
    """
    Run all XML practice exercises step by step.
    """
    print("=== 🎯 XML Practice Challenge ===")
    print()
    print("Master XML - the enterprise structured data format!")
    print("=" * 50)
    print()
    
    # Step 1: Learn to read XML files
    tree, root = read_network_xml()
    print()
    
    # Step 2: Extract device information
    display_xml_devices(root)
    print()
    
    # Step 3: Extract VLAN configuration  
    display_xml_vlans(root)
    print()
    
    # Step 4: Modify and save XML
    add_xml_device(tree, root)
    print()
    
    # Educational: Show XML structure
    show_xml_structure()
    print()
    
    # Bonus: Tips for success
    xml_tips()
    print()
    
    print("🎉 XML Practice Complete!")
    print("🚀 Now you've mastered all four major data formats!")
    print("💪 Ready to tackle any network automation challenge!")

if __name__ == "__main__":
    main()