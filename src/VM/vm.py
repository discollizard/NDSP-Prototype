from src.SettingsTypes import SettingsTypes

class VM:
    def __init__(self):
        self.interfaces = []
        self.neighbor_interfaces = []
        self.domain_name_mappings = {}
        self.memory_buffer = None
        self.name = ""

    def set_vm_name(self, name):
        self.name = name

    def bind_to_interface(self, interface):
        interface.bind_to_vm(self)
        self.interfaces.append(interface)

    def connect_interface_to_neighbor(self, interface_index, pair_interface):
        if interface_index < 0:
            raise IndexError("Interface index is less than 0")

        if interface_index >= len(self.interfaces):
            raise IndexError("Interface not found by index")

        self.interfaces[interface_index].connect_to_neighbor(pair_interface)
        self.neighbor_interfaces.append(pair_interface)

    def load_message(self, message):
        self.memory_buffer = message

    def interpret(self):
        host_settings = self.memory_buffer.values()
        for setting in host_settings:
            # set other host stuff here...
            if not setting["interfaces"]:
                pass
            interface_settings = setting["interfaces"].values()
            for param in interface_settings:

                #set other interface stuff here

                # name bindings
                SettingsTypes.interpret_dns_params(self, param)

    def send(self, message, source_interface=None):
        if source_interface is None:
            source_interface = self.interfaces[0]
        source_interface.send(message)

    # def send_message_unicast(self, source_interface, message, destination_ip):
    #     ip_is_in_arp = False
    #     destination_interface = None

    #     for interface in neighbor_interfaces:
    #         if destination_ip == interface.ip:

    #             ip_is_in_arp = True

    #     if not ip_is_in_arp:
    #         print("\n From "+self.name+": ip " + destination_ip + " is not reachable")
    #         return
    
    #     source_interface.send(message, destination_interface)