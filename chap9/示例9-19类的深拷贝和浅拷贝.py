class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = Disk()

com = Computer(cpu, disk)

com1 = com
print('对象的地址：', com, '子对象的内存地址：', com.cpu, com.disk)
print('对象1的地址：', com1, '子对象的内存地址：', com1.cpu, com1.disk)

print('-' * 40)
import copy

com2 = copy.copy(com)
print('对象的地址：', com, '子对象的内存地址：', com.cpu, com.disk)
print('对象2的地址：', com2, '子对象的内存地址：', com2.cpu, com2.disk)

print('-' * 40)
com3 = copy.deepcopy(com)
print('对象的地址：', com, '子对象的内存地址：', com.cpu, com.disk)
print('对象2的地址：', com3, '子对象的内存地址：', com3.cpu, com3.disk)
