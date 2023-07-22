from abc import ABC
from typing import List


class Address:
    address: int

    def __init__(self, address: int):
        self.address = address


    def __repr__(self):
        return str(self.address)

    def __str__(self):
        return str(self.address)


class AddressByRegister:
    register: str
    offset: int

    def __init__(self, registerName: str, offset: int):
        self.register = registerName
        self.offset = offset

    def __repr__(self):
        return f'{self.register} + {self.offset}'

    def __str__(self):
        return f'{self.register} + {self.offset}'


class Literal:
    value: float

    def __init__(self, value: float):
        self.value = value

    def get_value(self) -> float:
        return self.value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)



class Memory:
    memory: List[float]
    size: int

    def __init__(self, size: int):
        self.size = size
        self.memory = [0] * size  # TODO: memory is random at frist

    def read(self, address: int) -> float:
        return self.memory[address]

    def write(self, address: int, value: float):
        self.memory[address] = value  # TODO: memory stores bits not floats

    def get_size(self) -> int:
        return self.size