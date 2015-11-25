#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from naivebayes import *
from xmlparser import get_documents, true_list
         
def main(neutral):
    
    get_documents(15, neutral)
    """for element in training_list:
        print element.vector
        print element.opinion"""
    
    result = training_nb(true_list, neutral)
    print apply_nb(result, "I do not really like this film", neutral)   


neutral = False
# main(neutral)

get_documents(15, neutral)

#print cross_validation(25, 98)

print cross_validation(2, 98, neutral)


result = 0
maximum = 0
count = 0
i_max = 0
j_max = 0
for j in range(1, 10):
    for i in range(60,98):
        result = cross_validation(j, i, neutral)
        if result > maximum:
            maximum = result
            i_max = i
            j_max = j
        #print result
        
print "Resultat max: "+str(maximum)+" with percentage_learning = "+str(i_max)+", number_cuts = "+str(j_max)
        

    


