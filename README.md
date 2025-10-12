# Software Defined Networking - Module 1 Companion Lab

**Course:** Software Defined Networking  
**Module:** 1 - Python Fundamentals Review and Advanced Concepts

## 📚 Table of Contents

- [Getting Started](#-getting-started)
- [Python Functions](#-python-functions)
  - [Positional Arguments](#positional-arguments)
  - [Keyword Arguments](#keyword-arguments)
  - [Default Arguments](#default-arguments)
  - [Variable-Length Positional Arguments](#variable-length-positional-arguments)
  - [Variable-Length Keyword Arguments](#variable-length-keyword-arguments)
  - [Keyword-Only Arguments](#keyword-only-arguments)
  - [Positional-Only Arguments](#positional-only-arguments)
  - [Annotated Arguments](#annotated-arguments)
- [Classes and Objects](#️-classes-and-objects)
  - [Creating and Initializing Basic Class](#creating-and-initializing-basic-class)
  - [Class Properties](#class-properties)
  - [Class Methods](#class-methods)
  - [Class Inheritance](#class-inheritance)
- [Creating Modules and Importing](#-creating-modules-and-importing)
  - [Import Your Own Functions and Classes](#import-your-own-functions-and-classes)
  - [The `__init__.py` File](#the-__init__py-file)
  - [Importing Best Practices](#importing-best-practices)
- [Working with Files](#-working-with-files)
  - [The OS Module](#the-os-module)
  - [The open() Function](#the-open-function)
  - [The with open() Function](#the-with-open-function)
  - [Create, Read, and Append](#create-read-and-append)
- [Error Handling with try...except](#️-error-handling-with-tryexcept)
- [Working with Data Formats](#-working-with-data-formats)
  - [JSON](#json)
  - [YAML](#yaml)
  - [XML](#xml)
  - [CSV](#csv)

---

## 🚀 Getting Started

Welcome to the Module 1 Companion Lab! This repository contains hands-on practice exercises to reinforce the concepts covered in your instructional video.

**How to use this repository:**

1. Clone or download this repository to your local machine
2. Follow along with the video lessons
3. Complete the practice exercises in each section
4. Experiment with the sample data provided
5. Test your understanding with the challenge exercises

**Prerequisites:** Completion of Linux+, Introduction to Python, and Cisco 1,2,3

---

## 🔧 Python Functions

Functions are the building blocks of clean, reusable code. In network automation, you'll use functions to perform repetitive tasks like device configuration, data parsing, and network monitoring.

### Positional Arguments

**📁 Practice Location:** `01-functions/positional_args.py`

**What to Practice:**

- Run the example function that configures a network interface
- Modify the function to accept different interface types
- Create your own function that takes 3 positional arguments for IP configuration

**Try This:**

```bash
cd 01-functions
python positional_args.py
```

### Keyword Arguments

**📁 Practice Location:** `01-functions/keyword_args.py`

**What to Practice:**

- Execute the VLAN configuration function using keyword arguments
- Practice calling the function with arguments in different orders
- Create a function that configures OSPF with keyword arguments

**Try This:**

```bash
python keyword_args.py
```

### Default Arguments

**📁 Practice Location:** `01-functions/default_args.py`

**What to Practice:**

- Run the interface configuration with default values
- Override some defaults while keeping others
- Design a function with 3 parameters where 2 have defaults

**Challenge:** Create a function that configures a switch port with default VLAN 1 and default mode "access"

### Variable-Length Positional Arguments

**📁 Practice Location:** `01-functions/varargs_positional.py`

**What to Practice:**

- Use *args to configure multiple VLANs at once
- Create a function that can backup configurations for any number of devices
- Practice unpacking lists into function arguments

### Variable-Length Keyword Arguments

**📁 Practice Location:** `01-functions/varargs_keyword.py`

**What to Practice:**

- Use **kwargs to pass flexible configuration options
- Create a device configuration function that accepts any number of settings
- Practice unpacking dictionaries into function arguments

### Keyword-Only Arguments

**📁 Practice Location:** `01-functions/keyword_only.py`

**What to Practice:**

- Force certain parameters to be passed as keywords for clarity
- Create a network device connection function with keyword-only security settings

### Positional-Only Arguments

**📁 Practice Location:** `01-functions/positional_only.py`

**What to Practice:**

- Use positional-only parameters for core network settings
- Understand when to use this feature for API consistency

### Annotated Arguments

**📁 Practice Location:** `01-functions/annotated_args.py`

**What to Practice:**

- Add type hints to your network automation functions
- Use annotations to document expected data types
- Practice with List, Dict, and custom type annotations

---

## 🏗️ Classes and Objects

Object-oriented programming helps organize complex network automation tasks. You'll create classes for network devices, configurations, and monitoring systems.

### Creating and Initializing Basic Class

**📁 Practice Location:** `02-classes/basic_class.py`

**What to Practice:**

- Create a NetworkDevice class with basic initialization
- Instantiate multiple device objects
- Access and print object attributes

**Try This:** Create 3 different router objects with different hostnames and IP addresses

### Class Properties

**📁 Practice Location:** `02-classes/class_properties.py`

**What to Practice:**

- Add properties to control access to device attributes
- Create getter and setter methods for IP addresses
- Implement validation in property setters

**Challenge:** Create a property that validates IP address format before setting

### Class Methods

**📁 Practice Location:** `02-classes/class_methods.py`

**What to Practice:**

- Add methods to connect, configure, and disconnect from devices
- Create methods that return configuration status
- Practice method chaining for fluent interfaces

**Try This:** Add a method to backup device configuration and another to restore it

### Class Inheritance

**📁 Practice Location:** `02-classes/inheritance.py`

**What to Practice:**

- Create a base NetworkDevice class
- Inherit from it to create Router and Switch classes
- Override methods to provide device-specific behavior
- Use super() to call parent class methods

**Challenge:** Create a hierarchy: NetworkDevice → Router → ISR4000Router

---

## 📦 Creating Modules and Importing

Organize your network automation code into reusable modules for better maintainability and code sharing.

### Import Your Own Functions and Classes

**📁 Practice Location:** `03-modules/network_utils/`

**What to Practice:**

- Import functions from the device_config module
- Import classes from the network_devices module
- Use imported functions in your main script

**Try This:**

```bash
cd 03-modules
python main.py
```

### The `__init__.py` File

**📁 Practice Location:** `03-modules/network_utils/__init__.py`

**What to Practice:**

- Understand how `__init__.py` makes a directory a package
- Control what gets imported with `__all__`
- Create convenient imports for package users

### Importing Best Practices

**📁 Practice Location:** `03-modules/import_examples.py`

**What to Practice:**

- Use different import styles (import, from...import, as)
- Understand when to use each import method
- Practice organizing imports in your scripts

---

## 📂 Working with Files

File operations are essential for network automation - reading configuration files, logging, and storing network data.

### The OS Module

**📁 Practice Location:** `04-files/os_operations.py`

**What to Practice:**

- Navigate directories containing network configurations
- Create directories for device backups
- Check if configuration files exist
- Get file information and permissions

**Try This:** Create a backup directory structure for different device types

### The open() Function

**📁 Practice Location:** `04-files/basic_file_ops.py`

**What to Practice:**

- Open configuration files for reading
- Understand different file modes
- Practice proper file closing

### The with open() Function

**📁 Practice Location:** `04-files/context_manager.py`

**What to Practice:**

- Use with statements for automatic file handling
- Read configuration templates
- Understand why this is the preferred method

**Challenge:** Read a device configuration template and replace placeholders with actual values

### Create, Read, and Append

**📁 Practice Location:** `04-files/file_operations.py`

**What to Practice:**

- Create new configuration files
- Read existing device configurations
- Append log entries to monitoring files
- Practice with different file modes

---

## ⚠️ Error Handling with try...except

Network operations often fail - devices are unreachable, configurations are invalid, or connections timeout. Learn to handle these gracefully.

**📁 Practice Location:** `05-error-handling/`

**What to Practice:**

- Handle connection failures to network devices
- Catch and manage file operation errors
- Use specific exception types for different error scenarios
- Practice with finally blocks for cleanup operations

**Try This:**

```bash
cd 05-error-handling
python network_errors.py
```

**Scenarios to Practice:**

- Device connection timeout
- Invalid configuration syntax  
- File permission errors
- Network unreachable errors

---

## 📊 Working with Data Formats

Network automation relies heavily on structured data. Master these formats for configuration management, API interactions, and data storage.

### JSON

**📁 Practice Location:** `06-data-formats/json_examples/`
**📁 Sample Data:** `sample-data/network_devices.json`

**What JSON Is:** JavaScript Object Notation - lightweight, human-readable data format
**Syntax:** Uses key-value pairs, arrays, and nested objects with strict formatting rules

**What to Practice:**

- Load device inventory from JSON files
- Parse API responses from network controllers
- Create configuration templates in JSON format
- Convert Python dictionaries to/from JSON

**Try This:**

```bash
cd 06-data-formats/json_examples
python json_operations.py
```

**Practice Tasks:**

1. Load the sample device inventory and print all router hostnames
2. Add a new device to the JSON data and save it back
3. Extract all devices in a specific location
4. Create a JSON report of device status

### YAML

**📁 Practice Location:** `06-data-formats/yaml_examples/`
**📁 Sample Data:** `sample-data/network_config.yaml`

**What YAML Is:** Human-readable data serialization standard, commonly used for configuration files
**Syntax:** Uses indentation, lists with dashes, and key-value pairs without quotes

**What to Practice:**

- Read Ansible playbook-style configurations
- Parse network device configurations from YAML
- Create infrastructure-as-code templates
- Handle YAML parsing errors

**Try This:**

```bash
python yaml_operations.py
```

### XML

**📁 Practice Location:** `06-data-formats/xml_examples/`
**📁 Sample Data:** `sample-data/network_topology.xml`

**What XML Is:** Extensible Markup Language - structured data format with tags and attributes
**Syntax:** Uses opening/closing tags, attributes, and hierarchical structure

**What to Practice:**

- Parse NETCONF responses from network devices
- Extract data from network monitoring tools
- Create XML configuration snippets
- Navigate XML tree structures

**Try This:**

```bash
python xml_operations.py
```

### CSV

**📁 Practice Location:** `06-data-formats/csv_examples/`
**📁 Sample Data:** `sample-data/device_inventory.csv`

**What CSV Is:** Comma-Separated Values - simple tabular data format
**Syntax:** Rows of data with commas separating values, first row often contains headers

**What to Practice:**

- Import device inventories from spreadsheets
- Export network monitoring data for analysis
- Process bulk configuration data
- Handle CSV files with different delimiters

**Try This:**

```bash
python csv_operations.py
```

---

## 🎯 Putting It All Together

**📁 Final Challenge:** `07-final-challenge/network_automation_project.py`

Create a complete network automation script that:

1. Uses classes to represent network devices
2. Imports functions from custom modules
3. Reads configuration data from multiple file formats
4. Handles errors gracefully
5. Logs operations to files
6. Uses proper function annotations and documentation

**Success Criteria:**

- Script runs without errors
- All file operations use context managers
- Exceptions are properly handled
- Code is organized into functions and classes
- Configuration data is read from JSON/YAML files

---

## 📝 Notes for Success

- **Practice Regularly:** Run each example and modify it to understand the concepts
- **Experiment:** Change parameters and see what happens
- **Build Incrementally:** Start with simple examples and add complexity
- **Use the Debugger:** Step through code to understand execution flow
- **Ask Questions:** If something doesn't work as expected, investigate why

**Remember:** This is practice - make mistakes, break things, and learn from the experience!

---

## 🔗 Additional Resources

- All sample data files are located in the `sample-data/` directory
- Configuration templates are in the `templates/` directory  
- Completed examples are in each topic's folder
- Challenge solutions are in the `solutions/` directory (try the challenges first!)

Good luck with your network automation journey! 🚀
A Companion Repo for Module 1 Topics
