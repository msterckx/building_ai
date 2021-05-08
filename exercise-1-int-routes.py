import math
import random
import numpy as np
import io
from io import StringIO
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    k = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    matchcount = 0

                    for i in range (0,5):
                      if i in route:
                        matchcount = matchcount + 1
                    k = k + 1
                    if matchcount == 5:
                      # do not modify the print statement
                      print(' '.join([portnames[i] for i in route]))

main()