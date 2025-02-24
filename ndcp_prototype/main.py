import json
from ndcp_node import NDCPNode

# node1 = NDCPNode("11-11-11-11-11-11")
# node2 = NDCPNode("22-22-22-22-22-22")
# node3 = NDCPNode("33-33-33-33-33-33")

# node1.adjacent_nodes = [node2, node3]
# node2.adjacent_nodes = [node1]
# node3.adjacent_nodes = [node1]

# node1.interfaces = {
#     "fa0/1": {
#         "ip_addr": None,
#         "subnet_mask": None,
#         "is_up": False
#     },
#     "fa0/3": {
#         "ip_addr": "192.168.0.12",
#         "subnet_mask": "255.255.255.0",
#         "is_up": True
#     },
#     "fa0/4": {
#         "ip_addr": "192.168.0.13",
#         "subnet_mask": "255.255.255.0",
#         "is_up": True
#     }, 
#     "g0/1": {
#         "ip_addr": "172.16.0.144",
#         "subnet_mask": "255.255.0.0",
#         "is_up": False
#     },
# }

# with open("case.json", 'r') as file:
#     data = json.load(file)
#     node1.forward_msg(node1, data)
    
#     print(json.dumps(node1.to_dict(), indent=4), json.dumps(node2.to_dict(), indent=4), json.dumps(node3.to_dict(), indent=4))