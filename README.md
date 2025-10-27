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

The best way to learn a programming language is to use it. That is the purpose of the Companion. You should not just go through the companion and video without thought. You should understand what it is that you are practicing, change it, alter it, break it. Do whatever you want as the IDE is your own personal Canvas to build what you want. The more time you spend on the Companions the easier each Lab will be for you. You should spend most of your time in the companion. When you feel confident move over to the lab and you will find they are rather simple. The key is to practice as much as possible so you grasp the fundamentals of what we are learning.

**NOTE: IF THE PROVIDED CODE DOES NOT WORK OUT THE GATE IT IS INTENTIONAL. Read the errors the traceback provide to you to work through the problem and solve it!**

DO NOT PUSH THIS REPO BACK TO GITHUB IT IS NOT MEANT TO BE PUSHED BACK TO GITHUB. WHEN YOU ARE DONE
SIMPLY DELETE IT. IF YOU WANT TO WORK ON IT FURTHER JUST CLONE ANOTHER COPY

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

Building off the Basics in Python from your Scripting course one of the most useful features  
of Python is the ability to write your own functions(). A `Python Function` is simply a block  
of code that you can reuse. Rather than write giant single execution programs we break the code  
up into smaller blocks that we call functions(). A function can take different inputs known as  
arguments such as variables, lists, dictionaries, and tuples as an input that will be passed to  
the function upon execution. Functions do not require arguments to be passed in but it is common  
to see. For example a simple function that prints a message does not need anything else to execute  
successfully where a custom message that would require say a device hostname as part of the message  
will need that hostname passed in upon runtime.
A python function is a block of code that can be called after it is defined. As a best practice you
typically want to break up as much of your code as possible into multiple functions. As a general
guideline you should aim to have your functions be no longer than 20-30 lines of code. Most of the time
you will need to pass information into your function so it can perform some type of logic on the data.
In the function below we pass an argument name to the function and then print a message using that name.

```python
def greeting(name): #Define a function called greeting that takes one argument name
    print(f"Hello, {name}!") #Print a message using the name argument

name = "Sheldon" #Define a variable name

greeting(name) #Call the function greeting and pass in the variable name

```

### Positional Arguments

Positional arguments in Python are the values passed to a function in the exact order its parameters are defined. The position determines which parameter each value is assigned to. For example, in `def greet(name, age): ...` calling `greet("Bob", 37)` assigns `"Bob"` to `name` and `37` to `age`. If you switch the order, the meaning changes—so the *position* is what matters.

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

Keyword arguments in Python are passed by explicitly naming the parameter, so order doesn’t matter. For example, in `greet(name="Sheldon", age=37)`, each value is matched to its parameter by name, not position. This makes code clearer and allows you to mix them with positional arguments, as long as all positional ones come first.

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

Default arguments in Python are parameters that take on a preset value if no corresponding argument is provided when the function is called. They make parameters optional and help simplify code by avoiding redundant arguments. For example, `def greet(name, greeting="Hello"):` allows you to call `greet("Bob")` and automatically use “Hello,” but you can still override it with `greet("Bob", "Hi")`. The key rule is that default arguments must come after all required positional ones in the function definition.

**📁 Practice Location:** `01-functions/default_args.py`

**What to Practice:**

- Run the interface configuration with default values
- Override some defaults while keeping others
- Design a function with 3 parameters where 2 have defaults

**Challenge:** Create a function that configures a switch port with default VLAN 1 and default mode "access"

### Variable-Length Positional Arguments

