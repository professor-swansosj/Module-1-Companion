"""
Import Examples - Network Automation

This script demonstrates different import styles and best practices
for organizing and importing Python modules.
"""

# Standard library imports (grouped at top)
import os
import sys
import json
from datetime import datetime
from typing import List, Dict

# Add current directory to path for custom modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Third-party imports would go here
# import requests
# import paramiko

# Local/custom imports (grouped at bottom)
import network_utils
from network_utils import configure_interface
from network_utils.device_config import configure_vlan
from network_utils.network_devices import Router, Switch


def demonstrate_import_styles():
    """Demonstrate different ways to import modules and functions."""
    print("=== Python Import Styles Demo ===\n")
    
    # Style 1: Import entire module
    print("1. Import entire module:")
    print(f"Using network_utils module version: {network_utils.__version__}")
    
    # Access functions through module name
    result = network_utils.configure_interface("router-01", "eth0", "10.0.1.1", "255.255.255.0")
    print(f"Configuration result: {result}\n")
    
    # Style 2: Import specific functions
    print("2. Import specific functions (already imported above):")
    configure_interface("router-02", "eth1", "10.0.2.1", "255.255.255.0", "Management Interface")
    print()
    
    # Style 3: Import with alias
    print("3. Import with alias:")
    import network_utils.device_config as dev_config
    dev_config.configure_vlan("switch-01", 100, "Management", ["port1", "port2"])
    print()
    
    # Style 4: Import from submodule
    print("4. Import from submodule:")
    configure_vlan("switch-02", 200, "Data", ["port3", "port4", "port5"])
    print()
    
    # Style 5: Import classes
    print("5. Import and use classes:")
    router = Router("edge-router", "10.0.0.1", "Cisco")
    switch = Switch("core-switch", "10.0.0.2", "Cisco")
    
    print(f"Created: {router}")
    print(f"Created: {switch}")
    print()


def demonstrate_import_best_practices():
    """Show best practices for imports."""
    print("=== Import Best Practices ===\n")
    
    print("✓ DO: Group imports by category (standard, third-party, local)")
    print("✓ DO: Put imports at the top of the file")
    print("✓ DO: Use absolute imports when possible")
    print("✓ DO: Import only what you need")
    print("✓ DO: Use meaningful aliases for long module names")
    print()
    
    print("✗ DON'T: Use wildcard imports (from module import *)")
    print("✗ DON'T: Import inside functions (except when necessary)")
    print("✗ DON'T: Use relative imports for external packages")
    print("✗ DON'T: Import unused modules")
    print()
    
    # Good example: Specific imports with clear naming
    from network_utils.network_devices import create_network_topology
    
    devices = create_network_topology()
    print(f"Created topology with {len(devices)} devices using specific import")
    
    # Show the difference between import styles
    print("\n--- Import Style Comparison ---")
    
    # Style A: Import everything (not recommended for large modules)
    # from network_utils import *  # DON'T DO THIS
    
    # Style B: Import module and use dot notation
    print("Style B - Module dot notation:")
    print(f"  network_utils.__version__ = {network_utils.__version__}")
    
    # Style C: Import specific items (recommended)
    from network_utils.device_config import generate_config_template
    print("Style C - Specific import:")
    template = generate_config_template("switch", "test-switch")
    print(f"  Generated template ({len(template)} characters)")


def demonstrate_conditional_imports():
    """Show conditional imports for optional functionality."""
    print("\n=== Conditional Imports ===\n")
    
    # Try importing optional modules
    try:
        import json
        print("✓ JSON module available")
        json_available = True
        json_module = json
    except ImportError:
        print("✗ JSON module not available")
        json_available = False
        json_module = None
    
    # Use the module if available
    if json_available and json_module:
        sample_data = {
            "device": "router-01",
            "interfaces": ["eth0", "eth1"],
            "vlans": [10, 20, 30]
        }
        json_string = json_module.dumps(sample_data, indent=2)
        print("Sample JSON data:")
        print(json_string)
    
    # Example of importing different modules based on conditions
    print("\nConditional import example:")
    try:
        # Try to import a hypothetical advanced module
        # import advanced_network_tools  # This doesn't exist
        print("✓ Advanced tools available")
        use_advanced = True
    except ImportError:
        print("✗ Advanced tools not available, using basic functions")
        use_advanced = False
    
    if use_advanced:
        print("Using advanced network analysis...")
    else:
        print("Using basic network configuration...")


