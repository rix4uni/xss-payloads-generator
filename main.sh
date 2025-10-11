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

# pending after when run to get better results
# cat payloads.txt | python3 Different-Event-Handlers.py