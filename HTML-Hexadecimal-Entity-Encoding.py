import sys
import re

def html_entity_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []
            for i in range(len(keyword)):
                encoded_char = f"&#x0000{ord(keyword[i]):x};"
                new_payload = payload[:start + i] + encoded_char + payload[start + i + 1:]
                encoded_payloads.append(new_payload)
            
            # Adding the version where all letters are encoded
            fully_encoded = ''.join(f"&#x0000{ord(c):x};" for c in keyword)
            fully_encoded_payload = payload[:start] + fully_encoded + payload[start + len(keyword):]
            encoded_payloads.append(fully_encoded_payload)
            
            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = html_entity_encode(payload)
        for ep in encoded_payloads:
            print(ep)
