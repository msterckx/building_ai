import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.empty(10000)
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    cnt = 0
    i = 0
    for i in range(0,9996):
        if (seq[i]==1) and (seq[i+1]==1) and (seq[i+2]==1) and (seq[i+3]==1) and (seq[i+4]==1):
            cnt = cnt +1
    return cnt

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))