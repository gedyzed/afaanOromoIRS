class Tokenizer:
    
    def tokenize(self,word):
        cleanWord = ""
        for letter in word:
            if letter.isalpha(): # checks whether the letter is an alphabet 
                cleanWord += letter 
  
        return cleanWord.lower()  #normalize the word 
    
class StopWord:
    def  __init__ (self,wordFrequency):
            self.wordFrequency = wordFrequency
    def remove(self):
        """
        From our study of the stastical property we have identified most 
            of the words repeated most are stop words. 
            upperCutOffFrequency = 950 
            lowerCutOffFrequency = 10
        """     
        #based on frequency 
        upperCutOff = 950
        lowerCutOff = 10
            
        # removeStopWords
            
        nonStopWords = {}
        for word,value in self.wordFrequency.items():
            if value < 950 and value >= 10:
                nonStopWords[word] = value
                
        return nonStopWords    
    
class Stemmer:
    """
    Usage:
    
    >>> stemmer = Stemmer()
    >>> stemmer.rule_cluster_7("gaggabaabaa") 
    
    Or
    
    >>> stemmer.stem(word_token) 
    
    If we have a list of tokenized words:
    
    >>> [stemmer.stem(word_token) for word_token in word_tokens]
    
    """
    def __init__(self):
        pass

    def apply_cluster_rules(self, word):
        # Define rule clusters
        clusters = [
            
            self.rule_cluster_1,
            self.rule_cluster_2,
            self.rule_cluster_3,
            self.rule_cluster_4,
            self.rule_cluster_5,
            self.rule_cluster_6,
            self.rule_cluster_7,
        
        ]
        
        # Apply rules from each cluster
        stemmed_word = word
        while True:
            previous_word = stemmed_word
            for cluster in clusters:
                stemmed_word = cluster(stemmed_word)
                if stemmed_word is None:
                    stemmed_word = previous_word
            if stemmed_word == previous_word:
                break
        return stemmed_word

    def measure(self, word):
        # Calculate the number of vowel-consonant sequences in the word
        vowels = set("aeiou")
        measure = 0
        consecutive_vowel = False
        for char in word:
            if char.lower() in vowels:
                if not consecutive_vowel:
                    measure += 1
                    consecutive_vowel = True
            else:
                consecutive_vowel = False
        return measure

    def stem(self, word):
        return self.apply_cluster_rules(word)

    def rule_cluster_1(self, word):
        suffixes = ["olee", "olii", "oolii", "oota", "ota", "oolee", "icha", "ichi", "oma", "fis", "siis", "ooma", "siif", "fam", "ata"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    return word[:-len(suffix)]
        return word
    def rule_cluster_3(self, word):
        suffixes = ["eenya", "ina", "offaa", "annoo", "umsa", "ummaa", "insa", "iinsa", "am", "ni", "affaa"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    if word[:-len(suffix)] and word[:-len(suffix)][-1] in "bcdfghjklmnpqrstvwxyz":
                        return word[:-len(suffix)]
        return word

    def rule_cluster_4(self, word):
        suffixes = ["`aa", "’uu", "’ee", "`a", "’e", "’u", "s", "sii", "suu", "sa", "se", "si", "ssi", "sse", "ssa", "nye", "nya"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif self.measure(word) == 0:
                    return word[:-len(suffix)] + "`"
        return word

    def rule_cluster_5(self, word):
        special_cases = {
            "du": "to",
            "di": "to",
            "dan": "to",
            "lee": "la",
            "wwan": "sa",
            "een": "af",
            "an": "af",
            "f": "sha",
            "n": "sha"
        }

        for suffix, condition in special_cases.items():
            if word.endswith(suffix):
                if condition == "to":
                    preceding_chars = word[:-len(suffix)]
                    if preceding_chars.endswith(("b", "g", "d")):
                        if self.measure(word) >= 1:
                            return word[:-len(suffix)]
                        elif self.measure(word) == 0:
                            return word[:-len(suffix)] + "d"
                elif suffix == "lee" and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix in ["wwan", "een"] and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix == "an" and self.measure(word) >= 1:
                    return word[:-len(suffix)]
                elif suffix in ["f", "n"] and self.measure(word) >= 1:
                    return word[:-len(suffix)]
        return word

    def rule_cluster_6(self, word):
        suffixes = ["te", "tu", "ti", "tee", "tuu", "ne", "nu", "na", "nne", "nnu", "nna", "dhaa", "chaaf", "dhaaf", "tiif", "ach", "adh", "chuu", "at", "att", "ch", "tanu", "tanuu", "tan", "tani"]
        for suffix in suffixes:
            if word.endswith(suffix):
                if self.measure(word) >= 1:
                    return word[:-len(suffix)]
                else:
                    return word[:-len(suffix)] + "t"
        return word

    def rule_cluster_7(self, word):
        if len(word) <= 3:
            return word
        if not word.startswith(("a", "e", "i", "o", "u")):
            if word[:2] == word[3:5]:
                return word[3:]
            elif word[:2] == word[2:5]:
                return word[2:]
        if word.startswith(("a", "e", "i", "o", "u")):
            if word[:2] == word[2:4] or "'" in word or "h" in word:
                word = word.replace("'", word[3:4])
                word = word.replace("h", word[3:4])
                if word[:2] == word[2:4]:
                    return word[2:]
        return word
    def rule_cluster_2(self,word):
        suffixes = ["ittii", "ttii", "tii", "irra", "rra"]
        for suffix in suffixes:  
            if word.endswith(suffix):
                word_base = word[:-len(suffix)]
                if self.measure(word) >= 1 or word_base.endswith("ti"):
                    return word_base
        return word   
    
