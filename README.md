# NDSP - Network Device Settings Protocol (Prototype)
A prototype for an open protocol designed to automatically configure network devices.

## Basic overview
### Format
The format used is a JSON object indexed by MAC addresses, in which a network device can access its settings directly, and configure itself based on the specs received.

### Example

```
{
    "11-11-11-11-11-11": {
        "type": "router",
        "interfaces": {
            "fa0/1": {
                "ip_addr": "192.168.0.10",
                "subnet_mask": "255.255.255.0",
                "dns_server": "192.168.2.1",
                "is_up": true
            },
            "fa0/2": {
                "ip_addr": "192.168.0.11",
                "subnet_mask": "255.255.255.0",
                "dns_server": "192.168.2.1",
                "is_up": true
            }
        }
    }
}
```

## About the prototype
It is written in Python, and it simulates the configuration of devices inside a network. There are no platform-specific
implementations yet. As of now, All the machines' settings are portrayed as state inside the VM and Interface classes.

## Next steps
~~Address name resolution on the sending VM;~~
- Address name resolution on the receiving VM;
- Address documentation of classes;
- Implement the VM and interface settings mutation logic;
- Address security;
- Address message splitting (whole network vs single updates);
- Address implementation;
- Address extended options (router and switching stuff);
