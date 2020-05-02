import re

text = "random string. MyName123@website.com . some more randoom text. Yor name.s_k_@yopmail.com"

pattern = re.compile("[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.findall(text)

print(result)
