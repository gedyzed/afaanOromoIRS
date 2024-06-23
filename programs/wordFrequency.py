import pickle
import matplotlib.pyplot as plt
import numpy as np
from Assignment.textProcessor import Stemmer
from textExtractor import Binary

class WordFrequency: 

    def sortedWordFrequency(self):
        binary = Binary()
        documentWords = binary.read('corpus.bin')
        wordFrequency = {}
          
        for doc in documentWords:
            for word, freq in doc.items():
                if word in wordFrequency:
                    wordFrequency[word] += freq
                else: 
                    wordFrequency[word] = freq   
                    
        # Sort the word frequency in descending order               
        sortedWordFrequency = dict(sorted(wordFrequency.items(), key=lambda item: item[1], reverse=True))
                   
        return sortedWordFrequency   
    
    def drawGraph(self):
        wordFrequency = self.sortedWordFrequency()
        ranks = {}
        
        for i, values in enumerate(wordFrequency.values()):
            ranks[i + 1] = values
            if i == 200:
                break
        
        rank = list(ranks.keys())
        frequency = list(ranks.values())

        # Plot the graph as a bar plot
        plt.bar(rank, frequency)
        plt.xlabel('Rank')
        plt.ylabel('Frequency')
        plt.title('Rank Vs Frequency of Corpus Words')
        plt.grid(True)
        plt.show()

    def plot_zipf_log_log(self):
        wordFrequency = self.sortedWordFrequency()
        ranks = np.arange(1, len(wordFrequency) + 1)
        frequencies = np.array(list(wordFrequency.values()))

        plt.figure(figsize=(10, 6))
        plt.loglog(ranks, frequencies, marker="o", linestyle="none")
        plt.xlabel("Rank")
        plt.ylabel("Frequency")
        plt.title("Total Corpus Rank vs. Frequency")
        plt.grid(True)
        plt.show()

# Example usage
word_frequency = WordFrequency()
word_frequency.drawGraph()
word_frequency.plot_zipf_log_log()
