import pickle
import math
from collections import defaultdict
from Assignment.textProcessor import Stemmer,Tokenizer


class SimilarityCalculator:
    
    def __init__(self,documentWords,invertedIndex,document_ids):
        self.documentWords = documentWords
        self.invertedIndex = invertedIndex
        self.document_ids = document_ids
        self.documentNames = [
                                'Afaan Oromoo Kutaa 7.pdf',
                                'Afaan Oromoo Kutaa 8.pdf',
                                'Afaan-Oromoo-Grade-9.pdf',
                                'Hammattoo_Manni_Barumsaa_Sadarkaa_2ffaa_Addaa_ittiin_Hundeeffamuufi.pdf',
                                'Kitaabota.pdf',
                                'onnee dhugaa .pdf',
                                'Qajeelcha Barsiisaa kutaa 11 .pdf',
                                'Qajeelcha Barsiisaa kutaa 12 .pdf',
                                'Saayinsii Waliigalaa Kutaa-8.pdf',
                                'Seera Yakkaa  Rippaabilika Dimokraatawaa Federaalawaa Itoophiyaa.pdf',   
                                #add your file names here   
                            ]
        self.document_id_to_name = {f"doc_{index + 1}": name for index, name in enumerate(self.documentNames)}
        
    def calculate_tf(self,term, document):
        if document.get(term):
            return document[term]
        return 0
    def calculate_idf(self,term):
        document_frequency = len(self.invertedIndex.get(term, {}))
        total_documents = len(self.documentWords)
        return math.log(total_documents / (document_frequency + 1))
    def calculate_tfidf(self,term, document):
        tf = self.calculate_tf(term, document)
        idf = self.calculate_idf(term)
        return tf * idf
    def calculate_cosine_similarity(self,query, document):
        numerator = sum(query[term] * self.calculate_tfidf(term, document) for term in query)
        query_magnitude = math.sqrt(sum(query[term] ** 2 for term in query))
        document_magnitude = math.sqrt(sum(self.calculate_tfidf(term, document) ** 2 for term in document))
        if query_magnitude == 0 or document_magnitude == 0:
            return 0
        return numerator / (query_magnitude * document_magnitude)
    def process_query(self,query):
        stemmer = Stemmer()
        tokenizer =  Tokenizer()
        
        # Preprocess the query to get the cleaned and stemmed terms
        cleaned_query = query.split()
        tokens = [tokenizer.tokenize(word) for word in cleaned_query]
        stemmed_query = [stemmer.stem(word) for word in tokens]

        query_tf = defaultdict(int)
        for term in stemmed_query:
            query_tf[term] += 1

        # Calculate the cosine similarity between the stemmed query and each document
        similarity_scores = {}
        for i, document in enumerate(self.documentWords):
            stemmed_document = {stemmer.stem(term): freq for term, freq in document.items()}
            similarity_scores[self.document_ids[i]] = self.calculate_cosine_similarity(query_tf, stemmed_document)

        # Sort the documents based on similarity scores in descending order
        sorted_documents = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
        retrievedDocuments = []
        
        for index,(id,score) in enumerate(sorted_documents):   
            if score != 0:
                retrievedDocuments.append(self.document_id_to_name[id])
            if index == 6: break     

        return retrievedDocuments
