class Vehicle:
    print("         WELCOME TO  GORIDE          ")
    print(
        "AVAILABLE TRANSPORT\nAuto : can accomodate upto 3 people\nMicro : can accomodate upto 4 people\nXL : can accomodate upto 10 people")

    def __init__(self, category_type, km_range, with_ac_price, without_ac_price):
        self.category_type = category_type
        self.km_range = km_range
        self.with_ac_price = with_ac_price
        self.without_ac_price = without_ac_price

    def category_with_ac(self):
        print(self.category_type, "         ", self.km_range, "          ", self.with_ac_price)

    def category_without_ac(self):
        print(self.category_type, "         ", self.km_range, "          ", self.without_ac_price)


def price_menu(category, ac_need, details):
    print("Category        KM Range           Price")
    for obj in range(len(details)):
        if (category == details[obj].category_type):
            if (ac_need == "yes"):
                details[obj].category_with_ac()
            else:
                details[obj].category_without_ac()
    print("successfully booked a ride!")


def customer_selcection():
    category = input("select any one of the above category : ").lower()
    ac_need = input("do you want ac select yes/no:").lower()
    return (category, ac_need)


auto1 = Vehicle("auto", "upto 15km", "10/km", "NA")
auto2 = Vehicle("auto", "15-30km", "8/km", "NA")
auto3 = Vehicle("auto", "30km above", "15/km", "NA")
micro1 = Vehicle("micro", "upto 15km", "12/km", "10/km")
micro2 = Vehicle("micro", "15km above", "14/km", "12/km")
xl1 = Vehicle("xl", "upto 15km", "14/km", "15/km")
xl2 = Vehicle("xl", "15km above", "14/km", "15/km")

details = [auto1, auto2, auto3, micro1, micro2, xl1, xl2]
(category, ac_need) = customer_selcection()
price_menu(category, ac_need, details)


'''
         WELCOME TO  GORIDE          
AVAILABLE TRANSPORT
Auto : can accomodate upto 3 people
Micro : can accomodate upto 4 people
XL : can accomodate upto 10 people
select any one of the above category : micro
do you want ac select yes/no:yes
Category        KM Range           Price
micro           upto 15km            12/km
micro           15km above            14/km
successfully booked a ride!
'''
