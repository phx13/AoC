# with open('Day8.txt') as file:  # Read stream
#     content = file.read()
# lines = content.split('\n')  # split content to lines
# print(lines)
# print(len(lines))
#
# dict = {}
# counter = 0
# i = 0
# while 1:
#     if i in dict:
#         break
#     l = lines[i].split()
#     if l[0] == 'acc':
#         counter += int(l[1])
#         dict.update({i: counter})
#         i += 1
#     elif l[0] == 'nop':
#         dict.update({i: counter})
#         i += 1
#     elif l[0] == 'jmp':
#         dict.update({i: counter})
#         i += int(l[1])
# print(dict)
# print(counter)

inp = open('Day8.txt', 'r')
instructions = []
for line in inp:
    instructions.append(line.strip())

allRunCounter = 0


def runProgram(instructions):
    doneInstructions = []
    i = 0
    acc = 0
    while True:
        try:
            if i in doneInstructions:
                break
            doneInstructions.append(i)
            if instructions[i].startswith('jmp'):
                i += int(instructions[i].split(' ')[1])
            elif instructions[i].startswith('acc'):
                acc += int(instructions[i].split(' ')[1])
                i += 1
            else:
                i += 1
        except:
            global allRunCounter
            allRunCounter += 1
            break

    return acc


print(runProgram(instructions))

for i in range(len(instructions)):
    newInstructions = instructions.copy()
    if newInstructions[i].startswith('jmp'):
        newInstructions[i] = newInstructions[i].replace('jmp', 'nop')
        runProgram(newInstructions)
    elif newInstructions[i].startswith('nop'):
        newInstructions[i] = newInstructions[i].replace('nop', 'jmp')
        runProgram(newInstructions)
    if allRunCounter == 1:
        break

print(runProgram(newInstructions))

# import copy
# def read_input():
#     input_arr = []
#     with open("Day8.txt") as i_f:
#         for line in i_f:
#             line = line.rstrip().split(" ")
#             input_arr.append([line[0], line[1]])
#     return input_arr
#
#
# def test_comb(input_arr):
#     acc = 0
#     p = 0
#     num_steps = 0
#     while True:
#         num_steps += 1
#         if num_steps > 1000:
#             return False
#         if p == len(input_arr):
#             return acc
#         line = input_arr[p]
#         op = line[0]
#         val = int(line[1])
#         if op == "acc":
#             acc += val
#         elif op == "jmp":
#             p += val
#             continue
#         p += 1
#
# def solve_puzzle(input_arr):
#     for i in range(0, len(input_arr)):
#         if input_arr[i][0] == "nop":
#             copy1 = copy.deepcopy(input_arr)
#             copy1[i][0] = "jmp"
#             res = test_comb(copy1)
#             if res != False:
#                 print(res)
#         elif input_arr[i][0] == "jmp":
#             copy2 = copy.deepcopy(input_arr)
#             copy2[i][0] = "nop"
#             res = test_comb(copy2)
#             if res != False:
#                 print(res)
#
# def main():
#     input_arr = read_input()
#     print(solve_puzzle(input_arr))
#
# main()
