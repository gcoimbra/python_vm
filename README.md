# Virtual Machine Project

This project is a simple implementation of a Virtual Machine (VM) in Python. The VM is capable of executing a set of instructions, managing memory, and handling registers.

## Features

- **Memory Management**: The VM has a memory of a specified size, which can be read from or written to. The memory is initialized with zeros.
                                                                                                                                                             
- **Registers**: The VM has a set of registers, each of which can store a value. The registers are named 'r0', 'r1', 'r2', 'r3', 'cmp', 'pc', 'sp', and 'fp'.
                                                                                                                                                             
- **Instructions**: The VM can execute a set of instructions. Each instruction is an operation that the VM can perform. The current set of instructions includes Load, Store, and Jump.                                                                                                                                   
                                                                                                                                                             
- **Verbose Mode**: The VM can be run in verbose mode, which prints out additional information during execution.                                             
                                                                                                                                                             
## Usage                                                                                                                                                     
                                                                                                                                                             
To use the VM, create an instance of the `VirtualMachine` class with the desired memory size. Then, load the instructions you want the VM to execute using the `load_instructions` method. Finally, call the `run` method to start execution.                                                                             
                                                                                                                                                             
You can also use the `print_memory`, `print_registers`, and `print_instructions` methods to print the current state of the VM's memory, registers, and instructions, respectively.                                                                                                                                        
                                                                                                                                                             
## Instructions                                                                                                                                              
                                                                                                                                                             
- **Load**: This instruction loads a value from memory into a register. It takes an address and a register as operands.                                      
                                                                                                                                                             
- **Store**: This instruction stores a value from a register into memory. It takes an address and a value as operands.                                       
                                                                                                                                                             
- **Jump**: This instruction jumps unconditionally to an address. It takes an address as an operand.                                                         
                                                                                                                                                             
## Future Work                                                                                                                                               
                                                                                                                                                             
This project is a basic implementation of a VM and there are many ways it could be expanded. For example, additional instructions could be added, or the memory and register management could be made more complex.      
