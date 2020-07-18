class Product:
    print("Tax details for products")
    def __init__(self,id,product_name,price,category):
        self.id=id
        self.product_name=product_name
        self.price=price
        self.category=category
    def tax_cal(self):
        if self.category != "diary":
           if self.price > 500:
              return (self.price * 0.05 + self.price)
           else:
              return  (self.price * 0.02 + self.price)
        else:
            return ("No tax")
class Category(Product):
    def __init__(self,id,product_name,price,category):
        super().__init__(id,product_name,price,category)
    def cal_tax(self):
        if self.category=="diary" and self.price>=1000:
           return  ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax_price:%s"%(self.price*0.03+self.price))
        elif self.category =="textile":
           return  ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax_price:%s"%((self.price*0.01)+Product.tax_cal(self)))
        else:
           return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax_price:%s"%Product.tax_cal(self))
butter=Category(8988,"butter",1416,"diary")
saree=Category(9868,"saree",488,"textile")
rice=Category(3644,"Rice",405,"produce")
chair=Category(4167,"chair",466,"Homeneeds")
milk=Category(8776,"milk",800,"diary")
shirt=Category(9345,"shirt",510,"textile")
wheat=Category(3648,"wheat",578,"produce")
table=Category(4164,"table",515,"Homeneeds")
print(butter.cal_tax())
print(saree.cal_tax())
print(rice.cal_tax())
print(chair.cal_tax())
print(milk.cal_tax())
print(shirt.cal_tax())
print(wheat.cal_tax())
print(table.cal_tax())
'''
Tax details for products
('product_name:butter', 'price:1416', 'tax_price:1458.48')
('product_name:saree', 'price:488', 'tax_price:502.64')
('product_name:Rice', 'price:405', 'tax_price:413.1')
('product_name:chair', 'price:466', 'tax_price:475.32')
('product_name:milk', 'price:800', 'tax_price:No tax')
('product_name:shirt', 'price:510', 'tax_price:540.6')
('product_name:wheat', 'price:578', 'tax_price:606.9')
('product_name:table', 'price:515', 'tax_price:540.75')
'''

