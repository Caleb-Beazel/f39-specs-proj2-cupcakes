class Cupcake():

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


german_chocolate = Cupcake('German Chocolate', 4.99, 'german chocolate', 'coconut pecan', None)

german_chocolate.filling = 'chocolate'

german_chocolate.add_sprinkles('coconut flakes')

print(german_chocolate.sprinkles)