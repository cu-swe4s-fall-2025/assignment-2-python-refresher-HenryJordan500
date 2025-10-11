test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run general_test python -m src.print_fires --country "Albania" --country_column 0 --fires_column 3 --file_name "func_test_data.csv"
assert_in_stdout [7, 7, 7, 7, 7, 7, 13, 33, 6, 13, 77, 1, 6, 1, 2, 4, 0, 0, 2]
assert_exit_code 0

run mean_test python -m src.print_fires --country "Albania" --country_column 0 --fires_column 3 --file_name "func_test_data.csv" --operation "mean"
assert_in_stdout "Mean is 11.052631578947368"
assert_exit_code 0

run median_test python -m src.print_fires --country "Albania" --country_column 0 --fires_column 3 --file_name "func_test_data.csv" --operation "median"
assert_in_stdout "Median is 7"
assert_exit_code 0

run std_test python -m src.print_fires --country "Albania" --country_column 0 --fires_column 3 --file_name "func_test_data.csv" --operation "std"
assert_in_stdout "Standard deviation is 17.23971450554466"
assert_exit_code 0
