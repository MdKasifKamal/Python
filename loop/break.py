nums = (1,4,9,16,25,36,49,64,25,81,100,25)
x = 25

i = 0
while i < len(nums):
  if(nums[i] == x):
    print("fonded at idx", i)
    break
  else:
    print("finding...")
  i += 1
