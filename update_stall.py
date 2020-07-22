class Ice_cream:
    def __init__(self, shape, flavour, topping):
        self.shape = shape
        self.flavour = flavour
        self.topping = topping

    def adding_topping(self):
        if self.flavour == "chocolate":
            if self.topping == "caremel":
                return 10
            elif self.topping == "nuts":
                return 15
            elif self.topping == "chocochip":
                return 20


class Stall:
    print("                 MENU CARD                   ")
    print("select your favorite ice_cream with a Quantity")
    print("There are three flavours select one flavour:\n1.vennila=25\n2.chocolate=35\n3.strawberry=45")
    print("chocolate flavour only have toppings:\n1.caremel=10\n2.nuts=15\n3.chocochip=20")
    print("Three types of shape is there select one:\n1.cone=15\n2.cup=10\n3.stick=5")

    def __init__(self, shape, flavour, topping, quantity):
        self.shape=shape
        self.flavour = flavour
        self.topping = topping
        self.quantity = quantity
        self._Ice_cream=Ice_cream(self.shape,self.flavour,self.topping)



    def shape_cost(self):
        if self.shape == "stick":
            return 5
        if self.shape == "cone":
            return 15
        if self.shape == "cup":
            return 10

    def flavour_cost(self):
        if self.flavour == "vennila":
            return (self.quantity / 100 * 25)
        elif self.flavour == "chocolate":
            return (self.quantity / 100 * 35)
        else:
            return (self.quantity / 100 * 45)
    def total_cost(self):
        if flavour == "chocolate":
            return ("The updated ice_cream price is:%s" % (Stall.shape_cost(self) + Stall.flavour_cost(self) +self._Ice_cream.adding_topping()))
        else:
            print("only chocolate flavour have a toppings")
            return ("The updated ice_cream price is:%s" % (Stall.shape_cost(self) + Stall.flavour_cost(self)))


shape = input("enter a shape: ")
flavour = input("enter a flavour: ")
topping = input("chocolate only have a topping:")
quantity = int(input("enter a quantity: "))
cost = Stall(shape, flavour, topping, quantity)
print(cost.total_cost())




class Ice_cream:
    def __init__(self, shape, flavour, topping):
        self.shape = shape
        self.flavour = flavour
        self.topping = topping

    def adding_topping(self):
        if self.flavour == "chocolate":
            if self.topping == "caremel":
                return 10
            elif self.topping == "nuts":
                return 15
            elif self.topping == "chocochip":
                return 20


class Stall:
    print("                 MENU CARD                   ")
    print("select your favorite ice_cream with a Quantity")
    print("There are three flavours select one flavour:\n1.vennila=25\n2.chocolate=35\n3.strawberry=45")
    print("chocolate flavour only have toppings:\n1.caremel=10\n2.nuts=15\n3.chocochip=20")
    print("Three types of shape is there select one:\n1.cone=15\n2.cup=10\n3.stick=5")

    def __init__(self, shape, flavour, topping, quantity):
        self.shape=shape
        self.flavour = flavour
        self.topping = topping
        self.quantity = quantity



    def shape_cost(self):
        if self.shape == "stick":
            return 5
        if self.shape == "cone":
            return 15
        if self.shape == "cup":
            return 10

    def flavour_cost(self):
        if self.flavour == "vennila":
            return (self.quantity / 100 * 25)
        elif self.flavour == "chocolate":
            return (self.quantity / 100 * 35)
        else:
            return (self.quantity / 100 * 45)
def total_cost(Stall,Ice_cream):
    if flavour == "chocolate":
       return ("The updated ice_cream price is:%s" % (Stall.shape_cost() + Stall.flavour_cost() +Ice_cream.adding_topping()))
    else:
       print("only chocolate flavour have a toppings")
       return ("The updated ice_cream price is:%s" % (Stall.shape_cost() + Stall.flavour_cost()))


shape = input("enter a shape: ")
flavour = input("enter a flavour: ")
topping = input("chocolate only have a topping:")
quantity = int(input("enter a quantity: "))
cream=Ice_cream(shape,flavour,quantity)
cost = Stall(shape, flavour, topping, quantity)
print(total_cost(cost,cream))