Variable-length positional arguments let a function accept any number of extra positional values, captured as a tuple using `*args`. In `def f(x, *args):`, `x` gets the first argument and all remaining positional arguments land in `args` (e.g., `f(1, 2, 3, 4)` → `x=1`, `args=(2, 3, 4))`. `*args` must come after all regular positional parameters and before keyword-only parameters; you can iterate or unpack `args` inside the function as needed.

**📁 Practice Location:** `01-functions/varargs_positional.py`

**What to Practice:**

- Use *args to configure multiple VLANs at once
- Create a function that can backup configurations for any number of devices
- Practice unpacking lists into function arguments

### Variable-Length Keyword Arguments

Variable-length keyword arguments let a function accept any number of named arguments, captured as a dictionary using `**kwargs`. This means you don’t have to predetermine all possible keyword parameters. For example, in `def f(**kwargs):`, calling `f(x=1, y=2)` results in `kwargs = {'x': 1, 'y': 2}`. Inside the function, you can access, iterate, or pass these keyword pairs along to other functions. It’s a flexible way to handle optional or dynamic keyword inputs, especially useful in decorators, class constructors, and wrapper functions.

**📁 Practice Location:** `01-functions/varargs_keyword.py`

**What to Practice:**

- Use **kwargs to pass flexible configuration options
- Create a device configuration function that accepts any number of settings
- Practice unpacking dictionaries into function arguments

### Keyword-Only Arguments

Keyword-only arguments are parameters that must be specified by name when calling a function, rather than by position. They’re defined after a single asterisk (`*`) in the function signature. For example, in `def connect(host, *, timeout=5, retries=3):`, the arguments `timeout` and `retries` can only be passed as keywords like `connect("server", timeout=10)`. This makes function calls clearer and prevents mistakes caused by misordered positional arguments, especially when a function has many optional settings.

**📁 Practice Location:** `01-functions/keyword_only.py`

**What to Practice:**

- Force certain parameters to be passed as keywords for clarity
- Create a network device connection function with keyword-only security settings

### Positional-Only Arguments

Positional-only arguments are parameters that must be supplied strictly by their order, not by name. They’re defined by placing a slash (`/`) in the function signature. Any parameter before the slash is positional-only. For example, `def ratio(a, b, /):` means you must call it like `ratio(4, 2)`, not `ratio(a=4, b=2)`. This helps enforce cleaner, faster calls and protects internal parameter names from becoming part of your public API.

**📁 Practice Location:** `01-functions/positional_only.py`

**What to Practice:**

- Use positional-only parameters for core network settings
- Understand when to use this feature for API consistency

### Annotated Arguments

Annotated arguments in Python let you attach optional metadata—called type hints or annotations—to function parameters and return values. They don’t affect how the code runs but serve as documentation and can be checked by tools like mypy or IDEs for static analysis. For example,

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}."
```

Here, `name: str` and `age: int` indicate that `name` should be a string and `age` should be an integer, while `-> str` hints that the function returns a string. Annotations can be any valid Python expression, not just types, and are stored in the function’s `__annotations__` dictionary for inspection at runtime.

**📁 Practice Location:** `01-functions/annotated_args.py`

**What to Practice:**

- Add type hints to your network automation functions
- Use annotations to document expected data types
- Practice with List, Dict, and custom type annotations

---

## 🏗️ Classes and Objects

Object-oriented programming helps organize complex network automation tasks. You'll create classes for network devices, configurations, and monitoring systems.

A powerful feature of Python is the ability to create your own `Classes` and `Objects`.  A class is a
blueprint for an object. An object is an instance of a class. Classes can contain attributes (variables) and
methods (functions). Classes are used to model real-world entities and their behaviors. For example, you might
have a class called `NetworkDevice` that has attributes like `hostname`, `ip_address`, and `device_type`, and
methods like `connect()`, `disconnect()`, and `get_status()`. You can then create multiple instances of the
`NetworkDevice` class, each representing a different network device.
In python we define objects by defining the class. Think of an object as a way to represent anything
in the real world. The attributes help to describe the object. Inside an object we can also define
methods which are functions that are related to our object.

```python
class NetworkDevice: #Define our Class object of NetworkDevice
  def __init__(self, hostname, ip, device_type): #Initialize the object as well as the attributes
      self.hostname = hostname        #Define attribute hostname
      self.ip = ip                    #Define attribute ip 
      self.device_type = device_type  #Define attribute device_type
      self.vendor = "Cisco"           #Define attribute vendor with a default value of Cisco

  def summarize(self): #Define a method called summarize
      return f"{self.hostname} ({self.device_type}) - {self.ip}" #Return a summary string

device1 = NetworkDevice("router1", "192.168.1.1", "router") #Create an instance of the NetworkDevice class
print(device1.summarize()) #Call the summarize method on the device1 object

