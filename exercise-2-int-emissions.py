from itertools import permutations 

def getRoutes(route):
  perm = permutations(route)
  return perm

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


    co2 = 0.020
   
    
    route_seed = [1, 2, 3, 4]

    rts = getRoutes(route_seed)
    for route in list(rts):  
      route = list(route)
      route.insert(0,0)

      distance = sum([D[route[i]][route[i+1]] for i in range(0,len(route_seed))])
      emissions = distance * co2
    
      print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()

-