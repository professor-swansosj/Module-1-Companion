# 🏗️ Classes & Objects - Network Device Modeling

Welcome to the world of object-oriented programming! Here you'll learn to model network devices as Python classes - the foundation of professional network automation.

## 🎯 What You'll Master

Classes are like blueprints for creating objects. Just like a blueprint defines what every house should have (rooms, doors, windows), a class defines what every network device should have (hostname, IP address, connection methods).

### � Core Concepts You'll Practice

#### 1. **Objects and Attributes**

Think of a network device - it has properties like hostname, IP address, device type. In Python:

```python
class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname      # Attribute
        self.ip_address = ip_address  # Attribute
```

#### 2. **Methods (Behaviors)**

Devices can do things - connect, disconnect, show config. These are methods:

```python
def connect(self):
    print(f"Connecting to {self.hostname}...")
    self.status = "connected"
```

#### 3. **Properties (Smart Attributes)**

Sometimes you want to control how data is stored and retrieved:

```python
@property
def ip_address(self):
    return self._ip_address

@ip_address.setter  
def ip_address(self, value):
    # Validate IP format before storing
    if self._is_valid_ip(value):
        self._ip_address = value
```

#### 4. **Inheritance (Device Families)**

Create specialized devices that inherit common features:

```python
class NetworkDevice:  # Parent class
    def connect(self): pass

class Router(NetworkDevice):  # Child class
    def show_routing_table(self): pass  # Unique to routers
    
class Switch(NetworkDevice):  # Child class  
    def show_vlans(self): pass  # Unique to switches
```

## 🚀 Real-World Applications

**Why This Matters:** Every major network automation framework uses classes:

- **Netmiko** - Device classes for different vendors
- **NAPALM** - Standardized device interfaces
- **Ansible** - Inventory objects and module classes

**Professional Example:**

```python
# Create device objects
router = Router("CORE-R1", "192.168.1.1", model="ISR4331")
switch = Switch("ACCESS-SW1", "192.168.1.2", ports=48)

# Use them consistently
for device in [router, switch]:
    device.connect()
    device.backup_config()
    device.disconnect()
```

## 🎮 Your Coding Mission

In `class_fundamentals.py`, you'll build a complete network device management system:

1. **Start Simple** - Create basic NetworkDevice class
2. **Add Intelligence** - Use properties for data validation  
3. **Build Families** - Create Router and Switch subclasses
4. **Go Advanced** - Implement vendor-specific devices with multiple inheritance

## 💡 Key Programming Concepts

**Classes vs Objects:**

- Class = Blueprint (defines what a device should have)
- Object = Actual device created from that blueprint

**Inheritance Benefits:**

- Code reuse (write common features once)
- Polymorphism (treat different devices the same way)
- Organization (logical hierarchy of device types)

**Properties Advantages:**

- Data validation (prevent invalid IPs)
- Computed values (calculate network addresses)
- Controlled access (read-only attributes)

## 🏆 Success Criteria

After completing the exercises, you'll be able to:

- ✅ Create classes that model real network infrastructure
- ✅ Use inheritance to build device hierarchies  
- ✅ Implement properties for smart data handling
- ✅ Design reusable, maintainable network automation code

Ready to master object-oriented network automation? Let's build some classes! 🚀
