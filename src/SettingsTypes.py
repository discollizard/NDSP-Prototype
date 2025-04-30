class SettingsTypes:

    def __new__(cls):
        raise TypeError("This class cannot be instantiated")

    @staticmethod
    def interpret_dns_params(vm, interface_params):
        if interface_params.get('host_name') and interface_params.get('ipv4_addr'):
            vm.domain_name_mappings[interface_params['host_name']] = interface_params['ipv4_addr']
        pass