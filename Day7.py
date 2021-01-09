def initData():
    db = {}
    with open('Day7.txt') as file:  # Read stream
        content = file.read()
    for l in content.split("\n"):
        if l != '':
            l = l.replace(',', '').split()
            key = "{} {}".format(l[0], l[1])
            t = []
            l = l[4:]
            if (l != ['no', 'other', 'bags.']):
                for i in range(len(l)):
                    if (i % 4 == 0):
                        t.append((int(l[i]), "{} {}".format(l[i + 1], l[i + 2])))
                if (key not in db):
                    db[key] = t
    return db


db = initData()  # 初始化数据，把数据整理成字典{key是袋子名子：value是元组（数量，袋子名字）组成的列表


def part1():
    search = ['shiny gold']
    outer, start = set(), 0
    while True:
        for i in db.keys():  #
            for j in db[i]:
                if (j[1] in outer or j[1] in search):
                    outer.add(i)
        if (len(outer) > start):
            start = len(outer)
        else:
            break
    print(len(outer))


def part2():
    def getNumber(bag):
        c = 1
        if (bag in db):  # 在key中去找袋子名字，如果有
            for i in db[bag]:  # 遍历该袋子的value，追溯上一层
                c += i[0] * getNumber(i[1])  # 递归value的value的value...
        return c

    print(getNumber('shiny gold') - 1)


part1()
part2()
