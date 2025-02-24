class NDCPNode:
    def __init__(self, mac):
        self.visited = False
        self.mac_addr = mac
        self.host_name = None
        self.interfaces = {}
        self.adjacent_nodes = []
    
    def forward_msg(self, node, msg):
        if node.visited is True:
            return
        node.visited = True
        if(msg[node.mac_addr]):
            # access internal OS APIs and change their settings (platform-specific implementation)
            node.host_name = msg[node.mac_addr]['host_name']

            localInterfaceKeys = node.interfaces.keys()

            for interface_id in localInterfaceKeys:
                interface_to_set = msg[node.mac_addr]['interfaces'].get(interface_id)
                if  interface_to_set != None:
                    node.interfaces[interface_id]['ip_addr'] =  msg[node.mac_addr]['interfaces'][interface_id]['ip_addr']
                    node.interfaces[interface_id]['subnet_mask'] =  msg[node.mac_addr]['interfaces'][interface_id]['subnet_mask']
                    node.interfaces[interface_id]['is_up'] =  msg[node.mac_addr]['interfaces'][interface_id]['is_up']
        for adj_node in node.adjacent_nodes:
            if not adj_node.visited:
                node.forward_msg(adj_node, msg)

    def to_dict(self):
        return {
            "visited": self.visited,
            "mac_addr": self.mac_addr,
            "host_name": self.host_name,
            "interfaces": self.interfaces,
            # "adjacent_nodes": self.adjacent_nodes,
        }