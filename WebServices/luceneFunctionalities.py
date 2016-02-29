import nltk
from gensim.models import *
import spotlight
import os
from nltk.corpus import wordnet

nounPhrases = ""

def chunker(requestParameter):
    global nounPhrases
    nounPhrases = ""
    tokenized = nltk.word_tokenize(requestParameter)
    tagged = nltk.tag.pos_tag(tokenized)

    chunkgram = "NP: {<DT>?<JJ>*<NN>}"

    chunkparser = nltk.RegexpParser(chunkgram) 
    chunked = chunkparser.parse(tagged)
    nounPhrases = getNodes(chunked)
    return nounPhrases


def getNodes(parent):
    global nounPhrases
    for node in parent:
        if type(node) is nltk.Tree:
            getNodes(node)
        else:
            if(node[1]=='NN' or node[1]=='NNP' or node[1]=='NNS'):
                if(nounPhrases==""):
                    nounPhrases = nounPhrases+' '+node[0]
                else:
                    nounPhrases = nounPhrases+', '+node[0]
    return nounPhrases  

def getWordNetMatches(requestParameter,matchingWords):
    requestParameterList = requestParameter.split(', ')
    for p in requestParameterList:
        matchingWordsInUnicode = []
        for synset in wordnet.synsets(p):
            for lemma in synset.lemmas():
                matchingWordsInUnicode.append(lemma.name())
        matchingWordsInUnicode=(set(matchingWordsInUnicode))
        for x in matchingWordsInUnicode:
            if(matchingWords=="" or matchingWords==" "):
                matchingWords = matchingWords +' '+(x.encode('ascii','ignore'))
            else:
                matchingWords = matchingWords +', '+(x.encode('ascii','ignore'))
        matchingWords = getWordToVecMatches(p,matchingWords)
    return matchingWords

def getDbpediaMatches(requestParameterSelf, requestParameterForward):
    matchingWords = ""
    try:
        annotations = spotlight.annotate('http://spotlight.sztaki.hu:2222/rest/annotate', requestParameterSelf, confidence=0.4, support=0,spotter='Default')
        matches = annotations[0]['types'] 
        typeofline = matches[matches.rfind(':')+1:]
        matchingWords = matchingWords + typeofline
    except:
        ""
    matchingWords = getWordNetMatches(requestParameterForward,matchingWords)
    return matchingWords

def getWordToVecMatches(requestParameter, matchingWords):
    try:
        model = Word2Vec.load(os.path.join(os.path.expanduser('~'), 'Text Mining', "model"))
        wordToVec = model.most_similar(requestParameter.lower().strip(), topn=10)
        for x in range(0,5):
            matchingWords = matchingWords +', '+ wordToVec[x][0]
    except:
        return matchingWords
    return matchingWords