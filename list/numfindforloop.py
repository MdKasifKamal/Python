nums = (1,2,3,4,3,4,5,6,7,4,3,56,7,76,6)
x = 6

idx = 0
for num in nums:
    if(num == x):
     print("num found:", idx)
     break
    idx += 1