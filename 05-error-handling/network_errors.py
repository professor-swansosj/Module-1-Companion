"""
Network Error Handling - try...except Examples

This module demonstrates comprehensive error handling for common network automation
scenarios using try...except blocks. Network automation is prone to various errors
due to connectivity issues, device failures, configuration problems, and file system issues.
"""

import os
import socket
import json
import time
from datetime import datetime
import random


def demonstrate_basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    print("=== Basic Exception Handling ===\n")
    
    # Example 1: Basic try-except
    print("1. Basic try-except pattern:")
    try:
        result = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError:
        print("✓ Caught division by zero error")
    
    # Example 2: Multiple exception types
    print("\n2. Handling multiple exception types:")
    test_values = ["10", "abc", "5.5", ""]
    
    for value in test_values:
        try:
            number = int(value)
            result = 100 / number
            print(f"  {value} → {result}")
        except ValueError:
            print(f"  {value} → Invalid number format")
        except ZeroDivisionError:
            print(f"  {value} → Division by zero")
    
    # Example 3: Generic exception handling
    print("\n3. Generic exception with details:")
    try:
        # Simulate an unexpected error
        data = {"router": "192.168.1.1"}
        ip_address = data["switch"]  # Key doesn't exist
    except Exception as e:
        print(f"✓ Caught unexpected error: {type(e).__name__}: {e}")


def demonstrate_file_operation_errors():
    """Demonstrate file operation error handling."""
    print("\n=== File Operation Error Handling ===\n")
    
    # Example 1: File not found
    print("1. Handling file not found:")
    config_files = ["router1.cfg", "switch1.cfg", "nonexistent.cfg"]
    
    for config_file in config_files:
        try:
            with open(config_file, "r", encoding="utf-8") as file:
                content = file.read()
            print(f"  ✓ {config_file}: {len(content)} characters read")
        except FileNotFoundError:
            print(f"  ✗ {config_file}: File not found")
        except PermissionError:
            print(f"  ✗ {config_file}: Permission denied")
        except Exception as e:
            print(f"  ✗ {config_file}: Unexpected error - {e}")
    
    # Example 2: Creating files with error handling
    print("\n2. Safe file creation:")
    
    def safe_create_config(filename, content):
        """Safely create a configuration file with error handling."""
        try:
            # Check if directory exists
            directory = os.path.dirname(filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"  ✓ Created {filename}")
            return True
        except PermissionError:
            print(f"  ✗ Permission denied creating {filename}")
        except OSError as e:
            print(f"  ✗ OS error creating {filename}: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error creating {filename}: {e}")
        return False
    
    sample_config = "hostname TestRouter\ninterface GigE0/0\n no shutdown\n"
    test_files = ["router1.cfg", "configs/router2.cfg", "switch1.cfg"]
    
    for test_file in test_files:
        safe_create_config(test_file, sample_config)
    
    return test_files + ["configs"]


def simulate_network_connection_errors():
    """Simulate and handle network connection errors."""
    print("\n=== Network Connection Error Handling ===\n")
    
    def attempt_connection(host, port, timeout=3):
        """Attempt to connect to a network device."""
        try:
            print(f"  Attempting connection to {host}:{port}...")
            
            # Create socket and attempt connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            
            # This will likely fail for demo purposes
            result = sock.connect_ex((host, port))
            
            if result == 0:
                print(f"  ✓ Connected to {host}:{port}")
                sock.close()
                return True
            else:
                raise ConnectionRefusedError(f"Connection refused to {host}:{port}")
                
        except socket.timeout:
            print(f"  ✗ Connection timeout to {host}:{port}")
        except socket.gaierror as e:
            print(f"  ✗ DNS resolution failed for {host}: {e}")
        except ConnectionRefusedError as e:
            print(f"  ✗ {e}")
        except OSError as e:
            print(f"  ✗ Network error connecting to {host}:{port}: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected connection error: {e}")
        finally:
            try:
                sock.close()
            except:
                pass
        
        return False
    
    # Test connections to various devices
    devices = [
        ("192.168.1.1", 22),    # SSH
        ("192.168.1.1", 23),    # Telnet
        ("192.168.1.10", 161),  # SNMP
        ("invalid-host", 22),   # Invalid hostname
        ("8.8.8.8", 53)         # Google DNS (might work)
    ]
    
    print("Testing network connections:")
    for host, port in devices:
        attempt_connection(host, port)


