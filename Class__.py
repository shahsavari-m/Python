class lady:
    def __init__(self, name , age):
        self.__age = age
        self.name = name
    def show_lady(self):
        return self.name


l1 = lady("sara" , 99)
print(l1.show_lady())
