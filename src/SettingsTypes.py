class SettingsTypes:

    def __new__(cls):
        raise TypeError("This class cannot be instantiated")

    @staticmethod
    def interpret_dns_params(vm, interface_params):
        if interface_params.get('host_name') and interface_params.get('ipv4_addr'):
            vm.domain_name_mappings[interface_params['host_name']] = interface_params['ipv4_addr']

    @staticmethod
    def interpret_ipv4_params(interface, interface_params):
        if interface_params.get('ipv4_addr'):
            interface.ip = interface_params['ipv4_addr']
        if interface_params.get('subnet_mask'):
            interface.subnet_mask = interface_params['subnet_mask']
        if interface_params.get('default_gateway'):
            interface.default_gateway = interface_params['default_gateway']
        if interface_params.get('is_up'):
            interface.is_up = interface_params['is_up']
