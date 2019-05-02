import sys, time, itertools 
	
symbols = itertools.cycle("-?/|\!&*^%$#")	# cycle()
	
while True:
	# "\r" 默认将指针返回到最开始后输出（在原位置再次输出）
	sys.stdout.write("\r" + next(symbols))
	sys.stdout.flush()
	time.sleep(1)



"""
import itertools
import time
import sys


def spinner(seconds):
    # Show me an animated spinner while we sleep 
    symbols = itertools.cycle("-\|/")
    tend = time.time() + seconds
    while time.time() < tend:
        sys.stdout.write('\rPlease wait... ' + next(symbols))
        sys.stdout.flush()
        time.sleep(1)
    print()


if __name__ == '__main__':
    spinner(30)     # 


"""

