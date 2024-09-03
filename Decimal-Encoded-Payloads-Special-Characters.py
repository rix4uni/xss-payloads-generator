import sys

# Define a dictionary for special characters and their HTML entity encodings
special_characters = {
    '<': '&#60;',
    '>': '&#62;',
    '&': '&#38;',
    '"': '&#34;',
    "'": '&#39;',
    '¢': '&#162;',
    '£': '&#163;',
    '¥': '&#165;',
    '€': '&#8364;',
    '©': '&#169;',
    '®': '&#174;',
    '(': '&#40;',
    ')': '&#41;',
    '`': '&#96;'
}

def html_entity_encode_special(payload):
    return ''.join(special_characters.get(c, c) for c in payload)

if __name__ == "__main__":
    payload = sys.stdin.read().strip()
    encoded_payload = html_entity_encode_special(payload)
    print(encoded_payload)