def demonstrate_json_parsing_errors():
    """Demonstrate JSON parsing error handling."""
    print("\n=== JSON Parsing Error Handling ===\n")
    
    # Create various JSON test cases
    json_test_cases = [
        ('valid.json', '{"hostname": "router1", "ip": "192.168.1.1", "status": "online"}'),
        ('invalid_syntax.json', '{"hostname": "router2", "ip": "192.168.1.2" "status": "online"}'),  # Missing comma
        ('incomplete.json', '{"hostname": "router3", "ip": "192.168.1.3"'),  # Incomplete
        ('empty.json', ''),  # Empty file
        ('not_json.json', 'hostname router4\nip address 192.168.1.4')  # Not JSON format
    ]
    
    def safe_parse_json(filename):
        """Safely parse JSON file with comprehensive error handling."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            print(f"  ✓ {filename}: Successfully parsed JSON")
            return data
        except FileNotFoundError:
            print(f"  ✗ {filename}: File not found")
        except json.JSONDecodeError as e:
            print(f"  ✗ {filename}: Invalid JSON format - {e}")
        except Exception as e:
            print(f"  ✗ {filename}: Unexpected error - {e}")
        return None
    
    # Create test files
    for filename, content in json_test_cases:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            print(f"Failed to create {filename}: {e}")
    
    # Test parsing each file
    print("Testing JSON parsing:")
    results = []
    for filename, _ in json_test_cases:
        result = safe_parse_json(filename)
        results.append(filename)
    
    return results


def demonstrate_configuration_validation_errors():
    """Demonstrate configuration validation error handling."""
    print("\n=== Configuration Validation Error Handling ===\n")
    
    def validate_router_config(config_dict):
        """Validate router configuration with detailed error handling."""
        errors = []
        warnings = []
        
        try:
            # Check required fields
            required_fields = ["hostname", "interfaces", "routing"]
            for field in required_fields:
                if field not in config_dict:
                    errors.append(f"Missing required field: {field}")
            
            # Validate hostname
            if "hostname" in config_dict:
                hostname = config_dict["hostname"]
                if not isinstance(hostname, str) or len(hostname) < 3:
                    errors.append("Hostname must be a string with at least 3 characters")
                elif not hostname.replace("-", "").replace("_", "").isalnum():
                    warnings.append("Hostname contains special characters")
            
            # Validate interfaces
            if "interfaces" in config_dict:
                interfaces = config_dict["interfaces"]
                if not isinstance(interfaces, list):
                    errors.append("Interfaces must be a list")
                elif len(interfaces) == 0:
                    warnings.append("No interfaces configured")
                else:
                    for i, interface in enumerate(interfaces):
                        if not isinstance(interface, dict):
                            errors.append(f"Interface {i} must be a dictionary")
                            continue
                        
                        if "name" not in interface:
                            errors.append(f"Interface {i} missing name field")
                        
                        if "ip_address" in interface:
                            ip = interface["ip_address"]
                            # Simple IP validation
                            parts = ip.split(".")
                            if len(parts) != 4:
                                errors.append(f"Interface {i} has invalid IP format")
                            else:
                                try:
                                    for part in parts:
                                        num = int(part)
                                        if not 0 <= num <= 255:
                                            raise ValueError()
                                except ValueError:
                                    errors.append(f"Interface {i} has invalid IP address: {ip}")
            
            # Validate routing
            if "routing" in config_dict:
                routing = config_dict["routing"]
                if "protocols" in routing:
                    valid_protocols = ["OSPF", "BGP", "EIGRP", "RIP", "Static"]
                    for protocol in routing["protocols"]:
                        if protocol not in valid_protocols:
                            warnings.append(f"Unknown routing protocol: {protocol}")
            
        except Exception as e:
            errors.append(f"Validation error: {e}")
        
        return errors, warnings
    
    # Test configurations
    test_configs = [
        {
            "name": "Valid Config",
            "config": {
                "hostname": "router-01",
                "interfaces": [
                    {"name": "GigE0/0", "ip_address": "192.168.1.1", "subnet_mask": "255.255.255.0"},
                    {"name": "GigE0/1", "ip_address": "10.0.0.1", "subnet_mask": "255.255.255.252"}
                ],
                "routing": {
                    "protocols": ["OSPF", "BGP"]
                }
            }
        },
        {
            "name": "Missing Fields",
            "config": {
                "hostname": "router-02"
                # Missing interfaces and routing
            }
        },
        {
            "name": "Invalid IP",
            "config": {
                "hostname": "router-03",
                "interfaces": [
                    {"name": "GigE0/0", "ip_address": "192.168.1.999"}  # Invalid IP
                ],
                "routing": {"protocols": ["OSPF"]}
            }
        },
        {
            "name": "Invalid Structure",
            "config": {
                "hostname": "r",  # Too short
                "interfaces": "not_a_list",  # Should be list
                "routing": {"protocols": ["INVALID_PROTOCOL"]}
            }
        }
    ]
    
    print("Validating router configurations:")
    for test in test_configs:
        print(f"\n  Testing: {test['name']}")
        try:
            errors, warnings = validate_router_config(test['config'])
            
            if not errors and not warnings:
                print("    ✓ Configuration is valid")
            else:
                if errors:
                    print("    ✗ Errors found:")
                    for error in errors:
                        print(f"      - {error}")
                
                if warnings:
                    print("    ⚠ Warnings:")
                    for warning in warnings:
                        print(f"      - {warning}")
        
        except Exception as e:
            print(f"    ✗ Validation failed: {e}")


def demonstrate_retry_logic_with_errors():
    """Demonstrate retry logic for handling transient errors."""
    print("\n=== Retry Logic for Error Handling ===\n")
    
    def unreliable_network_operation(device_id, success_rate=0.3):
        """Simulate an unreliable network operation."""
        if random.random() < success_rate:
            return f"Successfully configured {device_id}"
        else:
            # Randomly choose different types of failures
            failure_types = [
                ConnectionError("Device unreachable"),
                TimeoutError("Operation timeout"),
                ValueError("Invalid configuration parameter"),
                RuntimeError("Device rejected configuration")
            ]
            raise random.choice(failure_types)
    
    def retry_operation(operation, max_attempts=3, delay=1):
        """Retry an operation with exponential backoff."""
        for attempt in range(1, max_attempts + 1):
            try:
                print(f"    Attempt {attempt}/{max_attempts}...")
                result = operation()
                print(f"    ✓ Success on attempt {attempt}")
                return result
            
            except ConnectionError as e:
                print(f"    ✗ Connection error: {e}")
                if attempt == max_attempts:
                    print(f"    ✗ Failed after {max_attempts} attempts - Connection issues")
                    raise
            
            except TimeoutError as e:
                print(f"    ⏱ Timeout error: {e}")
                if attempt == max_attempts:
                    print(f"    ✗ Failed after {max_attempts} attempts - Timeout")
                    raise
            
            except ValueError as e:
                print(f"    ✗ Configuration error: {e}")
                # Don't retry on configuration errors
                print("    ✗ Not retrying - configuration error")
                raise
            
            except Exception as e:
                print(f"    ✗ Unexpected error: {e}")
                if attempt == max_attempts:
                    print(f"    ✗ Failed after {max_attempts} attempts - Unexpected error")
                    raise
            
            # Wait before retry with exponential backoff
            if attempt < max_attempts:
                wait_time = delay * (2 ** (attempt - 1))
                print(f"    ⏳ Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    
    # Test retry logic on multiple devices
    devices = ["Router-01", "Switch-01", "Firewall-01", "AP-01"]
    
    print("Testing retry logic on network operations:")
    for device in devices:
        print(f"\n  Configuring {device}:")
        try:
            operation = lambda: unreliable_network_operation(device, success_rate=0.4)
            result = retry_operation(operation, max_attempts=3, delay=0.5)
            print(f"  ✓ {device}: {result}")
        except Exception as e:
            print(f"  ✗ {device}: Final failure - {e}")


def demonstrate_finally_and_cleanup():
    """Demonstrate finally blocks for cleanup operations."""
    print("\n=== Finally Blocks and Cleanup ===\n")
    
    def simulate_device_backup(device_name, should_fail=False):
        """Simulate device backup with cleanup."""
        temp_files = []
        connection = None
        
        try:
            print(f"  Starting backup for {device_name}...")
            
            # Simulate connection
            print(f"    Establishing connection to {device_name}...")
            connection = f"Connection_to_{device_name}"
            
            # Create temporary files
            temp_config = f"{device_name}_temp_config.tmp"
            temp_files.append(temp_config)
            
            with open(temp_config, "w", encoding="utf-8") as f:
                f.write(f"# Temporary backup for {device_name}\n")
                f.write("hostname " + device_name + "\n")
            
            print(f"    Created temporary file: {temp_config}")
            
            # Simulate failure if requested
            if should_fail:
                raise RuntimeError(f"Backup failed for {device_name}")
            
            # Simulate successful backup
            final_backup = f"{device_name}_backup.cfg"
            with open(final_backup, "w", encoding="utf-8") as f:
                f.write(f"# Backup for {device_name} - {datetime.now()}\n")
                f.write("hostname " + device_name + "\n")
                f.write("! Backup completed successfully\n")
            
            print(f"    ✓ Backup completed: {final_backup}")
            return final_backup
        
        except Exception as e:
            print(f"    ✗ Backup failed: {e}")
            raise
        
        finally:
            # Cleanup operations - always executed
            print(f"    🧹 Cleaning up resources for {device_name}...")
            
            # Close connection
            if connection:
                print(f"      Closing connection: {connection}")
            
            # Remove temporary files
            for temp_file in temp_files:
                try:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                        print(f"      Removed temporary file: {temp_file}")
                except Exception as cleanup_error:
                    print(f"      ✗ Failed to remove {temp_file}: {cleanup_error}")
    
    # Test backup operations
    test_devices = [
        ("Router-Success", False),
        ("Router-Failure", True),
        ("Switch-Success", False)
    ]
    
    created_files = []
    print("Testing backup operations with cleanup:")
    
    for device_name, should_fail in test_devices:
        print(f"\n  Testing {device_name}:")
        try:
            backup_file = simulate_device_backup(device_name, should_fail)
            created_files.append(backup_file)
        except Exception as e:
            print(f"  Final result: Backup failed for {device_name}")
    
    return created_files


def cleanup_demo_files(*file_lists):
    """Clean up all demonstration files."""
    print("\n=== Demo Cleanup ===\n")
    
    all_files = []
    for file_list in file_lists:
        if isinstance(file_list, list):
            all_files.extend(file_list)
        elif isinstance(file_list, str):
            all_files.append(file_list)
    
    # Add known demo files
    demo_files = [
        "router1.cfg", "switch1.cfg", "configs/router2.cfg",
        "valid.json", "invalid_syntax.json", "incomplete.json", 
        "empty.json", "not_json.json"
    ]
    all_files.extend(demo_files)
    
    for filename in all_files:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✓ Removed: {filename}")
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")
    
    # Clean up directories
    if os.path.exists("configs") and not os.listdir("configs"):
        try:
            os.rmdir("configs")
            print("✓ Removed empty configs directory")
        except Exception as e:
            print(f"✗ Failed to remove configs directory: {e}")


if __name__ == "__main__":
    try:
        print("Network Automation Error Handling Demonstration")
        print("=" * 50)
        
        demonstrate_basic_exception_handling()
        file_demo_files = demonstrate_file_operation_errors()
        simulate_network_connection_errors()
        json_demo_files = demonstrate_json_parsing_errors()
        demonstrate_configuration_validation_errors()
        demonstrate_retry_logic_with_errors()
        backup_demo_files = demonstrate_finally_and_cleanup()
        
        print("\n" + "="*50)
        response = input("Clean up demonstration files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_demo_files(file_demo_files, json_demo_files, backup_demo_files)
        
        print("\n=== Error Handling Demo Complete ===")
        print("\nKey takeaways:")
        print("• Use specific exception types when possible")
        print("• Always handle expected errors (FileNotFoundError, ConnectionError, etc.)")
        print("• Use finally blocks for cleanup operations")
        print("• Implement retry logic for transient errors")
        print("• Log errors with sufficient detail for debugging")
        print("• Validate data before processing")
        print("• Use context managers to ensure resource cleanup")
        print("• Don't catch exceptions you can't handle meaningfully")
        
    except Exception as e:
        print(f"Unexpected error in demonstration: {e}")
        import traceback
        traceback.print_exc()