Project Title: City Sorting and Mapping Visualization

Overview

This project visualizes and sorts a list of cities from a dataset, plotting them on a map using cs1lib. It enables users to interact with the map, identify city names, and explore cities sorted by various attributes such as name, population, and latitude. This program combines concepts from data filtering, sorting algorithms, and graphical visualization.

Features

	•	Sorting Functionality:
	•	Cities can be sorted alphabetically by name, by population, or by latitude.
	•	Interactive Map:
	•	Displays cities as points on a background map.
	•	Allows users to click on a city to view its name.
	•	Highlights the selected city while reverting the previous city’s color.
	•	Customizable Display:
	•	Users can specify the number of cities to display on the map.

Files

	•	world_cities.txt: The input file containing data on world cities.
	•	cities_out.txt: The file that stores all processed city data.
	•	cities_alpha.txt: File storing cities sorted alphabetically.
	•	cities_population.txt: File storing cities sorted by population.
	•	cities_latitude.txt: File storing cities sorted by latitude.
	•	maps_2.png: The background image of the map.
	•	city.py: Contains the City class defining the properties and drawing functions for city objects.
	•	quicksort.py: Implements a quicksort algorithm for sorting the city list.
	•	container.py: Contains the Container class used to display additional information on the screen.

Requirements

To run the project, you need:

	•	Python 3.x
	•	cs1lib library

How to Run

	1.	Place all required files in the same directory.
	2.	Run the main Python file.

python your_script_name.py


	3.	Interact with the graphical window:
	•	Left-click on a city to see its name displayed in the panel.

Sorting Logic

The program uses a custom compare_func in conjunction with a quicksort algorithm to sort the list of cities by:

	1.	Population: Uses a numerical comparison.
	2.	Alphabetical Order: Uses a string comparison.
	3.	Latitude: Uses a floating-point comparison.

The results are written to respective output files.

Interactivity

	•	Mouse Controls:
	•	Clicking on a city changes its color to orange.
	•	Previously selected cities revert to their original color.
	•	Dynamic Panel:
	•	Displays the name of the currently selected city.

Future Improvements

	•	Add more detailed visualizations, such as lines connecting cities based on proximity.
	•	Enhance sorting options to include longitude or combine multiple sorting criteria.
	•	Allow zooming and panning functionality on the map for better interactivity.

Acknowledgments

	•	Inspired by coursework in CS1.
	•	Utilizes the cs1lib library for graphical rendering.

Author

Richmond Nartey Kwalah Tettey
Course: CS1
Date: November 7, 2024
Purpose: To sort cities and display them interactively on a map.