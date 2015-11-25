#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from documents import Document, fetch_text, build_vector  

index_list = []
true_list = []

def get_documents(session_number, neutral):    
    for i in range(0, session_number):
        name = 'sessions/' + str(i+1)
        get_documents_from_file(name, neutral)      

def get_documents_from_file(file_name, neutral):      
    dom = parse(file_name + '.aa')
    handle_dom(dom, neutral)
    
    i = 0    
    while i < len(index_list):
        if( ((index_list[i] == "positive")  or  (index_list[i] == "negative") or (neutral and (index_list[i] == "none"))) and index_list[i-1].isdigit() and index_list[i-2].isdigit() ):                
            text = fetch_text(file_name + ".ac", int(index_list[i-2]) , int(index_list[i-1]) )
            true_list.append(Document(build_vector(text, neutral), index_list[i])  )                

        i = i + 1

def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handle_dom(docs, neutral):
    units = docs.getElementsByTagName("unit")
    handle_units(units, neutral)

def handle_units(units, neutral):
    for unit in units:
        handle_unit(unit, neutral)

def handle_unit(unit, neutral):
    characts = unit.getElementsByTagName("characterisation")
    positions = unit.getElementsByTagName("positioning")
    handle_positions(positions)
    handle_characts(characts, neutral)
    
def handle_characts(characts, neutral):
    for charact in characts:
        handle_charact(charact, neutral)
        
def handle_positions(positions):
    for positioning in positions:
        handle_position(positioning)
        
def handle_charact(charact, neutral):
    featureSets = charact.getElementsByTagName("featureSet")
    handle_feature_sets(featureSets, neutral)
    
def handle_position(positioning):
    starts = positioning.getElementsByTagName("start")
    ends = positioning.getElementsByTagName("end")
    handle_starts(starts)
    handle_ends(ends)
    
def handle_starts(starts):
    for start in starts:
        handle(start)
        
def handle_ends(ends):
    for end in ends:
        handle(end)
        
def handle(handle):
    baliseIndexs = handle.getElementsByTagName("singlePosition")
    handle_index(baliseIndexs)
    
def handle_index(baliseIndex):
    for baliseIndex in baliseIndex:
        write(baliseIndex)
        
def write(baliseIndex):
    index_list.append(baliseIndex.getAttribute('index'))
    
def handle_feature_sets(featureSets, neutral):
    for featureSet in featureSets:
        handle_feature_set(featureSet, neutral)        

def handle_feature_set(featureSet, neutral):
    features = featureSet.getElementsByTagName("feature")
    handle_features(features, neutral)
    
def handle_features(features, neutral):
    for feature in features:
        handle_feature(feature, neutral)
        
def handle_feature(feature, neutral):
    if((get_text(feature.childNodes) == "positive") or (get_text(feature.childNodes) == "negative") or (neutral and (get_text(feature.childNodes) == "none"))):
        index_list.append(get_text(feature.childNodes))        
        
def handleTypes(types):
    for t in types:
        handleType(t)

def handleType(t):
    index_list.append(get_text(t.childNodes))    
