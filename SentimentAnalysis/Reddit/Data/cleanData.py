# Cleaning, Organizing, and store the data in the database 

# Common data cleaning steps on all text:
    # Make text all lower case
    # Remove punctuation
    # Remove numerical values
    # Remove common non-sensical text (/n)
    # Tokenize text
    # Remove stop words

# https://realpython.com/sentiment-analysis-python/#using-natural-language-processing-to-preprocess-and-clean-text-data

# Import Libraries
import string
import re
from nltk import tokenize
from nltk.corpus import stopwords

class CleanData:
    def __init__(self, text):
        self.text = text
        self.blacklistTickers = ["YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH", "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP", "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE", "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD", "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM", "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW" "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ", "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE" "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT", "GG", "ELON", "RSI", "CCP", "EOD", "EOY"]
    
    def cleanText(self, text):        
        # Make text lowercase
        text = text.lower()
        
        # remove text in square brackets
        text = re.sub('\[.*?\]', '', text)

        # remove punctuation
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        
        # remove words containing numbers
        # text = re.sub('\w*\d\w*', '', text)
       
        text = text.replace('\n','')
        text = text.replace('\t','')


        text = [word for word in text.split() if word not in stopwords.words('english')]
        text = ' '.join(text)

        print(text)
        
        # return text

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


a = CleanData("aasd")
a.cleanText("""
I know everyone is already holding $GME and $PLTR until they lands on the moon but maybe we can find out what new tickers everyone is holding, why and what are their expectations.


Here is a list of my current positions;


* 70 shares of $BABA at an average of $245 with a price target of $265, where I'll liquidate unless the political environment gets better.

* COVID proof

* Solid financials, much more liquid than Amazon

* China is bound to become the largest economy

* Political uncertainties are exaggerated

* 70 shares of $CRM at $221 with a price target of $230. Have made this same play quite a few times in the last 2 months.

* COVID proof

* A solid company run by a solid CEO with good growth and financials

* Slack was purchased for $28b but the market has wiped 26% of its market cap off, which is more than $50b so at the very least the overreaction is extended by at least $22b (a 10% increase in market cap from current levels)

* Short-term PT of $230 but have no doubt this can break above $275 in 2021. A 24% upside.

* 24 shares of $FB at $273 with a price target of $280. Have also done this multiple times during the last few months.

* COVID proof

* Earnings coming up near the end of January.

* Zuck might be a lizard, but those IG "influencers" you follow from your fake account so your girlfriend doesn't find out will only keep luring you back in.

* Political risks surrounding breakup are exaggerated and seem to be an optic play to gain public confidence. Even if this is not the case, the first hearing is years away.

* Has the potential to breach $325 during 2021. An upside of 20%.

* 4 shares of $AMZN at $3250 with a price target of $3350 at least. Have made a bit over $5k only trading swings between $3000 and $3350.

* COVID proof

* Earnings coming up near the end of January.

* Possible to reach ATH which is around $3500 near earnings.

* Possible to breach $4000 during the year providing an upside of 23%.

* 275 shares of $PFE at average $38.62 with a price target of $41-42, not sure how this will go. Have made this play once before when I cashed out at $42.75 just a few weeks ago.

* Only speculative play in my portfolio

* Not a hold in the long run as this stock is as limp as they come but a reasonable dividend yield. So, not really worried about losing money.


Pretty boring shit, no $GME or $PLTR here but looking forward to seeing what other tickers the community is holding on to.
""")
