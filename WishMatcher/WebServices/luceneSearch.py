import sys
import lucene
from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import IndexReader
from org.apache.lucene.queryparser.classic import *
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from result import result

def searchLucene(requestParameter):
    "this method is used to search Lucene"
    searchResults = []
    requestParameter = requestParameter.replace("/"," ")
    # 1. open the index
    if __name__ == "luceneSearch":
        lucene.initVM()
    analyzer = StandardAnalyzer(Version.LUCENE_4_10_1)
    index = SimpleFSDirectory(File("Home/WishMatcherIndex"))
    reader = IndexReader.open(index)
    n_docs = reader.numDocs()
    print("Index contains %d documents." % n_docs)

    # 2. parse the query from the command line
    fields=["AdLine","FieldString","FieldRelatedWords"]    
    parser = MultiFieldQueryParser(Version.LUCENE_CURRENT, fields, analyzer)
    parser.setDefaultOperator(QueryParserBase.OR_OPERATOR)
    query = MultiFieldQueryParser.parse(parser,requestParameter)
    print(query)

    # 3. search the index for the query
    # We retrieve and sort all documents that match the query.
    # In a real application, use a TopScoreDocCollector to sort the hits.
    searcher = IndexSearcher(reader)
    hits = searcher.search(query, n_docs).scoreDocs

    # 4. display results
    print("Found %d hits:" % len(hits))
    for i, hit in enumerate(hits):
        doc = searcher.doc(hit.doc)
        product = doc.get("AdLine")
        url = doc.get("URL")
        if(doc.get("AdId") != 1200):
            product = product[:-1]
            url = url[:-1]
        print("%d. %s" % (i + 1, doc.get("AdLine")))
        r = result(str(product),str(url))
        searchResults.append(r)

    # 5. close resources
    #searcher.close()
    print(searchResults)
    return searchResults

