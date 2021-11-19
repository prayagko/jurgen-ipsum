Lorem Ipsum made from Jurgen Klopp quotes. Hosted on AWS Lambda.

**API**

Endpoint: https://t3ygzbl2q0.execute-api.ap-southeast-2.amazonaws.com/default/jurgen-ipsum

Method: Get

Query Parameters:

  **'type'**  
        value: "sentence" or "paragraph"  
        default value: "sentence"  
        required: false  
  
  **'number'**  
        value: digit > 0       e.g. "4"  
        default value: "6"  
        required: false  
        description: Number of sentences or paragraphs you want.  

  **'para-size'**  
        value: digit > 0       e.g. "4"  
        default value: "7"  
        required: false  
        description: Number of sentences you want per paragraph. This parameter ignored unless type is "paragraph".
