import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    minresult = 1e12
    index = 0
    for coeff in c:
        i = 0
        totresult = 0
        for x in X:
            result = coeff @ x
            diff = (result - y[i])**2
            totresult = totresult + diff 
            #print(result)
            #print(diff)
            i = i + 1

        if totresult < minresult:
            minresult = totresult
            best_index = index

        index = index + 1
        #print("totresult:" + str(totresult))
        #print("best_index:" + str(best_index))
            #pass     # edit here: calculate the sum of squared error with coefficient set coeff and
                 # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % best_index)


find_best(X, y, c)
