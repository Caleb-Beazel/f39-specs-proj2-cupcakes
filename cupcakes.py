import csv
from abc import ABC, abstractmethod
from pprint import pprint

def read_csv(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

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


# print(mini_chocolate.size)
# print(mini_chocolate.price)
# print(monster_vanilla.filling)
german_chocolate = Mini('German Chocolate', 2.99, 'german chocolate', 'coconut pecan')
german_chocolate.add_sprinkles('coconut flakes','chocolate shavings')
cookie_monster = Monster("Cookie Monster",27.99, "Chocolate", "Cream Cheese", "Chocolate Fudge")
cookie_monster.add_sprinkles("Oreo pieces")



cupcake_list = [german_chocolate, cookie_monster, mini_chocolate, monster_vanilla]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "filling": cupcake.filling,
                    "sprinkles": cupcake.sprinkles
                    })
            else:
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles
                })

# write_new_csv("cupcakes.csv",cupcake_list)

def add_cupcakes_to_csv(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "filling": cupcake.filling,
                    "sprinkles": cupcake.sprinkles
                    })
            else:
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles
                })