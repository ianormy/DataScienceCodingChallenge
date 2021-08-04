# Data Scientist: Coding Challenge
Data Scientist coding challenge.

I have chosen to do challenge number 2: Customer lead generator.

## Exploratory Data Analysis
Please see my notebook [EDA-Customer-Lead-Generator.ipynb](notebooks/EDA-Customer-Lead-Generator.ipynb) for an explanation of my exploratory data analysis.

## Training and evaluating a model
Please see my notebook [TRAIN-train-the-model.ipynb](notebooks/TRAIN-train-the-model.ipynb) for an explanation of my training and evaluating the model.

## Standalone scripts and test
To run the standalone scripts and test from your commandline, you should set your PYTHONPATH to the place you have cloned this repository to:

```
set PYTHONPATH=<path_to_cloned_repository>
```

## Data Preparation - standalone
I have put code for the data preparation into the file [data_processing.py](src/data_processing.py). You can run this as a stand-alone script as follows:

```
python src\data_processing.py data\CustomerData_LeadGenerator.csv
```

## Training and evaluation - standalone
I have put code for the training into the file [train.py](src/train.py). You can run this as a stand alone script as follows:

```
python src\train.py data\CustomerData_LeadGenerator.csv
```

## Python Environment
I have put all the python environment requirements in the file **requirements.txt**. To install them into your virtual environment simply do the following:

```
pip install -r requirements.txt
```


## Testing
There aren't a lot of functions, but I've written some unit tests for the data preparation. To run these you can do:

```
python src\tests\test_data_processing.py
```
