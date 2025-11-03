# 06: Data Formats - Working with Network Information

Learn to read and write the four (4) most common data formats in network automation. Each format has its strengths - master them all!

## 🎯 What You'll Master

Data formats are different ways to store and organize information. Think of them like different languages for computers to share network data.

### � The Big Four Data Formats

#### 1. **JSON - JavaScript Object Notation**

**What it's for:** APIs, web services, modern network controllers  
**Looks like:** Lists and dictionaries with quotes around everything

```json
{
  "hostname": "router1", 
  "ip": "192.168.1.1",
  "type": "router",
  "ports": ["gi0/0", "gi0/1"]
}
```

#### 2. **CSV - Comma Separated Values**  

**What it's for:** Spreadsheets, device lists, reports, bulk imports
**Looks like:** Rows and columns separated by commas

```csv
hostname,ip,type,location
router1,192.168.1.1,router,closet-a
switch1,192.168.1.2,switch,closet-b
```

#### 3. **YAML - YAML Ain't Markup Language**

**What it's for:** Configuration files, automation scripts, human-readable configs
**Looks like:** Organized with spaces and dashes (no quotes needed!)

```yaml
devices:
  - hostname: router1
    ip: 192.168.1.1
    type: router
  - hostname: switch1  
    ip: 192.168.1.2
    type: switch
```

#### 4. **XML - eXtensible Markup Language**

**What it's for:** Legacy systems, enterprise tools, structured documents  
**Looks like:** Tags with angle brackets (like HTML)

```xml
<devices>
  <device>
    <hostname>router1</hostname>
    <ip>192.168.1.1</ip>
  </device>
</devices>
```

## 🚀 Real-World Applications

**Where You'll See These:**

- **JSON:** REST APIs, network controller responses, modern automation tools
- **CSV:** Excel files, device inventories, monitoring reports
- **YAML:** Ansible playbooks, Docker configs, infrastructure as code
- **XML:** Legacy network management systems, SOAP APIs, configuration backups

**Professional Example:**

```python
# Read device list from CSV
devices = load_csv("device_inventory.csv")

# Get current config from each device (returns JSON)
for device in devices:
    config = get_device_config(device['ip'])  # JSON response
    
# Save configs in YAML format (human readable)
save_yaml("backup_configs.yaml", all_configs)
```

## 🎮 Your Coding Mission

Each format has its own directory with practice scripts and data files:

### 📁 `json_examples/`

- **`devices.json`** - Simple network device data (API format)
- **`json_practice.py`** - TODO exercises for JSON mastery
- Learn: Reading APIs, filtering data, creating JSON responses

### 📁 `csv_examples/`

- **`devices.csv`** - Device inventory with status (spreadsheet format)
- **`csv_practice.py`** - TODO exercises for CSV mastery
- Learn: Processing reports, creating summaries, bulk operations

### 📁 `yaml_examples/`

- **`network.yaml`** - Network configuration (human-readable format)
- **`yaml_practice.py`** - TODO exercises for YAML mastery
- Learn: Config files, automation scripts, infrastructure as code

### 📁 `xml_examples/`

- **`network.xml`** - Legacy system data (structured format)
- **`xml_practice.py`** - TODO exercises for XML mastery
- Learn: Enterprise systems, SOAP APIs, complex data structures

## 💡 Format Comparison

| Format | Human Readable | File Size | Parsing Speed | Use Case |
|--------|---------------|-----------|---------------|----------|
| JSON   | Good          | Medium    | Fast          | APIs, Modern Tools |
| CSV    | Excellent     | Small     | Very Fast     | Spreadsheets, Reports |
| YAML   | Excellent     | Medium    | Medium        | Config Files |
| XML    | Good          | Large     | Slower        | Enterprise Systems |

## 🏆 Success Criteria

After completing all format exercises, you'll be able to:

- ✅ Read and write JSON data from network APIs
- ✅ Process CSV files with device inventories and reports
- ✅ Create and modify YAML configuration files  
- ✅ Parse XML data from network management systems
- ✅ Choose the right format for different network automation tasks

Ready to become fluent in all data formats? Let's start parsing! 🚀
