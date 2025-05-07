from typing import Optional, Dict, Any
import random
from src.SettingsTypes import SettingsTypes

class Interface:
    """
    A network interface class that represents a network adapter with MAC and IP addresses.

    This class handles network interface operations including binding to virtual machines,
    establishing neighbor connections, and message transmission.

    Attributes:
        mac (str): MAC address of the interface. Auto-generated if not provided.
        ip (str): IP address of the interface.
        name (str): Interface name.
        neighbor (Interface): Reference to the connected neighbor interface.
        vm (VM): Reference to the virtual machine this interface is bound to.
        default_gateway (str): Default gateway for the interface.
        subnet_mask (str): Subnet mask for the interface.
        is_up (bool): Interface status flag indicating if it's up (True) or down (False).
    """

    def __init__(self, mac: str = "", ip: str = "", name: str = "") -> None:
        if len(mac) == 0:
            mac = self._generate_random_mac()
        self.mac: str = mac
        self.__ip: str = ip
        self.__default_gateway: str = ""
        self.__subnet_mask: str = ""
        self.__is_up: bool = False

        if len(name) == 0:
            name = self._generate_random_name()
        self.name: str = name

        self.__neighbor: Optional['Interface'] = None
        self.__vm: Optional['VM'] = None

    @property
    def ip(self) -> str:
        """Get the IP address of the interface."""
        return self.__ip

    @ip.setter
    def ip(self, value: str) -> None:
        """Set the IP address of the interface."""
        self.__ip = value

    @property
    def neighbor(self) -> Optional['Interface']:
        """Get the neighbor interface."""
        return self.__neighbor

    @neighbor.setter
    def neighbor(self, value: Optional['Interface']) -> None:
        """Set the neighbor interface."""
        self.__neighbor = value

    @property
    def vm(self) -> Optional['VM']:
        """Get the virtual machine reference."""
        return self.__vm

    @vm.setter
    def vm(self, value: Optional['VM']) -> None:
        """Set the virtual machine reference."""
        self.__vm = value

    @property
    def default_gateway(self) -> str:
        """Get the default gateway address."""
        return self.__default_gateway

    @default_gateway.setter
    def default_gateway(self, value: str) -> None:
        """Set the default gateway address."""
        self.__default_gateway = value

    @property
    def subnet_mask(self) -> str:
        """Get the subnet mask of the interface."""
        return self.__subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, value: str) -> None:
        """Set the subnet mask of the interface."""
        self.__subnet_mask = value

    @property
    def is_up(self) -> bool:
        """Get the interface status."""
        return self.__is_up

    @is_up.setter
    def is_up(self, value: bool) -> None:
        """Set the interface status."""
        self.__is_up = value

    @staticmethod
    def _generate_random_mac() -> str:
        """Generate a random MAC address."""
        return "-".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    @staticmethod
    def _generate_random_name() -> str:
        """Generate a random interface name."""
        identifier = ''.join(str(random.randint(0, 9)) for _ in range(4))
        return f"if{identifier}"

    def bind_to_vm(self, vm: 'VM') -> None:
        """
        Bind this interface to a virtual machine.

        Args:
            vm: The virtual machine instance to bind this interface to.
        """
        self.vm = vm

    def connect_to_neighbor(self, pair_interface: 'Interface') -> None:
        """
        Connect this interface to a neighbor interface.

        Args:
            pair_interface: The neighbor interface to connect to.
        """
        self.neighbor = pair_interface

        if pair_interface.neighbor is None:
            pair_interface.connect_to_neighbor(self)

    def send(self, message: Dict[str, Any]) -> None:
        """
        Send a message to the connected neighbor interface.

        Args:
            message: The message to send to the neighbor interface.
        """
        if self.__neighbor is None:
            raise ValueError("No neighbor interface connected")
        self.__neighbor.receive(message)

    def receive(self, message: Dict[str, Any]) -> None:
        """
        Receive a message from a neighbor interface.

        Args:
            message: The message received from the neighbor interface.
        """
        if self.__vm is None:
            raise ValueError("No VM bound to interface")
        self.__vm.load_message(message)
        self.__vm.interpret()

    def interpret(self, interface_settings: Dict[str, Any]) -> None:
        """
        Interpret and apply interface settings.

        Args:
            interface_settings: Dictionary containing interface configuration parameters.
        """
        SettingsTypes.interpret_ipv4_params(self, interface_settings)