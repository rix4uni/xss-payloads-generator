import sys

# Define a dictionary for special characters and their HTML entity encodings
special_characters = {
    '<': '&#x3C;',
    '>': '&#x3E;',
    '&': '&#x26;',
    '"': '&#x22;',
    "'": '&#x27;',
    '¢': '&#x20AC;',
    '£': '&#x20AC;',
    '¥': '&#x00A5;',
    '€': '&#x20AC;',
    '©': '&#x00A9;',
    '®': '&#x00AE;',
    '(': '&#x28;',
    ')': '&#x29;',
    '`': '&#x60;'
}

def html_entity_encode_special(payload):
    return ''.join(special_characters.get(c, c) for c in payload)

if __name__ == "__main__":
    payload = sys.stdin.read().strip()
    encoded_payload = html_entity_encode_special(payload)
    print(encoded_payload)
