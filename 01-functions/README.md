# 01: Function Basics - Your Network Automation Toolkit

## 🎯 Mission

Learn to write helpful functions for network automation - like connecting to devices and configuring interfaces!

## 📚 What Are Functions?

Functions are like tools in your network automation toolkit. Instead of writing the same code over and over, you create a function once and use it everywhere!

Think of it like this: Instead of manually typing connection commands every time, you create a `connect_device()` function that does it for you.

## 🔧 Function Building Blocks

### 1. Basic Functions

```python
def connect_device(hostname):
    print(f"Connecting to {hostname}...")
```

- **def** starts your function
- **hostname** is a parameter (input)
- The code inside does the work

### 2. Functions with Default Values

```python
def configure_interface(device, interface, ip, mask="255.255.255.0"):
    # mask has a default value - you don't always need to provide it!
```

This is super useful for network automation because most subnets use /24 masks.

### 3. Multiple Arguments (*args)

```python
def configure_multiple_devices(*devices):
    for device in devices:
        print(f"Configuring {device}")
```

The `*` lets you pass as many devices as you want!

### 4. Keyword Arguments (**kwargs)  

```python
def setup_network(**settings):
    for setting, value in settings.items():
        print(f"{setting}: {value}")
```

The `**` lets you pass named settings like `dns="8.8.8.8"`.

## 🎖 Your Learning Goals

- [ ] Write simple functions with parameters
- [ ] Use default values for common network settings
- [ ] Handle multiple devices with *args
- [ ] Use flexible configuration with **kwargs
- [ ] Make functions that network engineers love to use!

## 💡 Pro Tips for Network Functions

- **Use clear names**: `connect_device()` not `conn()`
- **Add default values**: Most networks use common settings
- **Think like a network engineer**: What would make your job easier?
- **Test with real scenarios**: Try different device types and configurations

## 🚀 Ready to Practice?

**Start here:** Open `function_basics.py` and work through each TODO step by step. The comments will guide you!

**Next level:** Try `function_challenge.py` for bonus exercises that will make you a function master!

## 🎯 Success Tips

1. Read each function's docstring to understand what it should do
2. Look at the test code in `main()` to see how functions should work
3. Start with simple print statements, then add more features
4. Don't worry about perfection - focus on making it work first!

You've got this! Functions are the foundation of great network automation! 🚀
