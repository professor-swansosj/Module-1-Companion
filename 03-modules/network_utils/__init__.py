"""
Network Utils Package

This package contains utility modules for network automation tasks.
It demonstrates how to organize code into packages and modules for reusability.
"""

# Import key classes and functions to make them available at package level
from .device_config import configure_interface, configure_vlan, backup_configuration
from .network_devices import NetworkDevice, Router, Switch

# Define what gets imported with "from network_utils import *"
__all__ = [
    'configure_interface',
    'configure_vlan', 
    'backup_configuration',
    'NetworkDevice',
    'Router',
    'Switch'
]

# Package metadata
__version__ = '1.0.0'
__author__ = 'Network Automation Student'
__description__ = 'Network automation utility functions and classes'