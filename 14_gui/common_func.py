# when: 2019/03/22 9:56 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. this a test file for firefly

"""


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# if __name__ == "__main__":
#     print(fib(5))

"""
on shell run :
# firefly common_func.fib

show: 
{"app": "firefly", "version": "0.1.15", "functions": 
    {"fib": {"path": "/fib", "doc": "", 
    "parameters": [{"name": "n", "kind": "POSITIONAL_OR_KEYWORD"}]}}}
"""


