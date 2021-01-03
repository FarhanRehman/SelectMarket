# 1) Getting the data - in this case, we'll be scraping data from a website

# Import Libraries
from nltk import tokenize
import yfinance as yf
import timeit
from Database.db import DatabaseManager
import re


# starttime = timeit.default_timer()
# print("The time difference is :", timeit.default_timer() - starttime)

# TODO: add relative imports & fix file structures
# TODO: Set up CI/CD
# TODO: Set up sqlite databasse (inside DB, keep count of number of mentions and positions)
# TODO: should also recognize tickers by company names
# TODO: start scraping user positions on stocks


class GetData:
    def __init__(self, subreddit):
        # Initialize Variables
        self.subreddit = subreddit
        self.blacklistTickers = ["YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH", "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP", "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE", "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD", "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM", "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW" "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ", "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE" "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT", "GG", "ELON", "RSI", "CCP", "EOD", "EOY"]


    # TODO: make this faster
    # TODO: recognize tickers that are misspelled, lowercase, using the company name instead of ticker
    def valtiadeTickers(self, tickers):
        valid = set()
        db = DatabaseManager()
        for ticker in tickers:
            if ticker not in self.blacklistTickers:
                # is it faster to search many at a time or one by one?
                # search csv file for ticker to check if it is valid
                if db.searchString(ticker):
                    valid.add(ticker)

                # with open('C:/Users/farha/Documents/GitHub/SelectMarket/SentimentAnalysis/Reddit/STOCKS.csv', 'rt') as csvfile:
                #     my_content = csv.reader(csvfile, delimiter=',')
                #     for row in my_content:
                #         if ticker in row:
                #             valid.add(ticker)

        return valid

    # TODO: sentiment analysis comment with many tickers
    # TODO: return dict with cleaned data as well so sentiment analysis can be Preformed


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

    # This function wil parse all tickers and related text from a submission/comment, and output it in a dictionary/csv
    def parseTickers(self, text):
        # GET CLEANED DATA HERE
        
        text = text.replace('\n','')
        text = text.replace('\t','')
        
        # Regex to identify stock tickers, we use a set here to avoid duplicates
        tickers = set(re.findall("(?:(?<=\A)|(?<=\s)|(?<=[$]))([A-Z]{1,5})(?=\s|$|[^a-zA-z])", text))

        # loop through tickers and verify valid ones
        tickers = self.valtiadeTickers(tickers)

        # turn set into dictionary
        tickers = dict.fromkeys(tickers, 0)
        

        if len(tickers) == 1:
            tickers = {tickers[0]: text}
        else:

            # TODO: check out some ways to split into sentences (should seperate by \n as well), check out nltk and regex examples
            # https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences

            # seperate tickers based on sentences
            # sentences = tokenize.sent_tokenize(text)
            # print(sentences)

            sentences = self.split_into_sentences(text)
            # print(sentences)
            # print(sentences)

            # TODO: if ticker appears twice it will overright so find a fix for that
            # assign each ticker the sentence it was included in
            for sentence in sentences:
                for key in tickers:
                    if key in sentence:
                        tickers[key] = sentence
        print(tickers)


r = GetData("WallStreetBets")
r.parseTickers("""
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
