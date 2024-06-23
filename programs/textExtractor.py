import os # used to iterate thourgh a folder
import pickle # Used to read and write file in binary
from pdfminer.high_level import extract_text  # type: ignore # Used for extracting text for the documents
from Assignment.textProcessor import Tokenizer

class TextExtractor:
     
    def extractText(self,directory_path):
        corpusWords = []
        
        tokenizer = Tokenizer () # creating instance of Tokenizer class 

        for fileName in os.listdir(directory_path):
            filepath = os.path.join(directory_path, fileName)
            doc = {}
            with open(filepath) as pdfile:
                text = extract_text(filepath)
                for word in text.split():
                    cleanWord = tokenizer.tokenize(word)
                    if cleanWord in doc and len(cleanWord) > 3:    # check if the word is in the document
                            doc[cleanWord]+= 1     
                    elif len(cleanWord) > 3 : # Add the word into the doc if not exist 
                            doc[cleanWord] = 1   
            corpusWords.append(doc)  
            binary = Binary()
        binary.save(corpusWords,"corpus.bin")                                       
        return corpusWords      

 
class Binary:
        
    def save(self,data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Data saved to binary file!")
        
    def read(self,filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data    
text = TextExtractor()
text.extractText("C:\\Users\\ETHIOPIA\\Desktop\\IR project\\IR project\\documents")