# CodesOnBytes
# Phase 1

This repository contains Python scripts to retrieve data from a public API and clean a dataset using Python and Pandas. The scripts perform the following tasks:

## Phase 1 Tasks

### Task 1 - Data Retrieval from a Public API

#### Python Script: `retrieve_data_from_api.py`

This script calls a public API to fetch data and create a CSV dataset using Python and Pandas.

#### How to Use:

1. Clone the repository to your local machine.
2. Open the script `retrieve_data_from_api.py` in a Python environment.
3. Run the script. It will make a request to the Binance API and create a CSV dataset named `binance_data.csv`.

### Task 2 - Data Cleaning

#### Python Script: `clean_dataset.py`

This script takes an existing dataset, replaces missing values, and removes outliers.

#### How to Use:

1. Download the dataset from the provided link.
2. Open the script `clean_dataset.py` in a Python environment.
3. Update the file path to your downloaded dataset.
4. Run the script. It will clean the dataset and create a new CSV file named `cleaned_dataset.csv`.

## Phase 2 Tasks

### Task 1 - Dataset Analysis and Graphs

#### Python Script: `analyze_dataset.py`

This script analyzes the dataset and creates graphs using Seaborn and Matplotlib.

#### How to Use:

1. Download the dataset from the provided link.
2. Open the script `analyze_dataset.py` in a Python environment.
3. Update the file path to your downloaded dataset.
4. Run the script. It will generate graphs based on the dataset.

### Task 2 - Simple Linear Regression Model

#### Python Script: `linear_regression.py`

This script trains a simple linear regression model on a dataset and predicts the output.

#### How to Use:

1. Download the train and test datasets from the provided links.
2. Open the script `linear_regression.py` in a Python environment.
3. Update the file paths to your downloaded train and test datasets.
4. Run the script. It will train the model and make predictions on the test dataset.

## Prerequisites:

- Python
- Pandas
- Scipy (for outlier removal in the cleaning script)
- Seaborn
- Matplotlib
- Scikit-Learn (for linear regression in Phase 2, Task 2)

Feel free to customize and extend the scripts as needed for your specific use case.

## Author:

Abhilash Reddy B

## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
