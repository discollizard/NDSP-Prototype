import random

class Interface:
    def __init__(self, mac="", ip=""):
        if len(mac) == 0 :
            mac = self._generate_random_mac()
        self.mac = mac
        self.ip = ip
        self.neighbor = None
        self.vm = None

    @staticmethod
    def _generate_random_mac():
        return "-".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    def bind_to_vm(self, vm):
        self.vm = vm

    def set_ip(self, ip):
        self.ip = ip

    def connect_to_neighbor(self, pair_interface):
        self.neighbor = pair_interface

        #connect back to source
        if self.neighbor.neighbor is None:
            self.neighbor.connect_to_neighbor(self)

    def send(self, message):
        self.neighbor.receive(message)

    def receive(self, message):
        self.vm.memory_buffer = message
