import xlrd

data = xlrd.open_workbook('Day3.xlsx')

table = data.sheet_by_name('Sheet1')
nums = table.col_values(0)
print(nums)
dicttemp = []

for item in nums:
    temp = item * 200
    dicttemp.append(temp)

res = 0
for i in range(int((len(dicttemp)-1)/2)):
    if dicttemp[2*i][i] == "#":
        res += 1

print(res)
# 58*209*58*64*35