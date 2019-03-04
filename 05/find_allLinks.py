import re
import requests

url = "http://llmb10.com/llzy"

html = requests.get(url).text


print(type(html))

links = re.findall('"((http|ftp)s?://.*?)"', html)

# try to find all emails
emails = re.findall('"(.*@.*\.com$)"', html)

# print(type(links))
# print(len(links))
#
# for l in links:
#     print(l[0])

# for e in emails:
#     print(e)