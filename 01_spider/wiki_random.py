import webbrowser

""" 
1. open 5 random wiki-pages to read, brain storm or kill some time.
2. could use selenium do the same, and close them in {some_time}, then open 5-new pages
3. 
"""

# 维基百科随机页面的 url
url = 'https://zh.wikipedia.org/wiki/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2'
num = 5

for i in range(num):
    webbrowser.open_new(url)


