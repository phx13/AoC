with open('Day10.txt') as file:  # Read stream
    content = file.read()
lines = content.split('\n')  # split content to lines
print(lines)
print(len(lines))

reslist = []
for line in lines:
    reslist.append(int(line))
reslist = sorted(reslist)
print(reslist)

counter1 = 0
counter3 = 0
for i in range(len(reslist) - 1):
    if reslist[i + 1] - reslist[i] == 1:
        counter1 += 1
    elif reslist[i + 1] - reslist[i] == 3:
        counter3 += 1
res = (counter1 + 1) * (counter3 + 1)
print(res)

with open("Day10.txt") as f:
    s = f.read().strip()

nums = [int(x) for x in s.split("\n")]
nums.append(0)
nums.append(max(nums) + 3)

nums.sort()

c3 = sum(1 for i in range(1, len(nums)) if nums[i] - nums[i - 1] == 3)
c1 = sum(1 for i in range(1, len(nums)) if nums[i] - nums[i - 1] == 1)

print(c1 * c3)


# some variables:
# nums is your input, appended (max(nums) + 3) in the end and appended 0 at the first, then sorted
# res is a list which record arrangements for every length nums

# init res as a list
res = [0] * (len(nums))
# the first element is 1 because from 0 to 0, there is only one arrangement
res[0] = 1
# loop from the second element to the last element in the nums
for i in range(1, len(nums)):
    # loop the elements before current element
    for j in range(0, i):
        # compare the difference between them, if <= 3, means it can from num[j] to arrive at current element(nums[i])
        if nums[i] - nums[j] <= 3:
            # If it can be achieved, add up the sum of previous arrangements
            # simple example:
            # if [0, 1, 2], there are two case => [0, 1, 2], [0, 2]
            # for [0, 1, 2, 3], we only need to take care about which number can arrive 3
            # ①. 0 can arrive 3, so we only need to add the number of arrangements from 0 to 0 (res[0])
            # ②. 1 can arrive 3, so we only need to add the number of arrangements from 0 to 1 (res[1])
            # ③. 2 can arrive 3, so we only need to add the number of arrangements from 0 to 2 (res[2])
            res[i] += res[j]
# in the end, we gain the result of the last one
print(res[-1])
