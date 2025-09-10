from my_utils import *

file_name = 'Agrofood_co2_emission.csv'
country_column = 'Area'
country = 'United States of America'
fires_column = 'Forest fires'

fires = get_column(file_name=file_name,
                   query_column=country_column,
                   query_value=country,
                   result_column=fires_column)

print(fires)
