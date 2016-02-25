# -*- coding: UTF-8 -*-
import os
import nltk
import spotlight
from luceneSearch import *
from nltk import word_tokenize
from nltk import pos_tag
from nltk.tag.stanford import StanfordNERTagger
from gensim.models import *

def findMatchesFromDBPedia(requestParameter):
    "This function finds details from DBPedia Spotlight"
    annotations = spotlight.annotate('http://spotlight.sztaki.hu:2222/rest/annotate',requestParameter, confidence=0.4, support=0,spotter='Default')
    matches = annotations[0]['types'] 
    print(matches[matches.rfind(':')+1:])
    searchMatches = searchLucene(matches[matches.rfind(':')+1:])
    print len(searchMatches)
    return searchMatches


def findMatchesFromWord2Vec(requestParameter):
    "This function finds matches from DBPedia"
    model = Word2Vec.load(os.path.join(os.path.expanduser('~'), 'Text Mining', "model"))
    return model.most_similar(requestParameter, topn=10)