def demonstrate_import_errors():
    """Demonstrate common import errors and how to handle them."""
    print("\n=== Import Error Handling ===\n")
    
    # Example 1: Missing module
    try:
        import non_existent_module
    except ImportError as e:
        print(f"ImportError caught: {e}")
    
    # Example 2: Wrong module path
    import importlib.util
    spec = importlib.util.find_spec("network_utils.wrong_module")
    if spec is None:
        print("Module path error: No module named 'network_utils.wrong_module'")
    else:
        print("Module found (this shouldn't happen in this example)")
    
    # Example 3: Circular import (simulated)
    print("Circular import prevention:")
    print("- Use 'import module' instead of 'from module import item'")
    print("- Move shared code to a separate module")
    print("- Use imports inside functions when necessary")
    
    # Example 4: Graceful fallback
    try:
        # This import is intentionally designed to fail for demonstration
        import importlib.util
        spec = importlib.util.find_spec("network_utils.advanced_features")
        if spec is None:
            raise ImportError("Module not found")
        # Import would go here if module existed
        # from network_utils.advanced_features import advanced_function
        print("✓ Advanced features loaded")
        
        def process_network_data():
            """Advanced implementation."""
            return "Advanced implementation"
    except ImportError:
        print("ℹ Advanced features not available, using standard functions")
        
        def process_network_data():
            """Fallback implementation."""
            return "Basic implementation"


def create_sample_config_file():
    """Create a sample configuration file to demonstrate file imports."""
    config = {
        "network": {
            "routers": [
                {"hostname": "R1", "ip": "10.0.1.1", "vendor": "Cisco"},
                {"hostname": "R2", "ip": "10.0.1.2", "vendor": "Juniper"}
            ],
            "switches": [
                {"hostname": "SW1", "ip": "10.0.1.10", "vendor": "Cisco"},
                {"hostname": "SW2", "ip": "10.0.1.11", "vendor": "Cisco"}
            ]
        },
        "vlans": [
            {"id": 10, "name": "Data"},
            {"id": 20, "name": "Voice"},
            {"id": 99, "name": "Management"}
        ]
    }
    
    # Write to file
    with open("sample_network_config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    
    print("Created sample_network_config.json")
    return "sample_network_config.json"


def load_and_use_config():
    """Load configuration from file and use imported modules."""
    config_file = create_sample_config_file()
    
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        print(f"\nLoaded configuration from {config_file}")
        
        # Use imported classes to create devices from config
        devices = []
        
        # Create routers from config
        for router_config in config["network"]["routers"]:
            router = Router(
                router_config["hostname"],
                router_config["ip"],
                router_config["vendor"]
            )
            devices.append(router)
        
        # Create switches from config
        for switch_config in config["network"]["switches"]:
            switch = Switch(
                switch_config["hostname"],
                switch_config["ip"],
                switch_config["vendor"]
            )
            devices.append(switch)
        
        print("Created devices from configuration:")
        for device in devices:
            print(f"  {device}")
        
        # Clean up
        os.remove(config_file)
        print(f"Cleaned up {config_file}")
        
    except Exception as e:
        print(f"Error loading config: {e}")


if __name__ == "__main__":
    demonstrate_import_styles()
    demonstrate_import_best_practices() 
    demonstrate_conditional_imports()
    demonstrate_import_errors()
    load_and_use_config()
    
    print("\n=== Import Examples Complete ===")
    print("\nRemember:")
    print("• Keep imports organized and clean")
    print("• Import only what you need")
    print("• Handle import errors gracefully")
    print("• Use meaningful names and aliases")
    print("• Follow PEP 8 import guidelines")