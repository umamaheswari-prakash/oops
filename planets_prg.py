class Planet():
    earth_year = 365.25
    def __init__(self,planet_name,diameter,no_of_moons,length_of_year):
        self.planet_name=planet_name
        self.diameter =diameter
        self.no_of_moons=no_of_moons
        self.length_of_year=length_of_year
    def radius_of_planet(self):
        print("radius of ",self.planet_name,"is",self.diameter/2)
    def no_of_days(self):
        if(self.planet_name=="mercury" or self.planet_name=="venus" or self.planet_name=="earth" or self.planet_name=="mars"):
            print(self.length_of_year)
        else:
            self.length_of_year=(self.length_of_year * self.earth_year)
            print( self.planet_name ,self.length_of_year)
def largest_planet(*planets):
    for planet in planets:
        if planet.diameter==max_val:
           print("the largest planet",planet.planet_name)

mercury=Planet("Mercury",4879,0,88)
Venus=Planet("Venus",12100,0,225)
Earth=Planet("Earth",12755,1,365)
mars=Planet("Mars",6786,2,687)
jupiter=Planet("jupiter",142800,79,12 )
saturn=Planet("saturn",120537,82,29.5)
uranus=Planet("uranus",51819,27,84)
neptune=Planet("neptune",49529,14,165)
max_val = max(mercury.diameter, Venus.diameter, Earth.diameter, mars.diameter, jupiter.diameter, saturn.diameter, uranus.diameter, neptune.diameter)
largest_planet(mercury,Venus,Earth,mars,jupiter,saturn,uranus,neptune)
neptune.radius_of_planet()
jupiter.no_of_days()

