import requests
import webbrowser
import json

"""
1. use wiki-api get random article meta data(json)
2. then process them 
"""

page_count = 10     # change nums of pages
# api url is english, try chinese later
api_url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit='\
      + str(page_count) + '&format=json'
# add the name in the end of url
goto_url = 'https://en.wikipedia.org/wiki?curid='


def load():
    resp = requests.get(api_url)
    if resp.ok:
        jsonData = resp.json()['query']['random']  # type:"dict"
        print("Got 10 pages.")
        # print(jsonData)

        for index, j in enumerate(jsonData):
            print(str(index) + ": ", j['title'])

        i = input("Which page you want to see, type number to continue,"
                  "[r: for retry, n: for exit]?").lower()
        if i == 'r':
            print("Loading again")
        elif i == 'n':
            print("shutting down!")
            return          # return nothing: means sys.exit()
        else:
            try:
                page_name = jsonData[int(i)]['id']
            except Exception:
                raise Exception("Bad input!")
            print("check out your browser...")
            webbrowser.open_new(goto_url + str(page_name))

        load()  # 再这里调用自身，属于递归。
    else:
        resp.raise_for_status()


if __name__ == '__main__':
    load()
