# Cleaning, Organizing, and store the data in the database 

# Common data cleaning steps on all text:
    # Make text all lower case
    # Remove punctuation
    # Remove numerical values
    # Remove common non-sensical text (/n)
    # Tokenize text
    # Remove stop words


# Import Libraries
import string
import re

class CleanData:
    def __init__(self, id):
        self.id = id
    
    def cleanText(self, text):        
        # Make text lowercase
        text = text.lower()
        
        # remove text in square brackets
        text = re.sub('\[.*?\]', '', text)

        # remove punctuation
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        
        # remove words containing numbers
        # text = re.sub('\w*\d\w*', '', text)
       
        print(text)
        
        # return text

    def cleanSubmission(self):
        pass

    def cleanComment(self):
        pass

a = CleanData("aasd")
a.cleanText("""Best. Rode HyLN from $15 to $45


Worst: bought Baba at $280 and sold at $219""")