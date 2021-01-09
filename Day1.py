import xlrd

data = xlrd.open_workbook('Day1.xlsx')

table = data.sheet_by_name('Sheet1')
nums = table.col_values(0)

# reslist = []
# dict = {}
# for item in nums:
#     temp = 2020 - item
#     if temp in dict:
#         reslist.append([temp, item])
#     else:
#         dict.update({item: item})
# print(reslist)

n = len(nums)
print(n)
nums.sort()

print(nums)
reslist = []

for i in range(n):
    if nums[i] > 2020:
        break
    left = i + 1
    right = n - 1
    while left < right:
        if nums[i] + nums[left] + nums[right] == 2020:
            reslist.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif nums[i] + nums[left] + nums[right] > 0:
            right -= 1
        else:
            left += 1
print(reslist)
