class Planet():
    earth_year = 365.25
    def __init__(self,planet_name,diameter,no_of_moons,length_of_year):
        self.planet_name=planet_name
        self.diameter =diameter
        self.no_of_moons=no_of_moons
        self.length_of_year=length_of_year
    def radius_of_planet(self):
        print ("radius of %s"%(self.planet_name), "is:%s"% (self.diameter/2))
    def no_of_days(self):
        days=self.length_of_year.split()
        if "days" in self.length_of_year:
            total_no_of_days=days[0]
            print(self.planet_name,"days in earth days:%s "% total_no_of_days)
        else:
            years=days[0]
            total_no_days=(float(years) * self.earth_year)
            print( self.planet_name,"no of days in earth days:%s "% total_no_days)
def largest_planet(*planets):
    max_val = max(mercury.diameter, Venus.diameter, Earth.diameter, mars.diameter, jupiter.diameter, saturn.diameter,uranus.diameter, neptune.diameter)
    for planet in planets:
        if planet.diameter == max_val:
           print ("The largest planet is ",planet.planet_name)


mercury=Planet("Mercury",4879,0,"88 days")
Venus=Planet("Venus",12100,0,"225 days")
Earth=Planet("Earth",12755,1,"365 days")
mars=Planet("Mars",6786,2,"687 days")
jupiter=Planet("jupiter",142800,79,"12 years" )
saturn=Planet("saturn",120537,82,"29.5 years")
uranus=Planet("uranus",51819,27,"84 years")
neptune=Planet("neptune",49529,14,"165 years")
largest_planet(mercury,Venus,Earth,mars,jupiter,saturn,uranus,neptune)
neptune.radius_of_planet()
jupiter.no_of_days()

