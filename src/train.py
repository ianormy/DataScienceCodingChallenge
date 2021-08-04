"""Train a Random Forest model using the input data.
"""
import os
import argparse
import sys
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd
import pickle
from data_processing import preprocess_dataset


def train(input_path):
    """Train our model using the input data

    Parameters
    ----------
    input_path : str
        Path to the data file.
    """
    logging.info(f'Loading data in {input_path}')
    df = pd.read_csv(input_path, index_col='fakeID')
    logging.info('Preparing data')
    x_train, y_train, x_test, y_test = preprocess_dataset(df)
    # Create the Random Forest Classifier model
    logging.info('Creating model')
    num_estimators = 100
    min_samples = 4
    model = RandomForestClassifier(n_estimators=num_estimators, min_samples_split=min_samples)
    # train the model using the training data
    logging.info('Training model')
    model.fit(x_train, y_train.values.ravel())
    logging.info('Saving trained model')
    # save the model for future use if needed
    filename = 'final_model.pkl'
    pickle.dump(model, open(filename, 'wb'))
    # test the trained model on our test data
    logging.info('Evaluating trained model on test data')
    y_test_pred = model.predict(x_test)
    # calculate the accuracy and AUC of the model
    accuracy = metrics.accuracy_score(y_test, y_test_pred)
    auc_score = metrics.roc_auc_score(y_test, y_test_pred)
    logging.info(f'accuracy: {accuracy:.2f}')
    logging.info(f'area under curve (AUC): {auc_score:.2f}')


def main():
    """Parse the parameters from the command line and do the training
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    parser = argparse.ArgumentParser(description='Train a Random Forest Classifier')
    parser.add_argument('Path', metavar='path', type=str, help='the path to the training data')
    args = parser.parse_args()
    input_path = os.path.abspath(args.Path)
    if not os.path.isfile(input_path):
        logging.error('The path specified does not exist')
        sys.exit()
    train(input_path)


if __name__ == "__main__":
    main()
