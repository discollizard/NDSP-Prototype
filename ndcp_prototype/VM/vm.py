class VM:
    def __init__(self):
        self.interfaces = []
        self.neighbor_interfaces = []
        self.memory_buffer = None

    def set_vm_name(self, name):
        self.name = name

    def bind_to_interface(interface):
        self.neighbor_interfaces.append(interface)

    def send(self, source_interface, message):
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




        
