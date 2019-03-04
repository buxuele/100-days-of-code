from itertools import permutations, combinations

friends = 'mike bob julian'.split()
print(friends)  # ['mike', 'bob', 'julian']

print(list(combinations(friends, 2)))	# 无重复。
print(list(permutations(friends, 2)))   # 有前后重复。这个词的本意是：序列，排列