[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

## Get Column Function

get_column takes the data from a csv and extracts the data from the results column from just the values queried in the queried column. Accepts csv file, manipulates it as a numpy array, and outputs a list of integers 

## Print Fires

print_fires.py prints the forest fires in the input country for each year in the dataset. Executes from run.sh file. Arguments are --country --country_column --fires_column --file_name --operation. --operation takes "mean", "median", or "std".

# Testing
Unit tests validate mean, median, and standard deviaition functions. Functional testing on shortetend data set of full program. 

# Continuous Integration
Implemented continous intergration with github actions. Will run a unit test, functional test, and a pycodestyle linter. Will run on push and pull request.