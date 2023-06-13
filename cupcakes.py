from abc import ABC, abstractmethod

class Cupcake(ABC):

    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling):

        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        
    
    def add_sprinkles(self, *args):

        for arg in args:
            self.sprinkles.append(arg)

    @abstractmethod
    def calculate_price(self, quantity):
        return self.price * quantity

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity

mini_chocolate = Mini("Mini Chocolate",1.99,"chocolate","chocolate")

class Monster(Cupcake):
    size = "monster"

    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity
    
monster_vanilla = Monster("Monster Vanilla", 20.99, "vanilla", "vanilla", "custard")

# german_chocolate = Cupcake('German Chocolate', 4.99, 'german chocolate', 'coconut pecan', None)

# german_chocolate.filling = 'chocolate'

# german_chocolate.add_sprinkles('coconut flakes','chocolate shavings')

# print(german_chocolate.sprinkles)
# print(german_chocolate.filling) 


print(mini_chocolate.size)
print(mini_chocolate.price)
print(monster_vanilla.filling)
