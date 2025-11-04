import sys
import re
import base64

def base64_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            # Extract the function call part (e.g., "alert(1)")
            function_call = payload[start:]
            
            # Base64 encode the entire function call
            b64_encoded = base64.b64encode(function_call.encode()).decode()
            encoded_payloads.append(f"eval(atob('{b64_encoded}'))")
            
            # Base64 encode just the keyword
            b64_keyword = base64.b64encode(keyword.encode()).decode()
            rest = payload[start + len(keyword):]
            encoded_payloads.append(f"eval(atob('{b64_keyword}')+'{rest}')")
            
            # Base64 encode keyword + rest separately
            b64_rest = base64.b64encode(rest.encode()).decode()
            encoded_payloads.append(f"eval(atob('{b64_keyword}')+atob('{b64_rest}'))")
            
            # Using String.fromCharCode with base64
            encoded_payloads.append(f"eval(String.fromCharCode(...atob('{b64_encoded}').split('').map(c=>c.charCodeAt(0))))")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = base64_encode(payload)
        for ep in encoded_payloads:
            print(ep)

