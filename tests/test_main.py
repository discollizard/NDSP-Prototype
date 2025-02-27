import unittest
import os
import json
from ndcp_prototype.ndcp_base_node import NDCPBaseNode

class TestNDCPNode(unittest.TestCase):
    def test_acyclical_topology_matching_interfaces(self):
        node1 = NDCPBaseNode("11-11-11-11-11-11")
        node2 = NDCPBaseNode("22-22-22-22-22-22")
        node3 = NDCPBaseNode("33-33-33-33-33-33")

        node1.adjacent_nodes = [node2, node3]
        node2.adjacent_nodes = [node1]
        node3.adjacent_nodes = [node1]

        node1.interfaces = {
            "fa0/1": {
                "ip_addr": "192.168.0.10",
                "subnet_mask": "255.255.255.0",
                "is_up": True
            },
        }

        current_directory = os.getcwd()
        case_file_path = os.path.join(current_directory, 'tests/cases/acyclical_topology.json')
        with open(case_file_path, 'r') as file:
            data = json.load(file)
            node1.forward_msg(node1, data)
            # print(json.dumps(node1.to_dict(), indent=4))

        self.assertEqual(node1.host_name, "Switch1")
        self.assertEqual(node1.interfaces, {
            "fa0/1": {
                "ip_addr": "192.168.0.10",
                "subnet_mask": "255.255.255.0",
                "is_up": True
            },
        })

if __name__ == '__main__':
    unittest.main()