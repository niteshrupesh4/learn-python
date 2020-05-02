class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)


a = '8'
com1 = Computer('i5', 16)
com2 = Computer('i3', 8)

com1.config()
com2.config()
print(type(com1))
