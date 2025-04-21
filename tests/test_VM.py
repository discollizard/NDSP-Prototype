import pytest
from src.VM.interface import Interface
from src.VM.vm import VM

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

# Test Initialization of VM
def test_init():
    generic_vm = VM()
    assert generic_vm.interfaces == []
    assert generic_vm.neighbor_interfaces == []
    assert generic_vm.memory_buffer is None
    assert generic_vm.name == ""

# Test setting VM name
def test_set_vm_name(mock_vm):
    mock_vm.set_vm_name("Test 1")
    assert mock_vm.name == "Test 1"

# Test binding interface to VM
def test_bind_to_interface(mock_vm):
    interface2 = Interface("22-22-22-22-22-22")
    mock_vm.bind_to_interface(interface2)
    assert mock_vm.interfaces[1].mac == "22-22-22-22-22-22"

# Test send method (with error handling)
def test_send(mock_vm, mock_vm2):
    with pytest.raises(IndexError):
        mock_vm.connect_interface_to_neighbor(-1, mock_vm2.interfaces[0])
        mock_vm.connect_interface_to_neighbor(1, mock_vm2.interfaces[0])

    # Connect interfaces properly
    mock_vm.connect_interface_to_neighbor(0, mock_vm2.interfaces[0])

    # Sending data
    mock_vm.send("test")
    assert mock_vm2.memory_buffer == "test"
