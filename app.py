# app.py
# import re

import json
import random
from quotes import quotes


def jurgenIpsum(event, context):
    
    if event.get('queryStringParameters'):
        number = event['queryStringParameters'].get('number', 6)
        textType = event['queryStringParameters'].get('type', 'sentence')
    else:
        number = 6
        textType = 'sentence'
            
            
    try:
        number = int(number)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps(["Error: Invalid number value"])
        }
    
    # make list of sentence from quotes string
    # sentenceList = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', quotesString)

    if textType.lower() == 'sentence':
        randomSentences = [quotes[random.randint(0,(len(quotes)-1))] for n in range(number)]
        ipsum = [' '.join(sentence for sentence in randomSentences)]
    
    elif textType.lower() == 'paragraph':
        ipsum = []
        for n in range(number):
            para = [quotes[random.randint(0,(len(quotes)-1))] for i in range(6)]
            para = ' '.join(sentence for sentence in para)
            ipsum.append(para)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps(["Error: text-type must be either sentence or pargraph"])
        }

    return {
            "statusCode": 200,
            "content-type": "application/json",
            "body": json.dumps(ipsum)
        }

