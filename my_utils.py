import pandas as pd


def get_column(file_name, query_column, query_value, result_column):


    df = pd.read_csv(file_name)  # Initialize csv as dataframe

    # Extract the column that is being queried
    q_column = df[query_column]

    # Extract indicies of the column where the value in dataframe matches queried value
    indicies = df.index[q_column == query_value]

    # Extract data from desired column that matches indicies of the
    results = df[result_column][indicies]

    # Convert dataframe datatype to integer than convert dataframe to list
    return results.astype(int).to_list()

def main():  # Define main function


    file_name = 'Agrofood_co2_emission.csv'
    query_column = 'Area'
    query_value = 'United States of America'
    result_column = 'Forest fires'

    fires = get_column(file_name=file_name,
                       query_column=query_column,
                       query_value=query_value,
                       result_column=result_column)

    print(fires)

if __name__ == '__main__':

    main()
