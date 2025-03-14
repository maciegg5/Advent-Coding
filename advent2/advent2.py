dictonary = {

    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9

}

keylist = dictonary.keys()


current_word = ''
lis = list()
res = 0

with open("advent2.txt") as txt:
    for line in txt:
        for i in range(len(line)-1):
            current_word += line[i]
            for wyraz in keylist:
                if wyraz in current_word:
                    lis.append(dictonary[wyraz])
                    if line[i].isalpha():
                        current_word = current_word[-1]
                    else:
                        current_word = ''
        if len(lis) > 1:
            lis = lis[::len(lis)-1]
            res += lis[0] * 10 + lis[1]
        if len(lis) == 1:
            lis.append(lis[0])
            res += lis[0] * 10 + lis[1]
        lis.clear()
print(res)

# odp: 54518
