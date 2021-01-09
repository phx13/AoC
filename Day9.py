with open('Day9.txt') as file:  # Read stream
    content = file.read()
lines = content.split('\n')  # split content to lines
# print(lines)
# print(len(lines))
#
# for i in range(25, len(lines)):
#     target = lines[i]
#     reslist = []
#     dict = {}
#     for item in lines[i - 25:i]:
#         temp = int(target) - int(item)
#         if temp in dict:
#             reslist.append([temp, item])
#         else:
#             dict.update({int(item): int(item)})
#     if len(reslist) == 0:
#         print(lines[i])
#         break

target = 3199139634
temp = 0
for i in range(len(lines)):
    reslist = []
    temp = 0
    while temp < target:
        reslist.append(int(lines[i]))
        temp += int(lines[i])
        i += 1
    # print(temp)
    if temp == target:
        reslist = sorted(reslist)
        res = reslist[0]+reslist[-1]
        print(res)
        break
