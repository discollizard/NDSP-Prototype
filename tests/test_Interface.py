import json
from pathlib import Path
import pytest
import re
from src.VM.interface import Interface
from src.VM.vm import VM

# Test Initialization of Interface
@pytest.fixture
def mock_interface():
    return Interface()

@pytest.fixture
def mock_neighbor_interface():
    return Interface()

def test_init_with_autogenerated_mac_address():
    autogen_mac_interface = Interface()
    pattern = r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$'

    assert autogen_mac_interface.mac != "" and bool(re.match(pattern, autogen_mac_interface.mac))

def test_init_with_preset_mac_address():
    preset_mac_interface = Interface("11-11-11-11-11-11")
    assert preset_mac_interface.mac == "11-11-11-11-11-11"

def test_init_with_autogenerated_name():
    autogen_name_interface = Interface()
    pattern = r'^(if)[0-9]{4}$'

    assert autogen_name_interface.name != "" and bool(re.match(pattern, autogen_name_interface.name))

def test_init_with_preset_name():
    preset_mac_interface = Interface(name="if1234")
    assert preset_mac_interface.name == "if1234"

# Test binding to VM
@pytest.fixture
def vm_instance():
    return VM()

def test_bind_to_vm(vm_instance, mock_interface):
    mock_interface.bind_to_vm(vm_instance)
    assert mock_interface.vm is vm_instance

@pytest.fixture
def two_way_params():
    config_path = Path("tests/cases/two_way.json")
    with open(config_path) as f:
        return json.load(f)

def test_connect_to_neighbor(mock_interface, mock_neighbor_interface):
    mock_interface.connect_to_neighbor(mock_neighbor_interface)
    assert mock_interface.neighbor is mock_neighbor_interface

def test_send(mock_interface, mock_neighbor_interface, vm_instance, two_way_params):
    mock_neighbor_interface.bind_to_vm(vm_instance)
    mock_interface.connect_to_neighbor(mock_neighbor_interface)

    mock_interface.send(two_way_params)
    assert mock_neighbor_interface.vm.memory_buffer == two_way_params

def test_send_invalid(mock_interface, mock_neighbor_interface, vm_instance):
    mock_neighbor_interface.bind_to_vm(vm_instance)
    mock_interface.connect_to_neighbor(mock_neighbor_interface)

    with pytest.raises(Exception):
        mock_interface.send("test")

def test_receive(mock_interface, vm_instance, two_way_params):
    mock_interface.bind_to_vm(vm_instance)

    mock_interface.receive(two_way_params)
    assert mock_interface.vm.memory_buffer == two_way_params

def test_receive_invalid(mock_interface, vm_instance):
    mock_interface.bind_to_vm(vm_instance)

    with pytest.raises(Exception):
        mock_interface.receive("test")

def test_interpret(mock_interface, two_way_params):
    interface_settings_to_test = two_way_params["01-12-23-34-45-65"]["interfaces"]["eth1"]

    mock_interface.interpret(interface_settings_to_test)
    assert all([
        mock_interface.ip == "192.168.2.12",
        mock_interface.default_gateway == "192.168.2.1",
        mock_interface.subnet_mask == "255.255.255.0",
        mock_interface.is_up == True,
    ])
