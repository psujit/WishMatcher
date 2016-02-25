import sys
import lucene
from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from luceneFunctionalities import *
import time
import datetime

counter = 0

def createind(product,url):
	"This function creates index for lucene"
	global counter
	counter += 1
	adId = counter
	adLine = product
	field_string = chunker(product.lower())
	field_related_words = getDbpediaMatches(product, field_string)
	url = url    

	lucene.initVM()
	# 1. create an index
	index_path = File("Home/WishMatcherIndex")
	analyzer = StandardAnalyzer(Version.LUCENE_4_10_1)
	index = SimpleFSDirectory(index_path)

	# 2. fill the index
	config = IndexWriterConfig(Version.LUCENE_4_10_1, analyzer)
	writer = IndexWriter(index, config)
	#for title in TITLES:
	import time
	millis = int(round(time.time() * 1000))
	
	userid = str(millis)
	
	doc = Document()
	doc.add(Field("AdId", str(adId), Field.Store.YES, Field.Index.ANALYZED))
	doc.add(Field("AdLine", adLine, Field.Store.YES, Field.Index.ANALYZED))
	doc.add(Field("FieldString", field_string, Field.Store.YES, Field.Index.ANALYZED))
	doc.add(Field("FieldRelatedWords", field_related_words, Field.Store.YES, Field.Index.ANALYZED))
	doc.add(Field("URL", url, Field.Store.YES, Field.Index.ANALYZED))
	writer.addDocument(doc)
	print(adId)
	# 3. close resources
	writer.close()
	index.close()	
	return ""