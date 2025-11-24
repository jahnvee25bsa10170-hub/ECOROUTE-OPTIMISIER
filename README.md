Route Emissions Simulator
● Overview of the project
A Python simulation tool that models how transportation emissions are affected by distance, speed, and number of stops. It generates multiple route variations between two points, calculates their CO2 emissions using a custom model, and identifies the most environmentally efficient option.

● Features

Generates random route variations with different distances, stops, and speeds

Calculates CO2 emissions based on distance, stops, and speed efficiency

Ranks routes by environmental impact and selects the optimal one

Provides visual charts comparing emissions across routes

Categorizes results as "nice", "ok", "meh", or "bad" based on emission levels

● Technologies/tools used

Python 3.6+

matplotlib (for visualization)

random and math modules (for route generation and calculations)

● Steps to install & run the project

Ensure Python 3.6 or later is installed

Install matplotlib: pip install matplotlib

Download the route_analyzer.py file

Run the script: python route_analyzer.py

Check the screenshots folder for generated charts (if matplotlib is available)

● Instructions for testing

Run the script multiple times to see different random route combinations

Modify the start and end points in the main() function to test different distances

Adjust the count parameter in make_routes() to generate more or fewer routes

Change the emission factors in the co2_calc() function to test different environmental models

Verify results by checking console output for route rankings and emission calculations

Disable matplotlib to test text-only functionality

