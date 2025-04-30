import pytest
import json
from src.VM.interface import Interface
from src.VM.vm import VM
from pathlib import Path

# Fixtures for setup
@pytest.fixture
def mock_vm():
    vm = VM()
    interface1 = Interface("11-11-11-11-11-11")
    vm.bind_to_interface(interface1)
    return vm

@pytest.fixture
def mock_vm2():
    vm2 = VM()
    interface_vm2 = Interface("ae-ff-01-fc-12-23")
    vm2.bind_to_interface(interface_vm2)
    return vm2

@pytest.fixture
def two_way_params():
    config_path = Path("tests/cases/two_way.json")
    with open(config_path) as f:
        return json.load(f)

# Test Initialization of VM
def test_init():
    generic_vm = VM()

    assert all([
        generic_vm.interfaces == [],
        generic_vm.neighbor_interfaces == [],
        generic_vm.memory_buffer is None,
        generic_vm.name == ""
    ])

def test_load_message(mock_vm, two_way_params):
    mock_vm.load_message(two_way_params)
    assert mock_vm.memory_buffer == two_way_params

# Test setting VM name
def test_set_vm_name(mock_vm):
    mock_vm.set_vm_name("Test 1")
    assert mock_vm.name == "Test 1"

# Test binding interface to VM
def test_bind_to_interface(mock_vm):
    interface2 = Interface("22-22-22-22-22-22")
    mock_vm.bind_to_interface(interface2)
    assert mock_vm.interfaces[1].mac == "22-22-22-22-22-22"

def test_interpret(mock_vm, two_way_params):
    mock_vm.load_message(two_way_params)
    mock_vm.interpret()
    assert all([
        mock_vm.domain_name_mappings.get("server.test") == "192.168.2.12",
        mock_vm.domain_name_mappings.get("web.test") == "192.168.2.15",
    ])
    # Sending data

# Test send method (with error handling)
def test_send(mock_vm, mock_vm2, two_way_params):
    with pytest.raises(IndexError):
        mock_vm.connect_interface_to_neighbor(-1, mock_vm2.interfaces[0])
        mock_vm.connect_interface_to_neighbor(1, mock_vm2.interfaces[0])

    # Connect interfaces properly
    mock_vm.connect_interface_to_neighbor(0, mock_vm2.interfaces[0])

    # Sending data
    mock_vm.send(two_way_params)
    assert mock_vm2.memory_buffer == two_way_params
