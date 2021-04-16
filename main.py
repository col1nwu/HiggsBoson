import numpy as np
import pandas as pd

if __name__ == '__main__':
    """
    LOADING DATA
    """
    # Import data from source file
    raw_data = pd.read_csv('training.csv').values

    # Select 1,000 samples from dataset
    data = raw_data[:1000, :]
    n, d = data.shape

    """
    CLEANING DATA
    """
    # Extract label and convert the last column (label) to -1 and 1
    label = data[:, d - 1]
    label = np.array([label]).T

    samples_with_s = list(np.where(label == 's')[0])
    label[samples_with_s] = 1.0
    samples_with_b = list(np.where(label == 'b')[0])
    label[samples_with_b] = -1.0

    # Separate data to get training data and testing data
    training = data[:500, :]
    testing = data[500:, :]

    X = training[:, 1:31]
    y = label[:500, 31]
    X_test = testing[:, 1:31]
    y_test = label[500:, 31]

    print(1)
