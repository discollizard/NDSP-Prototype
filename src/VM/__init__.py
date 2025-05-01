"""
This module houses the VM and Interface classes; two of the most important ones:

VM:
    A virtual machine class that simulates a network device with the ability to manage multiple
    network interfaces, handle message processing, and maintain network configurations. It supports
    operations like binding interfaces, connecting to neighbors, loading and interpreting messages,
    and maintaining DNS mappings.

Interface:
    A class representing a network interface with a MAC address that can be bound to a VM and
    connected to other interfaces. It enables network communication between VMs by providing
    capabilities to send and receive messages through connected interfaces.
"""
