echo -e "// Decimal-Encoded-Payloads"
cat payloads.txt | python3 Decimal-Encoded-Payloads.py

echo -e "\n// Decimal-Encoded-Payloads-Special-Characters"
cat payloads.txt | python3 Decimal-Encoded-Payloads-Special-Characters.py

echo -e "\n// HTML-Entity-Encoding"
cat payloads.txt | python3 HTML-Entity-Encoding.py

echo -e "\n// HTML-Entity-Encoding-Special-Characters"
cat payloads.txt | python3 HTML-Entity-Encoding-Special-Characters.py

echo -e "\n// HTML-Hexadecimal-Entity-Encoding"
cat payloads.txt | python3 HTML-Hexadecimal-Entity-Encoding.py

echo -e "\n// HTML-Hexadecimal-Entity-Encoding-Special-Characters"
cat payloads.txt | python3 HTML-Hexadecimal-Entity-Encoding-Special-Characters.py

echo -e "\n// Unicode-Encoded-Payloads"
cat payloads.txt | python3 Unicode-Encoded-Payloads.py

echo -e "\n// String-Concatenation"
cat payloads.txt | python3 String-Concatenation.py

echo -e "\n// Base64-Encoded-Payloads"
cat payloads.txt | python3 Base64-Encoded-Payloads.py

echo -e "\n// URL-Encoded-Payloads"
cat payloads.txt | python3 URL-Encoded-Payloads.py

echo -e "\n// String-FromCharCode-Payloads"
cat payloads.txt | python3 String-FromCharCode-Payloads.py

echo -e "\n// Template-Literal-Payloads"
cat payloads.txt | python3 Template-Literal-Payloads.py

echo -e "\n// Variable-Obfuscation-Payloads"
cat payloads.txt | python3 Variable-Obfuscation-Payloads.py

echo -e "\n// Function-Constructor-Payloads"
cat payloads.txt | python3 Function-Constructor-Payloads.py

echo -e "\n// Reverse-String-Payloads"
cat payloads.txt | python3 Reverse-String-Payloads.py

echo -e "\n// Mixed-Encoding-Payloads"
cat payloads.txt | python3 Mixed-Encoding-Payloads.py

# pending after when run to get better results
# cat payloads.txt | python3 Different-Event-Handlers.py