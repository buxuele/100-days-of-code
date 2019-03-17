import json
import time
import requests


"""
Purpose:
    1. review requests
    2. learn how to use a api and get data

Note:
    1. r = requests.post('https://httpbin.org/post', data = {'key':'value'})
    2. useful api:
        #  https://www.apiopen.top/api.html#top
    3. how to pretty print json see: 
        # https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
"""


def get_weather():
    query = {'city': "上海"}
    url = 'https://www.apiopen.top/weatherApi'
    resp = requests.get(url, params=query)

    # print(resp.text)
    python_obj = resp.json()      # type(python_obj): dict
    # print(python_obj)

    today = python_obj["data"]["forecast"][0]["date"] + "\t" + \
            python_obj["data"]["forecast"][0]["high"] + "\t" + \
            python_obj["data"]["forecast"][0]["low"] + "\t" + \
            python_obj["data"]["forecast"][0]["fengli"] + "\t" + \
            python_obj["data"]["forecast"][0]["fengxiang"] + "\t" + \
            python_obj["data"]["forecast"][0]["type"] + "\t"

    tomorrow = python_obj["data"]["forecast"][1]["date"] + "\t" + \
            python_obj["data"]["forecast"][1]["high"] + "\t" + \
            python_obj["data"]["forecast"][1]["low"] + "\t" + \
            python_obj["data"]["forecast"][1]["fengli"] + "\t" + \
            python_obj["data"]["forecast"][1]["fengxiang"] + "\t" + \
            python_obj["data"]["forecast"][1]["type"] + "\t"

    print(today)
    print(tomorrow)


if __name__ == '__main__':
    get_weather()

