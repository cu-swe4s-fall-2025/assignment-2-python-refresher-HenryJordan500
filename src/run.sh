#!/bin/bash

echo "Country: $1"
echo "Country column: $2"
echo "Fires column: $3"
echo "Filename: $4"

python src/print_fires.py --country "$1" --country_column "$2" --fires_column "$3" --file_name "$4"