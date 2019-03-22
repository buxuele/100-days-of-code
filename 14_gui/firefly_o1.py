# when: 2019/03/22 9:54 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. take a python-function as a web-service
    https://github.com/rorodata/firefly
2. pip install firefly-python
"""

import firefly

client = firefly.Client("http://127.0.0.1:8000/")
client.fib(n=10)    # failed...

# common_func.fib




