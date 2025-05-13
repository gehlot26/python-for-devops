#Find phone number
import re
phone_text = "Call me on 9876543210"
phone_pattern = r"\d{10}"
phone_match = re.search(phone_pattern, phone_text)
print("Phone Number found:", phone_match.group())

