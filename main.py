from interpreter.memory import Address, Literal, AddressByRegister
from interpreter.virtualmachine import VirtualMachine, Store, Load, Jump

if __name__ == '__main__':

    vm = VirtualMachine(8, True)
    testCase1 = [
        Store(address=Address(0), value=Literal(1)),
        Load(address=Address(0), registerName='r0'),
        Jump(address=Address(0))
    ]



    testCase2 = [
        Store(address=Address(0), value=Literal(1)),
        Load(address=Address(0), registerName='r0'),
        Jump(address=AddressByRegister('r0', 1))
    ]

    vm.load_instructions(testCase2)

    vm.run()

    vm.summary()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
