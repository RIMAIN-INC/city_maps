#Author: Richmond Nartey Kwalah Tettey
#Course: CS1
#Date: 11/07/2024
#Purpose: To sort cities and to display on map

from cs1lib import start_graphics, load_image, draw_image
from city import City
from quicksort import sort
from container import Container

WINDOW_X = 1000
WINDOW_Y = 500

#function to fetch certain attributes of object in each line of file
def filter_data():
    city_file = open("world_cities.txt", "r") #to open file
    updated_file = open("cities_out.txt", "w") #to create a new file,and append new object
    alpha_sort_file = open("cities_alpha.txt","w") #to store cities in alphabetical order
    population_sort_file = open("cities_population.txt", "w") #to store populated cities
    latitudes_sort_file = open("cities_latitude.txt", "w") #to store latitudes of cities in order

    city_list = [] #to create an empty list

    for line in city_file: #to loop through every line of file

        new_list = line.split(",") #to split data separated by comma

        new_city = City(new_list[0],new_list[1],new_list[2],new_list[3],new_list[4],new_list[5]) #to creat new object City
        city_list.append(new_city) #to add new object city to list


    for city in city_list: #to add filtered city data to new file created
        updated_file.write(str(city))


    # function to compare integers in a list
    def compare_population(a,b):
        return int(a.population) >= int(b.population)

    # function to compare strings in a list
    def compare_names(city1, city2):
        return city1.name.lower() <= city2.name.lower()

    def compare_latitude(l1,l2):
        return float(l1.latitude) <= float(l2.latitude)



    #sorting cities by latitude
    latitude_list = city_list
    sort(latitude_list,compare_latitude)

    for line in latitude_list:
        latitudes_sort_file.write(str(line))


    #sorting in alphabets
    alpha_list = city_list
    sort(alpha_list,compare_names)

    for line in alpha_list:
        alpha_sort_file.write(str(line))

    #sorting cities by population
    popolous_list = city_list
    sort(popolous_list,compare_population)

    for line in popolous_list:
        population_sort_file.write(str(line))



    city_file.close() #to close read file
    updated_file.close() #to close write file
    alpha_sort_file.close() #to close write file
    population_sort_file.close() #to close a file
    latitudes_sort_file.close() #to close a file

    return city_list

filtered_list = filter_data() #filter function is called

bg_img = load_image("maps_2.png") #to set canvas background with an image

cx = WINDOW_X / 2.17 #center of longitude window
cy = WINDOW_Y / 1.9 #center of latitude of window

#number of cities to display
no_cities = 80
max_list = filtered_list[:no_cities] #to an amount of city object

#variable to store name of clicked city
display_city_name = None

#get mouse x and y positions
my_mx = 0
my_my = 0

#store previous city
previous_city = None

#condition for when mouse is pressed
is_mouse_press = False

#function to check coordinates oof cities
def check_coordinates(mx,my,city):
    global display_city_name, previous_city
    px = cx + float(city.longitude) * 2.1
    py = cy - float(city.latitude) * 1.98
    if px - city.size <= mx <= px + city.size:
        if py - city.size <= my <= py + city.size:
            display_city_name = city.name
            c1.info = display_city_name

            if previous_city is None: #if first city is clicked
                previous_city = city
            else: #change previous city color to white and new city to orange
                previous_city.r = 1
                previous_city.g = 1
                previous_city.b = 1
                city.r = 1
                city.g = 165/255
                city.b = 0
                previous_city = city
            return True

#function to check all coordinates of cities
def check_all(clist,mx,my):
    for city in clist:
        if check_coordinates(mx,my,city):
            return True
        else:
            continue

c1 = Container(87, 79,50,"City",(149/255,95/255,70/255),(174/255,147/255,109/255)) #initialize a panel display

#main draw function
def main():
    global no_cities
    draw_image(bg_img,0,0) #call function to draw image

    #Drawing Display Container
    c1.draw()

    for i in range(no_cities): #to loop through cities to draw circle points
        max_list[i].draw(cx,cy)

    #check if mouse is pressed
    if is_mouse_press:
        if check_all(max_list, my_mx, my_my):
            print(display_city_name)


#function to get position of moused pressed
def my_mouse_press(mx,my):
    global my_mx, my_my, is_mouse_press
    print(mx,my)
    my_mx = mx
    my_my = my
    is_mouse_press = True

#function to get position of moused released
def my_mouse_release(mx,my):
    global my_mx, my_my, is_mouse_press
    my_mx = mx
    my_my = my
    is_mouse_press = False

#function to get position of mouse moved
def my_mouse_move(mx,my):
    pass

#function to start graphics
start_graphics(main,width=WINDOW_X, height=WINDOW_Y, mouse_release=my_mouse_release, mouse_press=my_mouse_press, mouse_move=my_mouse_move)