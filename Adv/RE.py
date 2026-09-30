import re

text = "My 456 order is 12345"
result = re.search(r"\d+", text)

print(result.group())

t = "sdfghjk  12345 is my order"
result = re.match(r"\d+", t)
print(result.group())