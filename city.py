#Author: Richmond Nartey Kwalah Tettey
#Course: CS1
#Date: 11/07/2024
#Purpose: To sort cities and to display on map

from cs1lib import draw_circle, set_fill_color
from random import randint

RAD = 6

#city class
class City:
    def __init__(self,country_code,name,region,population,latitude,longitude): #creating a constructor method
        self.country = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude =  longitude
        (r, g, b) = (1,1,1)
        self.r = r
        self.g = g
        self.b = b
        self.size = RAD

    def draw(self,cx,cy):
        px = cx + float(self.longitude) * 2.1 #compute position of city's longitude
        py = cy - float(self.latitude) * 1.98  #compute position of city's latitude
        set_fill_color(self.r,self.g,self.b) #to set color of point

        draw_circle(int(px),int(py),RAD) #to draw a circle


    def __str__(self): #to convert objects to strings
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

