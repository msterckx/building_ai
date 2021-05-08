
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + np.abs(ai - bi)
    return sum

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            row_i = data[i]
            row_j = data[j]
            if (i == j):
                dist[i,j] = np.inf
            else:
                dist[i,j] = distance(row_i, row_j)

    #print(dist)
    print(np.unravel_index(np.argmin(dist), dist.shape))


def main(text):
    # tasks your code should perform:

    docs = [line.lower().split() for line in text.split('\n')]
    words = [line.lower() for line in text.replace('\n',' ').split(' ')]
    uniquewords = [ word  for word in np.unique(words)]
    docfreq = { item:(words.count(item)/len(docs))  for item in np.unique(words)}
    columns = len(uniquewords) 
    rows = len(docs)
    data = np.zeros((rows, columns), dtype=np.float)
    i = 0

    for uniqueword in uniquewords:
        j = 0
        for doc in docs:
            termfreq = { item:(doc.count(item)/len(doc))  for item in np.unique(doc)}
            if uniqueword in doc:
                tf = termfreq[uniqueword]
                df = docfreq[uniqueword]
                tf_idf = tf-np.log(1/df)
                data[j,i] = tf_idf
            else:
                data[j,i] = 0

            j = j + 1
  
        i = i + 1

    find_nearest_pair(data)

main(text)

