import os
from gensim.models import *
trainingdir = os.path.join(os.path.expanduser('~'), 'word2vec', 'trunk/') # Directory of training file.
sentences = word2vec.Text8Corpus(trainingdir+'text8')
model = word2vec.Word2Vec(sentences, size=60, window=5, min_count=1)
model.save(os.path.join(os.path.expanduser('~'), 'Text Mining', "model"))