with open('Day25.txt') as f:
    content = f.read().split('\n')

card = 7290641
door = 19774466

# card = 5764801
# door = 17807724
value = 1
flag = 1
i = 0
#
# while flag:
#     value = value * 7
#     value = value % 20201227
#     i += 1
#     if value == card:
#         cardpublickey = i
#         i = 0
#         flag = 0
#         break
#
# value = 1
# while flag:
#     value = value * 7
#     value = value % 20201227
#     i += 1
#     if value == door:
#         doorpublickey = i
#         i = 0
#         flag = 0
#         break
#
# print(cardloopsize)  # 3816829    8
# print(doorloopsize)  # 11629023     11

# value = 1
for i in range(3816829):
    value = value * door
    value = value % 20201227
    encryptionkey = value
    i += 1
print(encryptionkey)