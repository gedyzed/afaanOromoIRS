from textExtractor import Binary
from Assignment.textProcessor import Stemmer,StopWord
from WordFrequency import WordFrequency


class InvertedIndex:
    
    def getInvertedIndex(self, documentWords, document_ids):
        stemmer = Stemmer()
        words = WordFrequency()
        wordFrequency = words.sortedWordFrequency()
        stopword = StopWord(wordFrequency)
        indexTerms = stopword.remove()
        indexTerms = [stemmer.stem(word) for word in indexTerms.keys()]
        invertedIndex = {}

        for i, wordFrequency in enumerate(documentWords):
            for word, frequency in wordFrequency.items():
                # Stem the word
                stemmedWord = stemmer.stem(word)
                if stemmedWord in indexTerms:
                    if stemmedWord not in invertedIndex:
                        invertedIndex[stemmedWord] = {}
                    # Add the document to the inverted index
                    invertedIndex[stemmedWord][document_ids[i]] = frequency
        sorted_index = dict(sorted(invertedIndex.items()))
    
        return sorted_index

    def writeInvertedIndexToFile(self, invertedIndex):
        with open('invertedIndex.txt', 'w') as file:
            for term, occurrences in invertedIndex.items():
                total_documents = len(occurrences)
                file.write(f'Term: {term}\n')
                file.write("+" + "-" * 30 + "+" + "-" * 20 + "+" + "-" * 30 + "+\n")
                file.write("|{:^30}|{:^20}|{:^30}|\n".format("Document ID", "Frequency", "Total Documents"))
                file.write("+" + "-" * 30 + "+" + "-" * 20 + "+" + "-" * 30 + "+\n")
                first_row = True
                for doc_id, frequency in sorted(occurrences.items()):
                    if first_row:
                        file.write("|{:^30}|{:^20}|{:^30}|\n".format(doc_id, frequency, total_documents))
                        first_row = False
                    else:
                        file.write("|{:^30}|{:^20}|{:^30}|\n".format(doc_id, frequency, ""))
                file.write("+" + "-" * 30 + "+" + "-" * 20 + "+" + "-" * 30 + "+\n")
                file.write("\n")
