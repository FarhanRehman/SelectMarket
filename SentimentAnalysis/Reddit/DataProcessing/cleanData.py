# Cleaning, Organizing, and store the data in the database 

# Common data cleaning steps on all text:
    # Make text all lower case
    # Remove punctuation
    # Remove numerical values
    # Remove common non-sensical text (/n)
    # Tokenize text
    # Remove stop words

# https://realpython.com/sentiment-analysis-python/#using-natural-language-processing-to-preprocess-and-clean-text-data


# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value



# Import Libraries
from nltk import tokenize
import string
import spacy
import nltk
import re

class CleanData:
    def __init__(self, text):
        self.text = text
        self.blacklistWords = ["YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH", "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP", "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE", "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD", "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM", "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW" "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ", "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE" "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT", "GG", "ELON", "RSI", "CCP", "EOD", "EOY", "I"]
    

    def cleanTextRoundOne(self):
        # TODO: make this custom to format on r/WSB

        # CLean text so its easier to identify tickers

        # remove custom stop words
        # self.text  = [word for word in re.split("\W+", self.text) if word.lower() not in self.blacklistTickers]
        # self.text = ' '.join(self.text)

        # Tokenizing with spacy
        # nlp = spacy.load("en_core_web_sm")
        # doc = nlp(self.text)
        # token_list = [token for token in doc]

        # Add custom stopwords to NLTK stopwords list
        stopwords = nltk.corpus.stopwords.words('english')
        stopwords.extend(self.blacklistWords)

        # Remove stop words using NLTK
        self.text = [word for word in self.text.split() if word not in stopwords]
        self.text = ' '.join(self.text)

        # remove standard stop words with spacy
        # nlp = spacy.load("en_core_web_sm")
        # sentence = nlp(self.text)        

        # # Normalizing Words with spacy
        # lemmas = [f"Token: {token}, lemma: {token.lemma_}" for token in filtered_tokens]
        # print(lemmas)

        # seperate tickers based on sentences
        # sentences = tokenize.sent_tokenize(text)
        # print(sentences)


        
        return self.text

    def cleanTextRoundTwo(self):
        # clean text to get extra ready for sentiment analysis

        # Vectorizing Text with spacy
        # a = filtered_tokens[1].vector
        # print(a)
        # self.text = self.text.replace('\n','')
        # self.text = self.text.replace('\t','')
        pass

    def split_into_sentences(self, text):
        alphabets= "([A-Za-z])"
        prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
        suffixes = "(Inc|Ltd|Jr|Sr|Co)"
        starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
        acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
        websites = "[.](com|net|org|io|gov)"

        text = " " + text + "  "
        text = text.replace("\n"," ")
        text = re.sub(prefixes,"\\1<prd>",text)
        text = re.sub(websites,"<prd>\\1",text)
        if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
        text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
        text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
        text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
        text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
        text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
        if "”" in text: text = text.replace(".”","”.")
        if "\"" in text: text = text.replace(".\"","\".")
        if "!" in text: text = text.replace("!\"","\"!")
        if "?" in text: text = text.replace("?\"","\"?")
        text = text.replace(".",".<stop>")
        text = text.replace("?","?<stop>")
        text = text.replace("!","!<stop>")
        text = text.replace("<prd>",".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences

# a = CleanData("""I would take profits on SQ, SBE, TSLA (sooner than later), and FB. Most of these are run up beyond reason. The mania will correct at some point and you don't want to be bag holding. Vertical green lines are not normal. Also you can get back in when they cool off.


# I personally am moving out from Google and Facebook. Antitrust may take some time but I personally don't want to invest in pure ads. AMZN and AAPL in comparison are more diversified revenue streams. Wouldn't take as big of a topple if the government broke them up.


# My portfolio for reference AAPL, MSFT, AMZN, GOOGL, AMD, NVDIA, DIS, NFLX, TSLA. I plan to transition out of AMD, GOOGL, and TSLA at some point. TSLA probably soon. AMD and GOOGL are holds for now. AAPL is my largest holding. I believe MSFT and AMZN are coming for that top spot with Azure and AWS.""").cleanText()