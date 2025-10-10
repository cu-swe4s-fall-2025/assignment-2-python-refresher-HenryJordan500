import pandas as pd
import numpy as np


def get_column(file_name, query_column, query_value, result_column=0):


    df = pd.read_csv(file_name)  # Initialize csv as dataframe
    arr = df.to_numpy()     # Convert dataframe to numpy array

    # Extract the column that is being queried
    q_column = arr[:,query_column]

    # Find where the in queried column it equals to queried value and set it to the value in the results column
    results = np.where(q_column == query_value, arr[:,result_column], 0)

    # Remove 0 elements from results array
    results = results[results != 0]

    # Convert array datatype to integer than convert array to list
    return results.astype(int).tolist()

def mean(array):

    if len(array) == 0:

        raise ValueError('list is of zero length')
    else:

        return sum(array) / len(array)

def median(array):

    sorted_array = sorted(array)
    mid_len = len(array) / 2

    if mid_len == 0:

        raise ValueError('list is of zero length')
    
    elif len(array) % 2 == 1:

        return sorted_array[int(mid_len)]
    
    else:

        return (sorted_array[int(mid_len - 0.5)] + sorted_array[int(mid_len + 0.5)]) / 2

def std(array):

    if len(array) == 0:

        raise ValueError('list of of zero length')
    
    else:

        std_list = []
        std_mean = mean(array)

        for i in range(len(array)):
            std_list.append((array[i] - std_mean)**2)

        std = np.sqrt(sum(std_list)/len(std_list))

        return std


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
