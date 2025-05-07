from typing import List, Dict, Optional, Any
from src.SettingsTypes import SettingsTypes
from src.VM.interface import Interface

class VM:
    """
    A virtual machine class that handles network interfaces and message processing.

    This class represents a virtual machine that can have multiple network interfaces,
    manage connections with neighbor interfaces, and handle message processing.

    Attributes:
        interfaces (List[Interface]): List of network interfaces attached to this VM.
        neighbor_interfaces (List[Interface]): List of interfaces connected to this VM's interfaces.
        domain_name_mappings (Dict[str, str]): DNS mappings for name resolution.
        memory_buffer (Optional[Dict[str, Any]]): Temporary storage for messages.
        name (str): Name identifier for the VM.
    """

    def __init__(self, name: str = "") -> None:
        """Initialize a new VM instance with empty interfaces and configurations."""
        self.__interfaces: List[Interface] = []
        self.__neighbor_interfaces: List[Interface] = []
        self.__domain_name_mappings: Dict[str, str] = {}
        self.__memory_buffer: Optional[Dict[str, Any]] = None
        self.__name: str = name

    @property
    def interfaces(self) -> List[Interface]:
        """Get the list of interfaces."""
        return self.__interfaces

    @property
    def neighbor_interfaces(self) -> List[Interface]:
        """Get the list of neighbor interfaces."""
        return self.__neighbor_interfaces

    @property
    def domain_name_mappings(self) -> Dict[str, str]:
        """Get the DNS mappings dictionary."""
        return self.__domain_name_mappings

    @property
    def memory_buffer(self) -> Optional[Dict[str, Any]]:
        """Get the memory buffer contents."""
        return self.__memory_buffer

    @memory_buffer.setter
    def memory_buffer(self, value: Optional[Dict[str, Any]]) -> None:
        """Set the memory buffer contents."""
        self.__memory_buffer = value

    @property
    def name(self) -> str:
        """Get the VM name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Set the VM name."""
        self.__name = value

    def bind_to_interface(self, interface: Interface) -> None:
        """
        Bind a network interface to this VM.

        Args:
            interface: The network interface object to bind to this VM.
        """
        interface.bind_to_vm(self)
        self.__interfaces.append(interface)

    def connect_interface_to_neighbor(self, interface_index: int, pair_interface: Interface) -> None:
        """
        Connect one of this VM's interfaces to a neighbor interface.

        Args:
            interface_index: Index of the local interface to connect.
            pair_interface: The neighbor interface to connect to.

        Raises:
            IndexError: If the interface_index is negative or exceeds the number of interfaces.
        """
        if interface_index < 0:
            raise IndexError("Interface index is less than 0")

        if interface_index >= len(self.__interfaces):
            raise IndexError("Interface not found by index")

        self.__interfaces[interface_index].connect_to_neighbor(pair_interface)
        self.__neighbor_interfaces.append(pair_interface)

    def load_message(self, message: Dict[str, Any]) -> None:
        """
        Load a message into the VM's memory buffer.

        Args:
            message: The message to load into memory.
        """
        self.memory_buffer = message

    def interpret(self) -> None:
        """
        Interpret the message in the memory buffer and configure host settings.

        This method processes the loaded message to configure various host settings
        including interface configurations and DNS parameters.
        """
        if self.__memory_buffer is None:
            return

        host_settings = self.__memory_buffer.values()
        for setting in host_settings:
            if not setting["interfaces"]:
                continue
            for interface in self.__interfaces:
                interface_settings = setting["interfaces"].get(interface.name)
                if interface_settings is None:
                    continue
                SettingsTypes.interpret_dns_params(self, interface_settings)
                interface.interpret(interface_settings)

    def send(self, message: Dict[str, Any], source_interface: Optional[Interface] = None) -> None:
        """
        Send a message through a specified interface or the default first interface.

        Args:
            message: The message to send.
            source_interface: The interface to send the message through. If None,
                            uses the first interface. Defaults to None.
        """
        if source_interface is None:
            source_interface = self.__interfaces[0]
        source_interface.send(message)

    def flush_memory(self) -> None:
        """Clear the memory buffer."""
        self.memory_buffer = None