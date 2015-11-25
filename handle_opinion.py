#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from naivebayes import training_nb, apply_nb_text
from xmlparser import get_documents, true_list
import sys
import pickle
import os.path

def store_training(neutral):
    if neutral:
        database_name = "database3"
    else:
        database_name = "database2"
        
    get_documents(15, neutral)
    training_result = training_nb(true_list, neutral)
 
 
    with open(database_name, 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(training_result)
         
def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s text number_classes' % sys.argv[0])
       
    if sys.argv[2] == "3":
        neutral = True
    else:
        neutral = False
        
    if neutral:
        database_name = "database3"
    else:
        database_name = "database2"
	
    if os.path.isfile(database_name) == False:
        store_training(neutral)
    
    training_result = None
    
    with open(database_name, 'rb') as file:
        my_depickler = pickle.Unpickler(file)
        training_result = my_depickler.load()	

    result = apply_nb_text(training_result, sys.argv[1], neutral)
	
    print result

main()

"""for element in true_list:
    print "DBG: "+str(element.opinion)+" "+str(element.vector)"""

    


