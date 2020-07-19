print("MENU CARD")
print("select your favorite ice_cream with a Quantity")
print("There are three flavours select one flavour","\n","1.vennila=25 2.chocolate=35 3.strawberry=45")
print("chocolate flavour only have toppings","\n","1.caremel=10 2.nuts=15 3.chocochip=20")
print("Three types of shape is there select one:","\n","1.cone=15 2.cup=10 3.stick=5")
class Ice_cream:
    def __init__(self,shape,flavour,quantity,topping):
        self.shape=shape
        self.flavour=flavour
        self.quantity=quantity
        self.topping=topping
    def shape_cost(self):
        if self.shape=="stick":
            return 5
        if self.shape=="cone":
            return 15
        if self.shape=="cup":
            return 10
    def flavour_cost(self):
        if self.flavour=="vennila":
           return (self.quantity/100*25)
        elif self.flavour=="chocolate":
           return (self.quantity/100*35)
        else:
            return  (self.quantity/100*45)
    def cost_of_topping(self):
        if self.topping=="caremel":
            return 10
        elif self.topping=="nuts":
            return 15
        elif self.topping=="chocochip":
            return 20
        else:
            return 0
class Updated_cost(Ice_cream):
    def __init__(self,shape,flavour,quantity,topping):
        super().__init__(shape,flavour,quantity,topping)
    def total_cost(self):
        if self.flavour=="chocolate":
            return ("The updated ice_cream price is:%s"%(Ice_cream.shape_cost(self)+Ice_cream.flavour_cost(self)+Ice_cream.cost_of_topping(self)))
        else:
            return ("The updated ice_cream price is:%s"%(Ice_cream.shape_cost(self)+Ice_cream.flavour_cost(self)))
vennila=Updated_cost("cone","vennila",350,"none")
chocolate=Updated_cost("cup","chocolate",250,"caremel")
strawberry=Updated_cost("stick","strawberry",500,"none")
print(vennila.total_cost())
print(chocolate.total_cost())
print(strawberry.total_cost())
'''
MENU CARD
select your favorite ice_cream with a Quantity
There are three flavours select one flavour 
1.vennila=25 2.chocolate=35 3.strawberry=45
chocolate flavour only have toppings 
1.caremel=10 2.nuts=15 3.chocochip=20
Three types of shape is there select one: 
1.cone=15 2.cup=10 3.stick=5
The updated ice_cream price is:102.5
The updated ice_cream price is:107.5
The updated ice_cream price is:230.0
'''
