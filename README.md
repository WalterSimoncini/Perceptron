# Perceptron

Two simple perceptron implementations:

- AND function classifier (run it with `python and_classifier.py`)
  - In order to mimic the behavior shown in the slides, this perceptron implementation will stop the current epoch if an error is encountered and start a new epoch (after adjusting the connections weights)
- Generic linear function classifier (run it with `python linear_function_classifier.py`)
  - The program will pause 1 second between each epoch to let the user observe the weights changes and the error sum accumulated during the current epoch

The linear function classifier can be run in verbose mode (default) or in non-verbose mode, in which only the perceptron's accuracy on the validation data set will be printed. This second mode is particularly useful for analyzing the perceptron's behavior based on the input data sets (training and validation)

### Requirements

In case you want to recreate the charts in the `charts` folder you might have to install the libraries listed in `requirements.txt`. No libraries should be needed for running the perceptron implementation. The program should work with both python 2.x and python 3.x. To use the plotting tools Python 2.x is recommended

### Generating dataset

To generate a new data set for the linear function classifier you can use:

`python data_generator.py <filename> <data_set_size>`

Where:

- `<filename>` is the filename of the output csv file (without the .csv extension)
- `<data_set_size>` is the size of the generated data set (e.g. 100)

The data generator generates data sets for the function $y = 2x + 1$ but you can edit it to generate data for any kind of linear function.