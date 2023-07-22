from time import sleep
from typing import List, Any, Dict

from memory import Memory

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from enum import Enum

from memory import Literal, Address, AddressByRegister

# define Register type as union of float and int
Register = float | int
RegisterName = str
RegisterNames: [] = Enum('RegisterNames', 'r0 r1 r2 r3 cmp pc sp fp')


class VirtualMachine:
    verbose: bool
    instruction_pointer: int
    instructions: List[Any]  # TODO: circular dependency
    memory: Memory

    # Register name and value
    registers: Dict[str, Register]  # TODO: registerName store bits not floats

    def __init__(self, memory_size, verbose=False):
        self.memory = Memory(memory_size)
        self.registers = {'r0': 0, 'r1': 0, 'r2': 0, 'r3': 0,
                          'cmp': 0, 'pc': 0, 'sp': 0, 'fp': 0}
        self.instructions = []
        self.verbose = verbose

    def load_instructions(self, instructions):
        self.instructions = instructions

    def execute_next(self):
        if self.verbose:
            print("Executing instruction: ", self.registers['pc'])

        instruction = self.instructions[self.registers['pc']]
        instruction.execute(self)
        # if instruction is not a jump instruction, increment instruction pointer
        if not isinstance(instruction, Jump):
            self.registers['pc'] += 1
        sleep(1)

    def run(self):
        while self.registers['pc'] < len(self.instructions):
            self.execute_next()

        if self.verbose:
            print("Finished executing instructions")

    def set_instruction_pointer(self, instruction_pointer: Address | AddressByRegister):
        self.registers['pc'] = self.compute_address(instruction_pointer)

    def print_memory(self):
        # pretty print memory, address and value
        print("Printing memory")
        print("Address |\tValue")
        for i in range(len(self.memory.memory)):
            print(f"{i} |\t{self.memory.memory[i]}")

    def print_registers(self):
        # pretty print registers, id and value
        print("Printing registers")
        print("Id |\tValue")
        for i in range(len(self.registers)):
            print(f"{i} |\t{self.registers[i]}")

    def print_instructions(self):
        # pretty print instructions, opcode and operands
        print("Printing instructions")
        print("Opcode |\tOperands")
        for i in range(len(self.instructions)):
            print(f"{str(i)} |\t{self.instructions[i]}")

    def summary(self):
        print("Currently executing instruction: ", self.registers['pc'])
        print("Number of instructions: ", len(self.instructions))
        print("Number of registers: ", len(self.registers))
        print("Memory size: ", len(self.memory.memory))
        self.print_memory()
        self.print_registers()
        self.print_instructions()

    def compute_address(self, address: Address | AddressByRegister) -> int:

        if isinstance(address, Address):
            ret = address.address
        elif isinstance(address, AddressByRegister):
            register = address.register
            offset = address.offset
            ret = self.registers[register] + offset
        else:
            # print what instance address is
            print("Address is instance of: ", type(address))
            raise Exception("Invalid address type")


        # check for out of bounds according to instruction memory
        if ret >= len(self.memory.memory):
            raise Exception("Address out of bounds")

        return ret

    def read(self, address: Address | AddressByRegister) -> float:
        address = self.compute_address(address)
        return self.memory.read(address)

    def write(self, address: Address | AddressByRegister, value: float):
        address = self.compute_address(address)
        self.memory.write(address, value)


class Instruction(ABC):
    """
    An instruction is a single operation that can be executed by the virtual machine.
    """

    def __init__(self, operands: List[Address | Literal | Register | AddressByRegister]):
        self.operands = operands

    def execute(self, vm: VirtualMachine):
        # Implement the logic for executing the instruction on the virtual machine (vm)
        pass


class Load(Instruction):
    """
    Load a value from memory into a registerName.
    """
    address: Address | AddressByRegister
    register: int

    def __init__(self, address: Address | AddressByRegister, registerName: str):
        self.address = address
        self.registerId = registerName
        super().__init__([address, registerName])

    def execute(self, vm: VirtualMachine):
        value = vm.read(self.address)
        vm.registers[self.registerId] = value


class Store(Instruction):
    """
    Store a value from a registerName into memory.
    """
    address: Address | AddressByRegister
    value: Literal | Register

    def __init__(self, address: Address | AddressByRegister, value: Literal | Register):
        self.address = address
        self.value = value
        super().__init__([address, value])

    def execute(self, vm: VirtualMachine):
        vm.write(self.address, self.value)


class Jump(Instruction):
    """
    Jump inconditionally to an address.
    """
    address: Address | AddressByRegister

    def __init__(self, address: Address | AddressByRegister):
        self.address = address
        super().__init__([address])

    def execute(self, vm: VirtualMachine):
        vm.set_instruction_pointer(self.address)


class Opcode(Enum):
    LOAD = Load
    STORE = Store
    JUMP = 3
    JE = 4
    CMP = 5
    JGE = 6
    JLE = 7
    JG = 8
    JL = 9
