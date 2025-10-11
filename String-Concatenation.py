import sys
import re

def string_concat_encode(payload):
    keywords = ['confirm', 'alert', 'prompt']
    for keyword in keywords:
        pattern = re.compile(keyword, re.IGNORECASE)
        match = pattern.search(payload)
        if match:
            start = match.start()
            encoded_payloads = []

            # Progressive splits: "c"+"onfirm(1)", "co"+"nfirm(1)", ..., "confir"+"m(1)"
            for i in range(1, len(keyword)):
                left = keyword[:i]
                right = keyword[i:] + payload[start+len(keyword):]
                encoded_payloads.append(f'eval("{left}"+"{right}")')

            # Keyword + rest payload
            rest_payload = payload[start+len(keyword):]
            encoded_payloads.append(f'eval("{keyword}"+"{rest_payload}")')

            # Fully split into single letters + rest payload
            fully_split_letters = '+'.join(f'"{c}"' for c in keyword)
            fully_split_payload = f'eval({fully_split_letters}+"{rest_payload}")'
            encoded_payloads.append(fully_split_payload)

            return encoded_payloads
    return [payload]

if __name__ == "__main__":
    for line in sys.stdin:
        payload = line.strip()
        encoded_payloads = string_concat_encode(payload)
        for ep in encoded_payloads:
            print(ep)
