##############################################################################################
# The Traveling Salesperson Problem
# This script takes as input a set of cities and the distance between each pair of cities 
# and return the shortest possible tour that visits each city exactly once and returns to the 
# starting city
#############################################################################################

import numpy as np
import itertools
import input_to_tsp as input # from here we get input.cities and input.distance


print ("\n\nThe Traveling Salesperson Problem \n----------------------------------\nThis script takes as input a set of cities and a pairwise distance matrix and it will return the shortest possible tour that visits each city exactly once and returns to the starting city together with the length of this tour. \n \nIt comes with a test set of cities (the 10 largest in Sweden) and to change this edit in the file input_to_tsp.py \n \n")


#All tours
#First I have to know how many cities there are
no_cities = len(input.cities)

#And make sure that there same numbers of rows and column in the distance matrix (the function)
def citiesAndDistances(distance,cities):
	if len(distance) == len(cities):
			return True
	if len(distance) != len(cities):
	        return False	       

#This is the function that actually calculate what we want to know! All tours start att the input.cities[0] to avoid redundant tours	       
def bestTour(alltours,distance):
    print ("\n\n ---SEARCHING FOR SHORTEST TOUR---\n\n")
    best_tour_distance = 10000
    tour_distance = 0
    for tours in alltours:
        tour_index = tours
        tour_distance = 0
        n = 0
        m = 1
        if (tour_index[0] == 0):
            while n < no_cities and m < no_cities:
               tour_distance = tour_distance + input.distance[tour_index[n],tour_index[m]]
               n+=1
               m+=1
            tour_distance = tour_distance + input.distance[tour_index[-1],tour_index[0]]
            if tour_distance < best_tour_distance:
                best_tour_distance = tour_distance
                best_tour = np.array(tour_index)
    return(best_tour, best_tour_distance)
     
            

#Make sure that there same numbers of rows and column in the distance matrix (the testing)
if citiesAndDistances(input.distance,input.cities) == False:
	    raise ValueError("Inconsistent number of cities and distances");	
			
# All possible tours 
alltours = list(itertools.permutations(range(no_cities),no_cities))

#Get the best tour and its distance given the list of all possible tours and the distance matrix

best_tour, best_tour_distance = bestTour(alltours,input.distance)
        
#To be able to print it in a nicer way:        
for i in range(len(best_tour)):
    if i == 0:
        city = str(input.cities[best_tour[i]])
    else:  
        city = city +" --> " +str(input.cities[best_tour[i]])
city = city + " --> " + input.cities[best_tour[0]]
km = int(best_tour_distance)
        
print("The shortest tour is %s" %(city))
print("\nThe length of the tour is %s km by car\n\n\n" %(km))