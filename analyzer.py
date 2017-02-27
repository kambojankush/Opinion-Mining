import nltk

class Analyzer():
    
    tokenizer = nltk.tokenize.TweetTokenizer()

    def __init__(self, positives, negatives):
        self.positives = set()
        self.negatives = set()
        with open(positives) as lines:
            for line in lines:
                if not line.startswith((";", " ")):
                    self.positives.add(line.rstrip("\n"))
                    
        with open(negatives) as lines:
            for line in lines:
                if not line.startswith((" ",";")):
                    self.negatives.add(line.rstrip("\n"))

    def analyze(self, text):
        
        result = 0
        tokens = self.tokenizer.tokenize(text)
        for word in tokens:
            if word in self.positives:
                l = 1
            elif word in self.negatives:
                l = -1
            else:
                l = 0
            result += l
        return result