```

### Creating and Initializing Basic Class

A basic class in network automation defines a new type of network object with its own data (attributes) and behavior (methods). You create one with the `class` keyword and initialize instances using `__init__`, which automatically runs when the object is created. The first parameter, `self`, refers to the specific instance so you can assign attributes like hostname or IP address to it. Inside `__init__`, you typically store connection details or configuration defaults that belong to that device.

```python
class NetworkDevice:
    def __init__(self, hostname: str, ip_address: str):
        self.hostname = hostname     # instance attribute
        self.ip_address = ip_address

    def connect(self):
        return f"Connecting to {self.hostname} at {self.ip_address}..."

# Creating (instantiating) objects:
dev1 = NetworkDevice("CoreSwitch", "10.0.0.1")
dev2 = NetworkDevice("Firewall", "10.0.0.2")

print(dev1.connect())   # Connecting to CoreSwitch at 10.0.0.1...
```

Here, `NetworkDevice` is the class, `__init__` sets up each device’s unique details, and `connect()` represents a method you might later expand to perform actual SSH or API connections in real automation tasks.

**📁 Practice Location:** `02-classes/basic_class.py`

**What to Practice:**

- Create a NetworkDevice class with basic initialization
- Instantiate multiple device objects
- Access and print object attributes

**Try This:** Create 3 different router objects with different hostnames and IP addresses

### Class Properties

In network automation, class properties are often used to manage and validate device attributes—like IP addresses or hostnames—while keeping the interface simple and readable. They let you safely control how data is accessed or modified without exposing internal variables directly. You create a property using the `@property` decorator, which makes a method act like an attribute, and can pair it with a setter to add validation logic.

```python
class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self._hostname = hostname
        self._ip_address = ip_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        if not value.count(".") == 3:
            raise ValueError("Invalid IP address format")
        self._ip_address = value
