from my_utils import *
import argparse

parser = argparse.ArgumentParser(description='Input ',  # Initialize argument parser
                                 prog='Extract data on fires from a given country')

parser.add_argument('--country',    # Add arguments
                    type=str,
                    help='Input the country you wish to study',
                    required=True,
                    default='United States of America')

parser.add_argument('--country_column',
                    type=str,
                    help='Select column to query by name',
                    required=True,
                    default='Area')

parser.add_argument('--fires_column',
                    type=str,
                    help='Select column by name to get data from',
                    default='Forest fires')

parser.add_argument('--file_name',
                    type=str,
                    help='Data file to extract from',
                    required=False,
                    default='Agrofood_co2_emission.csv')

args = parser.parse_args()

fires = get_column(file_name=args.file_name,    # Execute function to extract data
                   query_column=args.country_column,
                   query_value=args.country,
                   result_column=args.fires_column)

print(fires)
