import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

    # read in the training data and separate it to x_train and y_train
    
    train_file = StringIO(train_string)
    test_file = StringIO(test_string)

    train_data  = np.genfromtxt(train_file, skip_header=1)
    test_data  = np.genfromtxt(test_file, skip_header=1)

    train_columns = train_data.shape[1]
    train_x = train_data[:,0:train_columns-1]
    train_y = train_data[:,train_columns-1:train_columns]

    #print(train_x)
    #print(train_y)
    
    test_columns = test_data.shape[1]
    test_x = test_data[:,0:test_columns-1]
    test_y = test_data[:,test_columns-1:test_columns]

    #print(test_x)
    #print(test_y)
    c = np.linalg.lstsq(train_x, train_y)[0]

    # fit a linear regression model to the data and get the coefficients
    #c = np.asarray([])

    # read in the test data and separate x_test from it
    #x_test = np.asarray([])

    # print out the linear regression coefficients
    print(c.T[0])
    # this will print out the predicted prics for the two new cabins in the test data set
    result = test_x @ c
    print(result.T[0])


main()
