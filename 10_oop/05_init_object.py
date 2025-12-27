class ChaiOrder:
    def __init__(self, type_, size): # type is a reserved keyword that's why the underscore
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 250)
print(order_two.summary())