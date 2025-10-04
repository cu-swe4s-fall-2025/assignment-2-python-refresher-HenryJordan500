import pandas as pd
import numpy as np


def get_column(file_name, query_column, query_value, result_column=1):


    df = pd.read_csv(file_name)  # Initialize csv as dataframe
    arr = df.to_numpy()     # Convert dataframe to numpy array

    # Extract the column that is being queried
    q_column = arr[:,query_column]

    # Find where the in queried column it equals to queried value and set it to the value in the results column
    results = np.where(q_column == query_value, arr[:,result_column], 0)

    # Remove 0 elements from results array
    results = results[results != 0]

    # Convert dataframe datatype to integer than convert dataframe to list
    return results.astype(int).tolist()

def mean(array):


    return np.mean(array)

def median(array):


    return np.median(array)


def std(array):


    return np.std(array)


def main():  # Define main function


    file_name = 'Agrofood_co2_emission.csv'
    query_column = 0
    query_value = 'United States of America'
    result_column = 3

    fires = get_column(file_name=file_name,
                       query_column=query_column,
                       query_value=query_value,
                       result_column=result_column)

    print(fires)

if __name__ == '__main__':

    main()
