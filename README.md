# Module 1 Companion - Python Fundamentals for Network Automation

## Software Defined Networking Course

> **Practice Makes Perfect!** The purpose of the Companion Repo is to help you build a strong foundation of knowledge and skills so you can succeed in the graded lab. This companion is your hands-on workshop for mastering Python fundamentals in network automation. Get ready to code, explore, and build the foundation for advanced SDN concepts!

## 🎯 What You'll Practice

Master Python fundamentals through network automation scenarios! You'll build functions that configure devices, create classes for network equipment, handle data files, and develop error-resistant automation scripts. Each section builds your coding confidence while preparing you for real-world SDN challenges.

## 📋 Prerequisites

- Completion of Linux+, Introduction to Python, and Cisco 1,2,3
- VS Code or your preferred Python IDE
- Python 3.8+ installed and ready to go

## 🗂 Learning Path

**Work through these sections progressively - each builds on the previous!**

| Section | Focus | What You'll Build |
|--------|--------|-------------------|
| **01-functions/** | Function Mastery | Network automation functions with various argument patterns |
| **02-classes/** | Object-Oriented Design | Network device classes with inheritance and properties |
| **03-modules/** | Code Organization | Custom network utility packages and imports |
| **04-files/** | File Operations | Configuration file handlers and backup systems |
| **05-error-handling/** | Robust Code | Error-resistant network automation with try/except |
| **06-data-formats/** | Data Processing | Master JSON, CSV, YAML, and XML for network data |

## 🎯 Practice Callouts

Throughout each section, look for these opportunities to get hands-on:

- 🔧 **TODO Comments**: Complete the missing code to make scripts work
- 💡 **Hints**: Guidance to nudge you toward solutions without spoilers
- 🚀 **Challenges**: Extend your learning with bonus implementations
- 🧪 **Experiments**: Break things, modify code, see what happens!

## 🚀 Getting Hands-On

The best way to learn programming is to **write code**! This companion is your personal coding playground where you can:

- **Explore**: Change parameters, add features, see what happens
- **Break Things**: Intentionally cause errors to learn debugging
- **Build Confidence**: Start simple, gradually tackle complex challenges
- **Practice**: The more you code, the easier the labs become

> **🎯 Success Tip**: Spend serious time here! Master these fundamentals and the graded labs will feel straightforward.

**Important Notes:**

- 🔥 **Some code is intentionally incomplete** - read error messages and fix the issues!
- 📝 **This is practice space** - don't push back to GitHub, just code and learn
- 🎯 **Focus on understanding** - don't just run code, comprehend what it does

## 🔧 Quick Start Guide

Ready to dive in? Here's your roadmap:

1. **Start with 01-functions/** - Master function patterns for network automation
2. **Progress through each section** - Each builds on the previous
3. **Complete the TODOs** - Make the code work by filling in missing pieces
4. **Experiment freely** - Change code, break things, learn by doing!
5. **Build confidence** - Each success prepares you for the next challenge

## 🎖 Module 1 Companion Quick Reference

### Section 01: Functions

#### Positional Arguments

Positional arguments in Python are the values passed to a function in the exact order its parameters are defined. The position determines which parameter each value is assigned to. For example, in `def greet(name, age): ...` calling `greet("Bob", 37)` assigns `"Bob"` to `name` and `37` to `age`. If you switch the order, the meaning changes—so the *position* is what matters.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Run the example function that configures a network interface
- Modify the function to accept different interface types
- Create your own function that takes 3 positional arguments for IP configuration

**Try This:**

```bash
cd 01-functions
python function_basics.py
```

#### Keyword Arguments

Keyword arguments in Python are passed by explicitly naming the parameter, so order doesn’t matter. For example, in `greet(name="Sheldon", age=37)`, each value is matched to its parameter by name, not position. This makes code clearer and allows you to mix them with positional arguments, as long as all positional ones come first.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Execute the VLAN configuration function using keyword arguments
- Practice calling the function with arguments in different orders
- Create a function that configures OSPF with keyword arguments

#### Default Arguments

Default arguments in Python are parameters that take on a preset value if no corresponding argument is provided when the function is called. They make parameters optional and help simplify code by avoiding redundant arguments. For example, `def greet(name, greeting="Hello"):` allows you to call `greet("Bob")` and automatically use “Hello,” but you can still override it with `greet("Bob", "Hi")`. The key rule is that default arguments must come after all required positional ones in the function definition.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Run the interface configuration with default values
- Override some defaults while keeping others
- Design a function with 3 parameters where 2 have defaults

**Challenge:** Create a function that configures a switch port with default VLAN 1 and default mode "access"

#### Variable-Length Positional Arguments

Variable-length positional arguments let a function accept any number of extra positional values, captured as a tuple using `*args`. In `def f(x, *args):`, `x` gets the first argument and all remaining positional arguments land in `args` (e.g., `f(1, 2, 3, 4)` → `x=1`, `args=(2, 3, 4))`. `*args` must come after all regular positional parameters and before keyword-only parameters; you can iterate or unpack `args` inside the function as needed.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Use *args to configure multiple VLANs at once
- Create a function that can backup configurations for any number of devices
- Practice unpacking lists into function arguments

#### Variable-Length Keyword Arguments

Variable-length keyword arguments let a function accept any number of named arguments, captured as a dictionary using `**kwargs`. This means you don’t have to predetermine all possible keyword parameters. For example, in `def f(**kwargs):`, calling `f(x=1, y=2)` results in `kwargs = {'x': 1, 'y': 2}`. Inside the function, you can access, iterate, or pass these keyword pairs along to other functions. It’s a flexible way to handle optional or dynamic keyword inputs, especially useful in decorators, class constructors, and wrapper functions.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Use **kwargs to pass flexible configuration options
- Create a device configuration function that accepts any number of settings
- Practice unpacking dictionaries into function arguments

#### Keyword-Only Arguments

Keyword-only arguments are parameters that must be specified by name when calling a function, rather than by position. They’re defined after a single asterisk (`*`) in the function signature. For example, in `def connect(host, *, timeout=5, retries=3):`, the arguments `timeout` and `retries` can only be passed as keywords like `connect("server", timeout=10)`. This makes function calls clearer and prevents mistakes caused by misordered positional arguments, especially when a function has many optional settings.

**📁 Practice Location:** `01-functions/function_basics.py`

**What to Practice:**

- Force certain parameters to be passed as keywords for clarity
- Create a network device connection function with keyword-only security settings

#### Positional-Only Arguments

Lock down function parameters to prevent misuse in network automation scripts.

**📁 Practice Location:** `01-functions/function_basics.py`

**🎯 Your Mission:** Build functions where core parameters can't be accidentally passed by name

#### Annotated Arguments

Add type hints to make your network automation code more professional and maintainable.

**📁 Practice Location:** `01-functions/function_basics.py`

**🎯 Your Mission:** Transform basic functions with proper type annotations for IP addresses, device lists, and configuration data

---

### Section 02: Classes and Objects

Object-oriented programming helps organize complex network automation tasks. You'll create classes for network devices, configurations, and monitoring systems.

Build reusable network device objects that represent real infrastructure in your code.

#### Creating and Initializing Basic Class

Create your first network device blueprint with data and behaviors.

**📁 Practice Location:** `02-classes/class_fundamentals.py`

**🎯 Your Mission:** Build a NetworkDevice class and create multiple device instances

**💪 Level Up:** Add methods for device status and configuration backup

#### Class Properties

Add smart validation to your device objects to prevent configuration errors.

**📁 Practice Location:** `02-classes/class_fundamentals.py`

**🎯 Your Mission:** Build properties with IP address validation

**💪 Level Up:** Add hostname format checking and device type validation

#### Class Methods

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

**📁 Practice Location:** `02-classes/class_fundamentals.py`

**What to Practice:**

- Add methods to connect, configure, and disconnect from devices
- Create methods that return configuration status
- Practice method chaining for fluent interfaces

**Try This:** Add a method to backup device configuration and another to restore it

#### Class Inheritance

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

**📁 Practice Location:** `02-classes/class_fundamentals.py`

**What to Practice:**

- Create a base NetworkDevice class
- Inherit from it to create Router and Switch classes
- Override methods to provide device-specific behavior
- Use super() to call parent class methods

**Challenge:** Create a hierarchy: NetworkDevice → Router → ISR4000Router

---

### Section 03: Modules and Importing

In Python, a module is simply a file that contains code—functions, classes, or variables—that you can reuse in other programs. To create one, you just save your code in a `.py` file, and to use it elsewhere, you import it with the `import` statement. For example, if you have a file named `network_tools.py` with a function called `ping_device()`, you can use it in another script by writing `import network_tools` and then calling `network_tools.ping_device()`. You can also import specific parts of a module with `from network_tools import ping_device`. Modules keep your code organized, easier to read, and reusable across multiple network automation scripts.

#### Import Your Own Functions and Classes

**📁 Practice Location:** `03-modules/module_practice.py`

**What to Practice:**

- Import functions from the device_config module
- Import classes from the network_devices module
- Use imported functions in your main script

**Try This:**

```bash
cd 03-modules
python module_practice.py
```

#### The `__init__.py` File

In Python, the `__init__.py` file defines how a directory behaves when it’s imported as a package. When you import a package, Python executes the code inside that `__init__.py` file exactly once, setting up the package namespace. This is where you can include variables, import other modules, and control what symbols become available when someone runs `from package import *`. In older versions of Python, its presence was required for Python to even recognize a directory as a package, but modern versions allow namespace packages without it. Still, `__init__.py` remains very useful: it lets you manage imports cleanly so users don’t need to know the internal file structure. For instance, you can import specific classes or functions from submodules and re-export them, simplifying the interface of your package. In short, `__init__.py` is the package’s entry point—it executes setup code on import, defines what’s public, and often serves as the “front door” through which everything else in the package becomes accessible.

**📁 Practice Location:** `03-modules/module_practice.py`

**What to Practice:**

- Understand how `__init__.py` makes a directory a package
- Control what gets imported with `__all__`
- Create convenient imports for package users

#### Importing Best Practices

When importing in Python, keep it clean and predictable. Always place imports at the top of your file, right after any module docstring. Use absolute imports whenever possible, such as `from network_automation.devices import CiscoDevice`, so your code is clear and works across projects. Avoid wildcard imports like `from tools import *` because they clutter the namespace and make debugging harder. Group imports by standard library, third-party modules, and your own files, leaving a blank line between each group. Import only what you need—`from netmiko import ConnectHandler` is faster and easier to read than importing the whole library. Finally, avoid circular imports by placing shared constants or helper functions in a separate module if needed.

#### The Direct Execution Check

`if __name__ == "__main__"`: ensures that certain code only runs when the file is executed directly, not when it’s imported as a module. Python sets the special variable `__name__` to `"__main__"` for the main script, but to the module’s name when imported. This lets you keep reusable functions and classes separate from test or execution code.

To make sure a block of code only runs when a script is executed directly (not when it’s imported as a module), use the `if __name__ == "__main__"`: check. It’s written exactly like this:

```python
if __name__ == "__main__":
    # code that runs only when this file is executed directly
    main()
```

**📁 Practice Location:** `03-modules/module_practice.py`

**What to Practice:**

- Use different import styles (import, from...import, as)
- Understand when to use each import method
- Practice organizing imports in your scripts

---

### Section 04: Working with Files

Working with files in Python involves opening, reading, writing, and closing files using the built-in `open()` function. You can read contents with methods like `read()` or `readlines()`, and write data with `write()` or `writelines()`. Always close files when finished, or better yet, use a `with` statement like `with open("devices.txt", "r") as f:` so Python handles closing automatically. This approach is common in network automation for reading device lists, saving logs, or exporting configuration data.

#### The OS Module

The `os` module gives you portable access to your operating system—handy for network automation scripts that need to read env vars, manage paths, or touch files and directories. Common moves: get or set environment values with `os.getenv("API_TOKEN")` and `os.environ["REGION"]="us-east"`, find the current directory using `os.getcwd()`, change directories with `os.chdir("/labs")`, list files via `os.listdir("inventory")`, create folders safely with `os.makedirs("outputs/logs", exist_ok=True)`, and join paths portably using `os.path.join("configs", "routers", "r1.txt")`. For running external commands prefer `subprocess`, but a quick call with `os.system("ping 10.0.0.1 -n 1")` can work in simple demos.

**📁 Practice Location:** `04-files/file_practice.py`

**What to Practice:**

- Navigate directories containing network configurations
- Create directories for device backups
- Check if configuration files exist
- Get file information and permissions

**Try This:** Create a backup directory structure for different device types

#### The open() Function

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

**📁 Practice Location:** `04-files/file_practice.py`

**What to Practice:**

- Open configuration files for reading
- Understand different file modes
- Practice proper file closing

#### The with open() Function

`with open()` is the context-manager way to work with files so they close automatically—even if errors happen. Use it to read or write cleanly:

```python
# read
with open("inventory/devices.txt", "r", encoding="utf-8") as f:
    hosts = [line.strip() for line in f if line.strip()]

# write
with open("outputs/results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(hosts))
```

**📁 Practice Location:** `04-files/file_practice.py`

**What to Practice:**

- Use with statements for automatic file handling
- Read configuration templates
- Understand why this is the preferred method

**Challenge:** Read a device configuration template and replace placeholders with actual values

#### Create, Read, and Append

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

**📁 Practice Location:** `04-files/file_practice.py`

**What to Practice:**

- Create new configuration files
- Read existing device configurations
- Append log entries to monitoring files
- Practice with different file modes

---

### Section 05: Error Handling with try...except

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
python error_practice.py
```

**Scenarios to Practice:**

- Device connection timeout
- Invalid configuration syntax  
- File permission errors
- Network unreachable errors

---

### Section 06: Working with Data Formats

Master the 4 essential data formats used in network automation! Each format has specific strengths for different network automation tasks.

#### Practice Structure

Each format has its own focused directory with TODO-driven exercises:

**📁 `json_examples/`** - Network API data practice

- `devices.json` - Simple device inventory
- `json_practice.py` - TODO exercises for JSON mastery
- Learn: API responses, device filtering, JSON creation

**📁 `csv_examples/`** - Spreadsheet data practice  

- `devices.csv` - Device inventory with status
- `csv_practice.py` - TODO exercises for CSV mastery
- Learn: Reports, summaries, bulk operations

**📁 `yaml_examples/`** - Configuration file practice

- `network.yaml` - Network configuration structure
- `yaml_practice.py` - TODO exercises for YAML mastery
- Learn: Configs, automation scripts, infrastructure as code

**📁 `xml_examples/`** - Legacy system data practice

- `network.xml` - Structured enterprise data  
- `xml_practice.py` - TODO exercises for XML mastery
- Learn: Enterprise systems, SOAP APIs, complex structures

#### Quick Start

```bash
cd 06-data-formats/json_examples
python json_practice.py
```

Each practice script contains TODO exercises that build from basic reading to advanced manipulation. Complete the TODOs to make the code work and master each format!

---

## 📝 Notes for Success

- **Practice Regularly:** Run each example and modify it to understand the concepts
- **Experiment:** Change parameters and see what happens
- **Build Incrementally:** Start with simple examples and add complexity
- **Use the Debugger:** Step through code to understand execution flow
- **Ask Questions:** If something doesn't work as expected, investigate why

**Remember:** This is practice - make mistakes, break things, and learn from the experience!

## 🔗 Additional Resources

- Practice data files are located in each format's directory (`06-data-formats/*/`)
- Configuration templates are in the `templates/` directory  
- Each module has focused README and practice files
- Challenge solutions are in the `solutions/` directory (try the challenges first!)

Good luck with your network automation journey! 🚀
