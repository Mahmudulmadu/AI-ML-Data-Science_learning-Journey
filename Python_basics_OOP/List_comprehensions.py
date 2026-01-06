# sq = [i*i for i in range(6) if i%2 != 0]

# print(sq)


nums = [-2,-1, 2, 7 , -1 ,0]

nums = [0 if val < 0 else val for val in nums]
print(nums)