Lorem Ipsum made from Jurgen Klopp quotes.

# **API**


**Endpoint:** https://br2i5iof6e.execute-api.us-east-1.amazonaws.com/

**Method:** Get

## **Query Parameters:**

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
        description: Number of sentences you want per paragraph. This parameter is ignored unless type is "paragraph".
