# Since the api will allow user to request by number of sentences
# The raw quotes need to be separated into their constituent sentences
# However, I want the lorem ipsum response to still have some sort of coherence
# So ideally sentences from the same quotes should appear together. Hence this processing.


from raw_quotes import rawQuotes
import re
import json

def processQuotes(quotes):
    quotesList = []
    for i, q in enumerate(quotes):
        # using regex to get a list of sentence(s) from each quote
        sentenceList = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', q)
        quotesDict = {}
        quotesDict['id'] = i
        quotesDict['sentence'] = sentenceList
        quotesDict['length'] = len(sentenceList)
        quotesList.append(quotesDict)
    return quotesList


# store the quotesList as a pickled file
def pickleQuotesList(quotesList):
    with open('processed_quotes.txt', 'w') as filehandle:
        # store the data as json
        json.dump(quotesList, filehandle)
    return


if __name__ == "__main__":
    quotesList = processQuotes(rawQuotes)
    pickleQuotesList(quotesList)