```

Here, accessing `device.ip_address` calls the getter automatically, while assigning a new value (`device.ip_address = "10.0.0.5"`) triggers the setter, which checks that the format looks valid. This keeps your automation scripts safe from bad input while maintaining clean, readable code.

**📁 Practice Location:** `02-classes/class_properties.py`

**What to Practice:**

- Add properties to control access to device attributes
- Create getter and setter methods for IP addresses
- Implement validation in property setters

**Challenge:** Create a property that validates IP address format before setting

### Class Methods

In network automation, a class method is a function that operates on the class itself rather than on a single device instance. It’s defined with the `@classmethod` decorator and takes `cls` as its first argument, representing the class. Class methods are useful for creating devices from standard templates or shared data sources, such as loading device details from a configuration file or inventory.

```python
class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor using a dictionary of device info"""
        return cls(data["hostname"], data["ip_address"])

# Example use
device_info = {"hostname": "CoreSwitch", "ip_address": "10.0.0.1"}
device = NetworkDevice.from_dict(device_info)

print(device.hostname)   # CoreSwitch
print(device.ip_address) # 10.0.0.1
```

Here, the `from_dict` method acts as an alternate constructor—it creates a `NetworkDevice` directly from structured data. Since it’s a class method, it works the same way even if you later subclass `NetworkDevice` for specific vendors or device types.

**📁 Practice Location:** `02-classes/class_methods.py`

**What to Practice:**

- Add methods to connect, configure, and disconnect from devices
- Create methods that return configuration status
- Practice method chaining for fluent interfaces

**Try This:** Add a method to backup device configuration and another to restore it

### Class Inheritance

Class inheritance allows one class to reuse and extend the behavior of another, which is a core part of object-oriented programming. The original, or parent class, defines common attributes and methods, while the child class inherits them and can add or modify functionality as needed. In network automation, for instance, you might create a general `NetworkDevice` class that handles shared behavior like connecting to a device, and then create subclasses such as `CiscoDevice` or `FortiGateDevice` that override certain methods like `get_version()` to perform vendor-specific actions. This makes code easier to maintain and extend, since all common logic lives in one place, while differences are isolated in the subclasses. It also allows you to use polymorphism—treating different device types the same way when calling shared methods like `connect()` or `get_version()`.

```python
# Base class
class NetworkDevice:
    def __init__(self, host):
        self.host = host

    def connect(self):
        print(f"Connecting to {self.host}...")

    def get_version(self):
        # Meant to be overridden
        return "Unknown OS"

# Child classes
class CiscoDevice(NetworkDevice):
    def get_version(self):
        return "Cisco IOS-XE 17.9"

class FortiGateDevice(NetworkDevice):
    def get_version(self):
        return "FortiOS 7.4"

# Use it
devices = [
    CiscoDevice("10.0.0.10"),
    FortiGateDevice("10.0.0.12"),
]

for d in devices:
    d.connect()
    print(d.get_version())
```

**📁 Practice Location:** `02-classes/inheritance.py`

**What to Practice:**

- Create a base NetworkDevice class
- Inherit from it to create Router and Switch classes
- Override methods to provide device-specific behavior
- Use super() to call parent class methods

**Challenge:** Create a hierarchy: NetworkDevice → Router → ISR4000Router

---

## 📦 Creating Modules and Importing

In Python, a module is simply a file that contains code—functions, classes, or variables—that you can reuse in other programs. To create one, you just save your code in a `.py` file, and to use it elsewhere, you import it with the `import` statement. For example, if you have a file named `network_tools.py` with a function called `ping_device()`, you can use it in another script by writing `import network_tools` and then calling `network_tools.ping_device()`. You can also import specific parts of a module with `from network_tools import ping_device`. Modules keep your code organized, easier to read, and reusable across multiple network automation scripts.

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

In Python, the `__init__.py` file defines how a directory behaves when it’s imported as a package. When you import a package, Python executes the code inside that `__init__.py` file exactly once, setting up the package namespace. This is where you can include variables, import other modules, and control what symbols become available when someone runs `from package import *`. In older versions of Python, its presence was required for Python to even recognize a directory as a package, but modern versions allow namespace packages without it. Still, `__init__.py` remains very useful: it lets you manage imports cleanly so users don’t need to know the internal file structure. For instance, you can import specific classes or functions from submodules and re-export them, simplifying the interface of your package. In short, `__init__.py` is the package’s entry point—it executes setup code on import, defines what’s public, and often serves as the “front door” through which everything else in the package becomes accessible.

**📁 Practice Location:** `03-modules/network_utils/__init__.py`

**What to Practice:**

- Understand how `__init__.py` makes a directory a package
- Control what gets imported with `__all__`
- Create convenient imports for package users

### Importing Best Practices

When importing in Python, keep it clean and predictable. Always place imports at the top of your file, right after any module docstring. Use absolute imports whenever possible, such as `from network_automation.devices import CiscoDevice`, so your code is clear and works across projects. Avoid wildcard imports like `from tools import *` because they clutter the namespace and make debugging harder. Group imports by standard library, third-party modules, and your own files, leaving a blank line between each group. Import only what you need—`from netmiko import ConnectHandler` is faster and easier to read than importing the whole library. Finally, avoid circular imports by placing shared constants or helper functions in a separate module if needed.

**📁 Practice Location:** `03-modules/import_examples.py`

**What to Practice:**

- Use different import styles (import, from...import, as)
- Understand when to use each import method
- Practice organizing imports in your scripts

---

## 📂 Working with Files

Working with files in Python involves opening, reading, writing, and closing files using the built-in `open()` function. You can read contents with methods like `read()` or `readlines()`, and write data with `write()` or `writelines()`. Always close files when finished, or better yet, use a `with` statement like `with open("devices.txt", "r") as f:` so Python handles closing automatically. This approach is common in network automation for reading device lists, saving logs, or exporting configuration data.

### The OS Module

The `os` module gives you portable access to your operating system—handy for network automation scripts that need to read env vars, manage paths, or touch files and directories. Common moves: get or set environment values with `os.getenv("API_TOKEN")` and `os.environ["REGION"]="us-east"`, find the current directory using `os.getcwd()`, change directories with `os.chdir("/labs")`, list files via `os.listdir("inventory")`, create folders safely with `os.makedirs("outputs/logs", exist_ok=True)`, and join paths portably using `os.path.join("configs", "routers", "r1.txt")`. For running external commands prefer `subprocess`, but a quick call with `os.system("ping 10.0.0.1 -n 1")` can work in simple demos.

**📁 Practice Location:** `04-files/os_operations.py`

**What to Practice:**

- Navigate directories containing network configurations
- Create directories for device backups
- Check if configuration files exist
- Get file information and permissions

**Try This:** Create a backup directory structure for different device types

### The open() Function

`open()` returns a file handle so you can read or write data. Use a context manager so it auto-closes: `with open("devices.txt", "r") as f:`. Modes: `"r"` read, `"w"` write (truncate), `"a"` append, `"rb"`/`"wb"` binary. Read with `f.read()` or iterate lines; write with `f.write(text)`. Example:

```python
# read device hosts
with open("inventory/devices.txt", "r", encoding="utf-8") as f:
    hosts = [line.strip() for line in f if line.strip()]

# write results
with open("outputs/scan.txt", "w", encoding="utf-8") as f:
    for h in hosts:
        f.write(f"{h}: reachable\n")
```

**📁 Practice Location:** `04-files/basic_file_ops.py`

**What to Practice:**

- Open configuration files for reading
- Understand different file modes
- Practice proper file closing

### The with open() Function

`with open()` is the context-manager way to work with files so they close automatically—even if errors happen. Use it to read or write cleanly:

```python
# read
with open("inventory/devices.txt", "r", encoding="utf-8") as f:
    hosts = [line.strip() for line in f if line.strip()]

# write
with open("outputs/results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(hosts))
```

**📁 Practice Location:** `04-files/context_manager.py`

**What to Practice:**

- Use with statements for automatic file handling
- Read configuration templates
- Understand why this is the preferred method

**Challenge:** Read a device configuration template and replace placeholders with actual values

### Create, Read, and Append

Use `with open()` to safely create, read, and append files. Create (or overwrite) with `"w"`, read with `"r"`, and append with `"a"`:

```python
# Create/overwrite: write initial inventory
with open("inventory/devices.txt", "w", encoding="utf-8") as f:
    f.write("10.0.0.10\n10.0.0.11\n")

# Read: load hosts
with open("inventory/devices.txt", "r", encoding="utf-8") as f:
    hosts = [line.strip() for line in f if line.strip()]

# Append: add a discovery result
with open("logs/discovery.log", "a", encoding="utf-8") as f:
    f.write("10.0.0.12 reachable\n")
```

Use `"x"` to fail if the file already exists, and `"rb"`/`"wb"` for binary data.

**📁 Practice Location:** `04-files/file_operations.py`

**What to Practice:**

- Create new configuration files
- Read existing device configurations
- Append log entries to monitoring files
- Practice with different file modes

---

## ⚠️ Error Handling with try...except

Use `try...except` to handle errors without crashing, keeping the script moving when something fails.

```python
# minimal example
try:
    with open("inventory/devices.txt", "r", encoding="utf-8") as f:
        hosts = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("inventory/devices.txt not found")

# simple network call with a generic catch
try:
    result = ping("10.0.0.10")  # pretend function for demo
except Exception as e:
    print(f"Ping failed: {e}")
```

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

Working with data formats in Python means handling structured files like JSON, CSV, or YAML that store device info or automation results. Use the `json` module for reading and writing JSON (`json.load()` and `json.dump()`), `csv` for spreadsheets, and `yaml` (via PyYAML) for configuration data. These formats make it easy to share, parse, and automate network data between scripts and tools.

### JSON

JSON (JavaScript Object Notation) is a lightweight text format for storing and sharing data. In Python, use the `json` module—`json.load()` to read from a file and `json.dump()` to write. It’s perfect for storing device configs or API responses in network automation.

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

YAML (YAML Ain’t Markup Language) is a human-friendly format for structured data, often used for configs and playbooks. In Python, use the `yaml` module (`yaml.safe_load()` and `yaml.dump()`) to read and write it—ideal for network inventories and automation settings.

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

XML (eXtensible Markup Language) is a structured text format often used in network devices and APIs. In Python, use the `xml.etree.ElementTree` module to read, parse, and create XML data—commonly for exchanging configurations or NETCONF responses.

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

CSV (Comma-Separated Values) is a simple format for storing tabular data like device lists or logs. In Python, use the `csv` module—`csv.reader()` to read rows and `csv.writer()` to write them. It’s great for quick inventory files or exporting network data.

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
