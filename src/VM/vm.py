from src.SettingsTypes import SettingsTypes

class VM:
    """
    A virtual machine class that handles network interfaces and message processing.

    This class represents a virtual machine that can have multiple network interfaces,
    manage connections with neighbor interfaces, and handle message processing.

    Attributes:
        interfaces (list): List of network interfaces attached to this VM.
        neighbor_interfaces (list): List of interfaces connected to this VM's interfaces.
        domain_name_mappings (dict): DNS mappings for name resolution.
        memory_buffer (object): Temporary storage for messages.
        name (str): Name identifier for the VM.
    """

    def __init__(self):
        """Initialize a new VM instance with empty interfaces and configurations."""
        self.interfaces = []
        self.neighbor_interfaces = []
        self.domain_name_mappings = {}
        self.memory_buffer = None
        self.name = ""

    def set_vm_name(self, name):
        """
        Set the name of the virtual machine.

        Args:
            name (str): The name to assign to this VM.
        """
        self.name = name

    def bind_to_interface(self, interface):
        """
        Bind a network interface to this VM.

        Args:
            interface: The network interface object to bind to this VM.
        """
        interface.bind_to_vm(self)
        self.interfaces.append(interface)

    def connect_interface_to_neighbor(self, interface_index, pair_interface):
        """
        Connect one of this VM's interfaces to a neighbor interface.

        Args:
            interface_index (int): Index of the local interface to connect.
            pair_interface: The neighbor interface to connect to.

        Raises:
            IndexError: If the interface_index is negative or exceeds the number of interfaces.
        """
        if interface_index < 0:
            raise IndexError("Interface index is less than 0")

        if interface_index >= len(self.interfaces):
            raise IndexError("Interface not found by index")

        self.interfaces[interface_index].connect_to_neighbor(pair_interface)
        self.neighbor_interfaces.append(pair_interface)

    def load_message(self, message):
        """
        Load a message into the VM's memory buffer.

        Args:
            message: The message to load into memory.
        """
        self.memory_buffer = message

    def interpret(self):
        """
        Interpret the message (parsed JSON object) in the memory buffer and configure host settings.

        This method processes the loaded message to configure various host settings
        including interface configurations and DNS parameters.
        """
        host_settings = self.memory_buffer.values()
        for setting in host_settings:
            if not setting["interfaces"]:
                pass
            interface_settings = setting["interfaces"].values()
            for param in interface_settings:
                SettingsTypes.interpret_dns_params(self, param)

    def send(self, message, source_interface=None):
        """
        Send a message through a specified interface or the default first interface.

        Args:
            message: The message to send.
            source_interface: The interface to send the message through. If None,
                            uses the first interface. Defaults to None.
        """
        if source_interface is None:
            source_interface = self.interfaces[0]
        source_interface.send(message)

    def flush_memory(self):
        self.memory_buffer = None