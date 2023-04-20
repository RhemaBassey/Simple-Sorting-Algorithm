# METHOD 1
nums = [-25,20,0,+57]

def sort(nums):
      i = 0
      swap = 0
      swap_mode = False
      count = 0
      while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                  swap_mode = True
                  swap = int(nums[i+1])
                  nums [i+1] = int(nums[i])
                  nums [i] = int(swap)
                  i += 1
                  continue

            else:
                  if swap_mode == True:
                        i = 0
                        swap_mode = False
                  else:
                        i += 1
            count += 1
      return(nums)

print(sort(nums))

# #METHOD 2 (SLOWER)
# nums = [1,10,9,8,-3,-25,20,0,+57]

# def sort2(nums):
#       i = 0
#       swap = 0
#       count = 0
#       while i < len(nums) - 1:
#             if nums[i] > nums[i+1]:
#                   swap = int(nums[i+1])
#                   nums [i+1] = int(nums[i])
#                   nums [i] = int(swap)
#                   i = 0
#                   continue

#             else:
#                   i += 1
#             count += 1
#       return(nums)

# print(sort2(nums))
