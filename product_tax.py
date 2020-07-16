class Product:
    print("Tax details for products")
    def __init__(self,id,product_name,price,category):
        self.id=id
        self.product_name=product_name
        self.price=price
        self.category=category
    def tax_product(self):
        if self.category =="textile":
           if self.price > 500:
              return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price*(0.05+0.01)),"total price:%s"%(self.price*(0.05+0.01)+ self.price))
           else:
              return("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price*(0.05+0.01)),"total price:%s"%(self.price*(0.02+0.01)+ self.price))
        elif self.category =="diary":
            if self.price >1000:
                return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price*(0.05+0.03)),"total price:%s"%(self.price * (0.05+0.03)+ self.price))
            else:
                return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price*0.02),"total price:%s"%(self.price+self.price*0.02))
        else:
            if self.price > 500:
                return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price * 0.05),"total price:%s"%(self.price * 0.05 + self.price))
            else:
                return ("product_name:%s"%(self.product_name),"price:%s"%(self.price),"tax:%s"%(self.price * 0.02),"total price:%s"%(self.price * 0.02 + self.price))

diary=Product(8988,"choco",1416,"diary")
Textile=Product(98687,"saree",488,"textile")
produce=Product(36448,"Rice",578,"produce")
Homeneeds=Product(416784,"chair",466,"Homeneeds")
print(diary.tax_product())
print(Textile.tax_product())
print(produce.tax_product())
print(Homeneeds.tax_product())