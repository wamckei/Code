# Regex library
import re

text = "Contact us at support@example.com, sales@example.co.in or feedback@company.org. You can also wisit our website or send a message directly"
# Regular Expression - Regex is the pattern to search in the text
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print("Extracted all emaails: ", emails)

#detect is a phone number has exactly 10 didgits
inputnumber = input("Enter a phone number: ")

if re.fullmatch(r"\d{10}", inputnumber):
    print("Valid phone number entered", inputnumber)
else:
    print("Invalid phone number entered")