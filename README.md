# NDSP - Network Device Settings Protocol (Prototype)
A prototype for an open protocol designed to automatically configure network devices.

## Basic overview
### Format
The format used is a JSON object indexed by MAC addresses, in which a network device can access its settings in constant time, and configure itself based on the specs received.

### Example

```
{
    "11-11-11-11-11-11": {
        "host_name": "Router1",
        "type": "router",
        "interfaces": {
            "fa0/1": {
                "ip_addr": "192.168.0.10",
                "subnet_mask": "255.255.255.0",
                "is_up": true
            },
            "fa0/2": {
                "ip_addr": "192.168.0.11",
                "subnet_mask": "255.255.255.0",
                "is_up": true
            }
        }
    }
}
```

## About the prototype
Is is written in Python and it uses a graph data structure to emulate the behaviour of devices inside a network. There are no platform-specific implementations yet. All the settings are portrayed as state inside the NDCPNode classes.