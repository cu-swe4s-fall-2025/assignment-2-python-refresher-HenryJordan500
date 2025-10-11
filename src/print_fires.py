from my_utils import *
import argparse


# Initialize argument parser
parser = argparse.ArgumentParser(description='Input ',
                                 prog=('Extract data on fires from'
                                       ' a given country'))

# Add arguments
parser.add_argument('--country',
                    type=str,
                    help=('Input the country'
                          ' you wish to study'),
                    required=False,
                    default='United States of America')

parser.add_argument('--country_column',
                    type=int,
                    help=('Select column to query by'
                          ' number starting from index 0'),
                    required=False,
                    default=0)

parser.add_argument('--fires_column',
                    type=int,
                    help=('Select column to get data'
                          ' from by index starting at 0'),
                    required=False,
                    default=3)

parser.add_argument('--file_name',
                    type=str,
                    help='Data file to extract from',
                    required=False,
                    default='Agrofood_co2_emission.csv')

parser.add_argument('--operation',
                    type=str,
                    help=('Specifiy to compute mean,'
                          ' median or std of retrived data'),
                    required=False,
                    default=None)

args = parser.parse_args()

# Execute function to extract data file
fires = get_column(file_name=args.file_name,
                   query_column=args.country_column,
                   query_value=args.country,
                   result_column=args.fires_column)

if args.operation == 'median':
    print(f'Median is {median(fires)}')
elif args.operation == 'mean':
    print(f'Mean is {mean(fires)}')
elif args.operation == 'std':
    print(f'Standard deviation is {std(fires)}')
else:
    print(fires)
