import xlrd

data = xlrd.open_workbook('Day2.xlsx')

table = data.sheet_by_name('Sheet1')
nums = table.col_values(0)

dict = []

for item in nums:
    arr = item.split(':')
    dict.append((arr[0], arr[1].strip()))

rescounter = 0

# for item in dict:
#     keytemplist = item[0][:len(item[0]) - 2].split('-')
#     flag = item[0][-1]
#
#     lettercounter = 0
#     for i in item[1]:
#         if i == flag:
#             lettercounter += 1
#
#     if int(keytemplist[0]) <= lettercounter <= int(keytemplist[1]):
#         rescounter += 1

for item in dict:
    keytemplist = item[0][:len(item[0]) - 2].split('-')
    flag = item[0][-1]

    if item[1][int(keytemplist[0])-1]==flag and item[1][int(keytemplist[1])-1]!=flag or item[1][int(keytemplist[0])-1]!=flag and item[1][int(keytemplist[1])-1]==flag:
        rescounter += 1

print(rescounter)
