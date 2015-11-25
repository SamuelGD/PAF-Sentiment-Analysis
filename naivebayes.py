#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from math import log, floor
from sys import maxint
from documents import build_vector
from xmlparser import true_list
 
class Conditional_Probability:
# Contains P(t | c) 
    
    def __init__(self, conditional_probability_dic):
        self.conditional_probability_dic = conditional_probability_dic
    
    def get_log(self, c, t, neutral):
        if t in self.conditional_probability_dic[c]:
            return log(self.conditional_probability_dic[c][t])
        elif neutral:
            return - maxint - 1 
        else:
            return 0

class Result_Training:
# Contains P(c) and P(t | c)
    
    def __init__(self, prior, conditional_probability):
        self.prior = prior
        self.conditional_probability = conditional_probability         

def training_nb(documents, neutral):
    # The function for training with Naive Bayes
	# documents is a list of Document classes
    total_number_documents = len(documents)
    
    if total_number_documents == 0:
        return None
    
    if neutral:
        number_documents = [0., 0., 0.]
    else:
        number_documents = [0., 0.]
    
    number_classes = 2
    if neutral:
        number_classes = 3
 
    
    for document in documents:
        if document.opinion == 1:
            number_documents[1] += 1 # number of documents having a positive opinion
        elif document.opinion == 0:
            number_documents[0] += 1 # number of documents having a negative opinion
        elif neutral:
            number_documents[2] += 1 # number of documents having a neutral opinion

    if neutral:
        prior = [0., 0., 0.]
    else:
        prior = [0., 0.]
    
    for c in range(0, number_classes):
        prior[c] = number_documents[c] / total_number_documents

        
        
    # We browse every word in every document to find the number of occurences 
    # t is an array of dictionaries, for example t[1][word] returns the number of occurences for the word in the documents beloging to class 1 (positive opinion)     
    
    if neutral:
        t = [{}, {}, {}]
    else:
        t = [{}, {}]
        
    for document in documents:      
        for word in document.vector:
            
            if word in t[document.opinion]:
                t[document.opinion][word] += 1
            else:
                t[document.opinion][word] = 1
                
    # We calculates conditional probability P(word | c)
    
    
    if neutral:
        conditional_probability_dic = [{}, {}, {}]
    else:
        conditional_probability_dic = [{}, {}]
        
    if neutral:
        number_words = [0., 0., 0.] # the number of words in class c
    else:
        number_words = [0., 0.]
    
    for c in range(0, number_classes):
        for n in t[c].values():
            number_words[c] += n + 1
            
        
    for c in range(0, number_classes):
        for word in t[c].keys():
            conditional_probability_dic[c][word] = (t[c][word] + 1) / number_words[c]
            
    conditional_probability = Conditional_Probability(conditional_probability_dic)
    
    
    result = Result_Training(prior, conditional_probability)
    return result    

def apply_nb(result_training, test_vector, neutral):
    # The function for evaluation with Naive Bayes

    if result_training is None:
        return -1 # error
    
    if neutral and test_vector == set([]):
            return 2
    
    if neutral:
        score = [0., 0., 0.]
    else:
        score = [0., 0.]

    number_classes = 2
    if neutral:
        number_classes = 3
    
    
    for c in range(0, number_classes):
        proba_c = result_training.prior[c]
        
        if(proba_c > 0):
            score[c] = log(proba_c)
        else:
            score[c] = 0
    
    for c in range(0, number_classes):
        for word in test_vector:
            score[c] += result_training.conditional_probability.get_log(c, word, neutral)
    
    maximum = score[0]
    result = 0  
    
    for c in range(1, number_classes):
        if score[c] > maximum:
            maximum = score[c]
            result = c
            
    return result
		
def apply_nb_text(result_training, test_text, neutral):
    vector = build_vector(test_text, neutral) # we get the vector representing the text test_document
    
    int_result = apply_nb(result_training, vector, neutral)
    
    if int_result == 1:
        return "positive"
    elif int_result == 0:
        return "negative"
    else:
        return "neutral"

 
def validation(index_start, percentage_training, neutral):
    length = len(true_list)
    
    size = floor(length*(percentage_training/100.))
    size = int(size)
    
    training_list = []
    test_list = []
    
    index_end = (index_start + size) % (length)
    
    if index_end < index_start:
        training_list = true_list[index_start:] + true_list[0: index_end]
        test_list = true_list[index_end : index_start]
    else:
        training_list = true_list[index_start : index_end]
        test_list = true_list[index_end :] + true_list[0 : index_start]
    
    
    training_result = training_nb(training_list, neutral)
    
    return evaluate(test_list, training_result, neutral)
    
def cross_validation(number_rotations, percentage_training, neutral):
    length = len(true_list)
    
    percentage_results = []
    
    for i in range(0, number_rotations):
        percentage_result = validation(i * (length / number_rotations), percentage_training, neutral)
        percentage_results.append(percentage_result)
        
    if percentage_results != []:
        return max(percentage_results)
    else:
        return 0
        
def evaluate(documents_test, training_result, neutral):
# Tests the documents from documents_test and returns a percentage of success
    
    number_documents = len(documents_test)
    number_success = 0
   
 
    
    #resultats = [[0,0,0], [0,0,0], [0,0,0]]
    
    for document in documents_test:        
        result_evaluation = apply_nb(training_result, document.vector, neutral)
        
        #resultats[document.opinion][result_evaluation] += 1
        if result_evaluation == document.opinion:
            number_success += 1
            
          
    percentage_success = float(number_success) / float(number_documents) * 100
    return percentage_success
    