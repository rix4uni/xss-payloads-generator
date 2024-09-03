import sys

# Define a dictionary for special characters and their HTML entity encodings
special_characters = {
    '<': '&#x00003C;',
    '>': '&#x00003E;',
    '&': '&#x000026;',
    '"': '&#x000022;',
    "'": '&#x000027;',
    '¢': '&#x000020AC;',
    '£': '&#x000020AC;',
    '¥': '&#x000000A5;',
    '€': '&#x000020AC;',
    '©': '&#x000000A9;',
    '®': '&#x000000AE;',
    '(': '&#x000028;',
    ')': '&#x000029;',
    '`': '&#x000060;'
}

def html_entity_encode_special(payload):
    return ''.join(special_characters.get(c, c) for c in payload)

if __name__ == "__main__":
    payload = sys.stdin.read().strip()
    encoded_payload = html_entity_encode_special(payload)
    print(encoded_payload)
