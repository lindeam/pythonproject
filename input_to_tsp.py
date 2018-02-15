#!/usr/bin/python

############################################################################
#This is the document with the input to the travelling salesperson problem #
############################################################################
import numpy as np

cities = np.array(["Stockholm","Goteborg","Malmo","Uppsala","Vasteras","Orebro","Linkoping","Helsingborg","Jonkoping","Norrkoping"])

distance = np.array([
[0,469,613,70,108,201,200,556,324,163],     #Stockholm
[469,0,273,453,376,282,275,217,150,313],    #Goteborg
[613,273,0,679,597,502,417,65,292,456],     #Malmo
[70,453,679,0,78,171,265,622,390,228],      #Uppsala
[108,376,597,78,0,95,187,540,308,150],       #Vasteras
[201,282,502,171,95,0,123,446,213,118],      #Orebro
[200,275,417,265,187,123,0,361,129,43],      #Linkoping
[556,217,65,622,540,446,361,0,235,398],      #Helsingborg
[324,150,292,390,308,213,129,235,0,167],     #Jonkoping
[163,313,456,228,150,118,43,398,167,0],     #Norrkoping
])         