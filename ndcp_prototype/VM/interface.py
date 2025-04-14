class Interface:
    def __init__(self, mac, ip="", host_name=""):
        self.mac = mac
        self.neighbor = None
        self.vm = None

    def bind_to_vm(self, vm):
        self.vm = vm
        self.vm.interfaces.append(self)
    
    def set_ip(self, ip):
        self.ip = ip

    def set_host_name(self, host_name):
        self.host_name = host_name

    def connect_to_neighbor(self, pair_interface):
        self.neighbor = pair_interface
        self.vm.neighbor_interfaces.append(pair_interface)

    def receive(self, message):
        self.vm.memory_buffer = message

    def send(self, message):
        self.neighbor.receive(message)