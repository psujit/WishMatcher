# -*- coding: UTF-8 -*-
import os
import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.tag.stanford import StanfordNERTagger

def findKeyword( requestParameter ):
    "This function finds the key word to be searched"
    path_to_model = os.path.join(os.path.expanduser('~'), 'nltk_data', 'taggers', 'stanford-ner-2014-08-27','classifiers','english.all.3class.distsim.crf.ser.gz')
    path_to_jar = os.path.join(os.path.expanduser('~'), 'nltk_data', 'taggers', 'stanford-ner-2014-08-27','stanford-ner.jar')
    tagger = nltk.tag.stanford.StanfordNERTagger(path_to_model, path_to_jar)
    tokenized = nltk.word_tokenize(requestParameter)
    tagged_text = tagger.tag(tokenized)
    keyWordToSearch = ""
    for x in tagged_text:
        if(x[1]=="ORGANIZATION"):
            keyWordToSearch += ' '+ x[0]
    if(keyWordToSearch == ""):
        listOfKeywordsToOmit = ["Looking for", "I need", "I am looking for", "I want"]
        keyWordToSearch = ""
        for x in listOfKeywordsToOmit:
            if(requestParameter.find(x)!=-1):
                keyWordToSearch = requestParameter[requestParameter.find(x)+len(x):]
        #keyWordToSearch = keyWordToSearch.lstrip(' ')
    if(keyWordToSearch == ""):
        keyWordToSearch = requestParameter
    keyWordToSearch = keyWordToSearch.strip()
    return keyWordToSearch

def removeArticle( requestParameter ):
    "This function removes the article the key word to be searched"
    listOfKeywordsToOmit = ["a ", "an ", "the "]
    keyWordToSearch = requestParameter
    for x in listOfKeywordsToOmit:
        if(requestParameter.find(x)!=-1):
            keyWordToSearch = requestParameter[requestParameter.find(x)+len(x):]
    #keyWordToSearch = keyWordToSearch.lstrip(' ')
    keyWordToSearch = keyWordToSearch.strip()
    return keyWordToSearch