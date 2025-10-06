from my_utils import *
import argparse

parser = argparse.ArgumentParser(description='Input ',  # Initialize argument parser
                                 prog='Extract data on fires from a given country')

parser.add_argument('--country',    # Add arguments
                    type=str,
                    help='Input the country you wish to study',
                    required=False,
                    default='United States of America')

parser.add_argument('--country_column',
                    type=int,
                    help='Select column to query by number starting from index 0',
                    required=False,
                    default=0)

parser.add_argument('--fires_column',
                    type=int,
                    help='Select column to get data from by index starting at 0',
                    required=False,
                    default=3)

parser.add_argument('--file_name',
                    type=str,
                    help='Data file to extract from',
                    required=False,
                    default='Agrofood_co2_emission.csv')

parser.add_argument('--operation',
                    type=str,
                    help='Specifiy to compute mean, median or std of retrived data',
                    required=False)

args = parser.parse_args()

fires = get_column(file_name=args.file_name,    # Execute function to extract data
                   query_column=args.country_column,
                   query_value=args.country,
                   result_column=args.fires_column)

print(fires)

if args.operation == 'median':
    print(f'Median is {median(fires)}')
elif args.operation == 'mean':
    print(f' Mean is {mean(fires)}')
elif args.operation == 'std':
    print(f'Standard deviaiton is {std(fires)}')
