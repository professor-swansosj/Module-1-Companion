# 05: Error Handling - Make Your Code Bulletproof

Network automation breaks ALL THE TIME! Learn to handle errors gracefully so your scripts keep running when things go wrong.

## 🎯 What You'll Master

Error handling is like having a safety net for your code. When something breaks (and it will!), your program can catch the error and handle it instead of crashing.

### 🔧 Core Concepts You'll Practice

#### 1. **The Try-Except Pattern**

This is your safety net! Try to do something, but if it fails, catch the error:

```python
try:
    # Code that might break
    result = 10 / 0  # This will cause an error!
except ZeroDivisionError:
    # Handle the specific error
    print("Can't divide by zero!")
```

#### 2. **Finding Error Names**

When your code crashes, Python tells you exactly what went wrong! Look at the error message:

```bash
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

The error name is `ZeroDivisionError` - use this in your except block!

#### 3. **Handling Different Errors**

Different things break in different ways. Handle each one specifically:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

#### 4. **Always Clean Up with Finally**

Some code needs to run no matter what happens (like closing files):

```python
try:
    file = open("config.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always close the file!
```

## 🚀 Real-World Network Problems

**Why This Matters:** Network automation fails constantly!

- **Device offline** → `ConnectionError`
- **Wrong password** → `AuthenticationError`
- **File missing** → `FileNotFoundError`
- **Invalid IP** → `ValueError`
- **Timeout** → `TimeoutError`

**Professional Example:**

```python
def backup_device(hostname):
    try:
        # Try to connect and backup
        connect_to_device(hostname)
        config = get_running_config()
        save_backup(config)
        print(f"✅ {hostname} backup successful!")
    except ConnectionError:
        print(f"❌ {hostname} is offline - skipping")
    except FileNotFoundError:
        print(f"❌ Can't save backup for {hostname}")
    except Exception as e:
        print(f"❌ Unexpected error on {hostname}: {e}")
```

## 🎮 Your Coding Mission

In `error_practice.py`, you'll learn to handle errors step by step:

1. **Start Simple** - Handle basic math and input errors
2. **File Problems** - Deal with missing files and permissions
3. **Network Issues** - Handle connection and timeout errors
4. **Multiple Devices** - Keep going when some devices fail

## 💡 How to Find Error Names

**When your code crashes, Python tells you the error name:**

```bash
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

**Error name:** `FileNotFoundError` ← Use this in except!

```bash
ConnectionError: [Errno 111] Connection refused
```

**Error name:** `ConnectionError` ← Use this in except!

**Common Network Automation Errors:**

- `FileNotFoundError` - File doesn't exist
- `PermissionError` - Can't read/write file
- `ConnectionError` - Can't connect to device  
- `TimeoutError` - Operation took too long
- `ValueError` - Invalid data format
- `KeyError` - Missing dictionary key

## 🏆 Success Criteria

After completing the exercises, you'll be able to:

- ✅ Use try-except blocks to catch and handle errors
- ✅ Find error names from Python tracebacks
- ✅ Handle multiple error types in one function
- ✅ Use finally blocks for cleanup operations
- ✅ Write network automation that continues running when devices fail

Ready to make your code unbreakable? Let's handle some errors! 🚀
