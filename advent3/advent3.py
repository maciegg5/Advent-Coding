g = 0
sum_ = list()
with open("test.txt") as file:
    for line in file:
        flag = 1
        g += 1
        x = line.index(':') + 2
        line = line[x:]
        line = line.split(";")
        cleaned_list = [item.strip() for item in line]
        for i in cleaned_list:
            cl = {}
            r = i.split(", ")
            for i in r:
                value, key = i.split(" ")
                cl[key] = int(value)
            print(cl)
            for key in cl:
                if key == "red":
                    if cl[key] > 12:
                        sum_.append(g)
                if key == "green":
                    if cl[key] > 13:
                        sum_.append(g)

                if key == "blue":
                    if cl[key] > 14:
                        sum_.append(g)

sum_ = list(set(sum_))
sum_ = sum(sum_)
suma_ = [ix for ix in range(101)]
suma_ = sum(suma_)
print(suma_ - sum_)
