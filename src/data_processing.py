import argparse
import pandas as pd
import sys
import os
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.utils import get_numeric_column_names, get_highly_correlated_column_names
pd.options.mode.chained_assignment = None  # default='warn'


def preprocess_dataset(input_data: pd.DataFrame):
    """ The preprocessing selects the relevant data.

    Parameters
    ----------
    input_data : pd.Dataframe
        Input data

    Returns
    -------
    x : pd.Dataframe
        Transformed data containing the training data.
    y : pd.Dataframe
        Transformed data containing the training data target
    x_test : pd.Dataframe
        Transformed data containing the tests data.
    y_test : pd.Dataframe
        Transformed data containing the tests data target
    """
    if input_data is None:
        raise ValueError('input_data cannot be None')
    # drop any rows that have a non-numeric 'q_OpeningHours' value
    input_data['q_OpeningHours'] = pd.to_numeric(input_data['q_OpeningHours'], errors='coerce')
    rows_before = input_data.shape[0]
    input_data.dropna(inplace=True)
    logging.info('dropped {} row(s) that had invalid data'.format(rows_before - input_data.shape[0]))
    # drop the highly correlated rows
    input_data = input_data.drop(get_highly_correlated_column_names(), axis=1)
    # rename a couple of the columns
    input_data = input_data.rename(columns={"b_gekauft_gesamt": "converted", "b_in_kontakt_gewesen": "contacted"})
    target_col = ['converted']
    # split the data by the target column
    df_x = input_data.drop(target_col, axis=1)
    df_y = input_data[target_col]
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, train_size=0.8, test_size=0.2, random_state=42)
    # standardize the data
    scaler = StandardScaler()
    scaler = scaler.fit(x_train[get_numeric_column_names()])
    x_train[get_numeric_column_names()] = scaler.transform(x_train[get_numeric_column_names()])
    x_test[get_numeric_column_names()] = scaler.transform(x_test[get_numeric_column_names()])
    return x_train, y_train, x_test, y_test


def main():
    """Parse the parameters from the command line and do the data processing.
    """
    parser = argparse.ArgumentParser(description='Preprocess data')
    parser.add_argument('Path', metavar='path', type=str, help='the path to the data')
    args = parser.parse_args()
    input_path = os.path.abspath(args.Path)
    if not os.path.isfile(input_path):
        print('The path specified does not exist')
        sys.exit()
    input_data = pd.read_csv(input_path, index_col='fakeID')
    x, y, x_test, y_test = preprocess_dataset(input_data)
    print(x[get_numeric_column_names()].describe(), flush=True)
    print(x_test[get_numeric_column_names()].describe(), flush=True)


if __name__ == "__main__":
    main()
