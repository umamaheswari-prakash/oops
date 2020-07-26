import re
class Driver_details:
    def __init__(self, Driver_name, Driver_age, licence_number, license_validity_period):
        self.Driver_name = Driver_name
        self.Driver_age = Driver_age
        self.license_number = licence_number
        self.license_validity_period = license_validity_period

    def is_license(self):
        if re.search('[A-z]{2}[0-9]{13}', self.license_number):
            return True

    def is_license_period(self):
        if re.search(r"([1-9]|1[0-9]| 2[0-9]|3[0-1])[/]([1-9] |1[0-2])[/]202[0-9]",self.license_validity_period):
            return True


class Car_details:
    def __init__(self, car_number, car_colour, car_company, car_model, category_name):
        self.car_number = car_number
        self.car_colour = car_colour
        self.car_company = car_company
        self.car_model = car_model
        self.category_name = category_name
    def is_car_number(self):
        if re.search(r"[A-z]{2} [0-9]{2} [A-z]{2} [0-9]{4}",self.car_number):
            return True

    def get_a_category_type(self):
        if self.category_name.lower() == "micro":
            print("Micro includes all cars that can accommodate a maximum upto 4 people")
        elif self.category_name.lower() == "xl":
            print("XL includes all cars that can accommodate a maximum upto 10 people.")


class Owner():
    print("WELCOME TO GORIDE SERVICE\n")
    def __init__(self,driver_details,car_details):
        self.driver_details=driver_details
        self.car_details=car_details


    is_driver = input("select a driver/car to registeration: ")

    def selction_process(self):
        if self.is_driver == "driver":
            return get_driver_details()
        else:
            return get_car_details()
    def submission_details(self):
        print("\t\t\tCONGRATS\n your registration process has been successful.")

def get_car_details():
    car_number = input("Enter a car number: ")
    car_colour = input("Enter a colour: ").lower()
    car_company = input("Enter a car company: ").lower()
    car_model = input("Enter a car model: ").lower()
    car_category = input("Enter a category type Micro or XL: ")
    car = Car_details(car_number, car_colour, car_company, car_model, car_category)
    if car.is_car_number()==True:
        return True
    print("enter valid car number")
    get_car_details()
    car.get_a_category_type()


def get_driver_details():
    driver_name = input("Enter a driver name: ")
    driver_age = input("Enter a driver age: ")
    license_num = input("enter a license number: ")
    license_period = input("Enter a license period dd/mm/yy : ")
    driver = Driver_details(driver_name, driver_age, license_num, license_period)
    if driver.is_license()==True:
        if driver.is_license_period()==True:
            return True
        print("license period expired")
    print("license num invalid")
    print("enter valid details again")
    get_driver_details()



details = Owner(Driver_details, Car_details)
details.selction_process()
details.submission_details()

'''
1.select a driver/owner to registeration: car
  Enter a category type Micro or XL: micro
  Micro includes all cars that can accommodate a maximum upto 4 people
  Enter a car number: TN 01 PA 4554
  Enter a colour: white
  Enter a car company: honda
  Enter a car model: city
			CONGRATS
 your registration process has been successful.
2. select a driver/car to registeration: driver
   Enter a driver name: anu
   Enter a driver age: 24
   Enter a license number: MH1420110062821
   Enter a license period dd/mm/yy : 04-02-2021
			CONGRATS
your registration process has been successful.
'''
