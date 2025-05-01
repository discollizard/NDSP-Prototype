import random

class Interface:
    """
    A network interface class that represents a network adapter with MAC and IP addresses.

    This class handles network interface operations including binding to virtual machines,
    establishing neighbor connections, and message transmission.

    Attributes:
        mac (str): MAC address of the interface. Auto-generated if not provided.
        ip (str): IP address of the interface.
        neighbor (Interface): Reference to the connected neighbor interface.
        vm (VM): Reference to the virtual machine this interface is bound to.
    """

    def __init__(self, mac="", ip=""):
        """
        Initialize a new network interface.

        Args:
            mac (str, optional): MAC address for the interface. If not provided,
                               a random MAC address will be generated.
            ip (str, optional): IP address for the interface.
        """
        if len(mac) == 0:
            mac = self._generate_random_mac()
        self.mac = mac
        self.ip = ip
        self.neighbor = None
        self.vm = None

    @staticmethod
    def _generate_random_mac():
        """
        Generate a random MAC address.

        Returns:
            str: A randomly generated MAC address in the format 'xx-xx-xx-xx-xx-xx'
                where xx are hexadecimal values.
        """
        return "-".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    def bind_to_vm(self, vm):
        """
        Bind this interface to a virtual machine.

        Args:
            vm: The virtual machine instance to bind this interface to.
        """
        self.vm = vm

    def set_ip(self, ip):
        """
        Set the IP address for this interface.

        Args:
            ip (str): The IP address to assign to this interface.
        """
        self.ip = ip

    def connect_to_neighbor(self, pair_interface):
        """
        Connect this interface to a neighbor interface.

        This method establishes a bidirectional connection between two interfaces.
        If the neighbor interface isn't already connected back to this interface,
        it will establish the reverse connection.

        Args:
            pair_interface (Interface): The neighbor interface to connect to.
        """
        self.neighbor = pair_interface

        # Connect back to source if neighbor doesn't have a connection
        if self.neighbor.neighbor is None:
            self.neighbor.connect_to_neighbor(self)

    def send(self, message):
        """
        Send a message to the connected neighbor interface.

        Args:
            message: The message to send to the neighbor interface.
        """
        self.neighbor.receive(message)

    def receive(self, message):
        """
        Receive a message from a neighbor interface.

        This method loads the received message into the bound VM's memory buffer
        and triggers message interpretation.

        Args:
            message: The message received from the neighbor interface.
        """
        self.vm.load_message(message)
        self.vm.interpret()