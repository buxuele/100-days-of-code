# 1. dict
some_dict = {"Julian": 25, "Bob": 26, "Dan": 47, "Cornelius": 3}
for i, j in some_dict.items():
    print(i, j)


# 2. sort list 
s = [32, 14, 65, 2, 99, 222, 3, 1]

# s.sort()	# 无返回值，改变原来的列表
# print(s)	# 

a = sorted(s)	# 有返回值，不改变原来的列表。
print(a)	
print(s)


s.reverse()		# 无返回值，改变原来的列表
print(s)

