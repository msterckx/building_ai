import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # read the data in and fit it. the values below are placeholder values
    c = np.asarray([])  # coefficients of the linear regression
    x = np.asarray([])  # input data to the linear regression

    data  = np.genfromtxt(input_file, skip_header=1)
    #data  = np.genfromtxt(input_file)
    columns = data.shape[1]
    x = data[:,0:columns-1]
    y = data[:,columns-1:columns]
    #print(x)
    #print(y)
    c = np.linalg.lstsq(x, y)[0]
    c_r = c.T[0]
    x_c = x @ c
    print(c_r)
    print(x_c.T[0])

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
