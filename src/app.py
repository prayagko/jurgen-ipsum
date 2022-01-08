import json
import random
from src.lambda_decorators import cors_headers

@cors_headers
def jurgenIpsum(event, context):
    try:
        if event.get('queryStringParameters'):
            number = event['queryStringParameters'].get('number', 6)
            textType = event['queryStringParameters'].get('type', 'sentence')
            paraSize = event['queryStringParameters'].get('para-size', 7)
        else:
            number = 6
            textType = 'sentence'
            paraSize = 7
        try:
            number = int(number)
        except ValueError:
            return {
                "statusCode": 400,
                "body": json.dumps({"Error": "Invalid number value. Ensure that number value is a digit."})
            }

        if number < 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"Error": "Number value should be digit greater than 0."})
            }   
            
        if textType == 'paragraph':
            try:
                paraSize = int(paraSize)
            except ValueError:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"Error": "Invalid para-size value. Ensure that para-size value is a digit."})
                }        
        if textType=='paragraph' and paraSize < 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"Error": "para-size value should be digit greater than 0."})
            }         
        with open('src/processed_quotes.txt', 'r') as filehandle:
            quotesList = json.load(filehandle)
    
        if textType.lower() == 'sentence':
            ipsumSentences = []
            while len(ipsumSentences) < number:
                randomQuote = quotesList[random.randint(0,(len(quotesList)-1))]
                for i in range(int(randomQuote.get('length'))):
                    remainingSentenceSlots = number - len(ipsumSentences)
                    if remainingSentenceSlots >0:
                        if randomQuote.get('sentence'):
                            ipsumSentences.append(randomQuote.get('sentence')[i])
                        else:
                             continue
                    else:
                        break
            ipsum = [' '.join(ipsumSentences)]
        elif textType.lower() == 'paragraph':
            ipsum = []
            for _ in range(number):
                ipsumSentences = []
                while len(ipsumSentences) < paraSize:
                    randomQuote = quotesList[random.randint(0,(len(quotesList)-1))]
                    for i in range(int(randomQuote.get('length'))):
                        remainingSentenceSlots = paraSize - len(ipsumSentences)
                        if remainingSentenceSlots >0:
                            if randomQuote.get('sentence'):
                                ipsumSentences.append(randomQuote.get('sentence')[i])
                            else:
                                continue
                        else:
                            break
                para = ' '.join(ipsumSentences)
                ipsum.append(para)        
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"Error": "text-type value must be either sentence or paragraph"})
            }
        return {
                "statusCode": 200,
                "body": json.dumps({"data": ipsum})
            }
    except Exception as e:
        print('Exception Occured: ', e)
        return {
            "statusCode": 500,
            "body": json.dumps({"Error": "Server Error"})
        }