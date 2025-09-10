import pandas as pd


def get_column(file_name, query_column, query_value, result_column):

    df = pd.read_csv(file_name)

    q_column = df[query_column]
    indicies = df.index[q_column == query_value]

    results = df[result_column][indicies]

    return results
