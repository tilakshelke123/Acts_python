#  Create a class that captures planets. 
#	Each planet has a name, a distance from the sun, and its gravity relative to Earth’s gravity. For distance and gravity, use the type double which captures real numbers. Make objects for Earth and your favorite non-earth planet.
 
class Planets:
    
    def __init__ (self,name,dist_from_sun,gravity_relate_to_Earth):
        self.name= name
        self.dist_from_sun=dist_from_sun
        self.gravity_relate_to_Earth=gravity_relate_to_Earth
    
    
    def display_info (self):
        print(f"Name:{self.name}")
        print(f"Dist_from_sun:{self.dist_from_sun}")
        print(f"gravity_relate_to_Earth:{self.gravity_relate_to_Earth}")
        

def main():
    earth = Planets("Earth","100km",50)
    mars = Planets("Mars","200km",100)
        
    earth.display_info()
    mars.display_info()
    
if __name__ == '__main__':
 main()