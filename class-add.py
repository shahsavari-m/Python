class Number:
    def __init__(self,value):
        self.value = value
    def __str__ (self):
            return str(self.value)
    def __add__ (self, other):
            return self.value + other.value

n1= Number (2)
n2= Number(2)

print(n1+n2+1)
