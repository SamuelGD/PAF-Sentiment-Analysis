#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from nltk import WordNetLemmatizer, RegexpTokenizer, pos_tag

class Document:
# A document is defined by its vector and its opinion
    
    def __init__(self, vector, opinion):
        self.vector = vector
        
        if opinion == "positive":
            self.opinion = 1; # positive opinion
        elif opinion == "negative":
            self.opinion = 0; # negative opinion
        else:
            self.opinion = 2; # neutral opinion

def fetch_text(file_name, start, end):
# Fetch the text starting with index start and ending with index end in the .ac file 
    
    with open(file_name, 'r') as file_aa:
        contents = file_aa.read()
        return contents[start : end]
        
def lemmatize(word):    
    wordnet_lemmatizer = WordNetLemmatizer()
    return wordnet_lemmatizer.lemmatize(word)  
    
def build_vector(text, neutral):
    # We tokenize the text 
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    if neutral:
        tokens = pos_tag(tokens) # we add POS tag
        forbidden_pos = ['RB', 'RBS', 'RBR', 'CC', 'CD', 'DT', 'EX', 'IN', 'LS', 'PDT', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'WDT', 'WP', 'WP$', ]
 
    # We build the document vector
    vector = set()
    for couple in tokens:

        if neutral:
            if (couple[1] in forbidden_pos):
                continue
        
            vector.add(lemmatize(couple[0]))
        else:
            vector.add(lemmatize(couple))
		
    return vector