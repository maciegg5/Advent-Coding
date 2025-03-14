g = 0
sum_ = list()
suma = 0
with open("test.txt") as file:
    for line in file:
        flag = 1
        g += 1
        x = line.index(':') + 2
        line = line[x:]
        line = line.split(";")
        cleaned_list = [item.strip() for item in line]
        # print(cleaned_list)
        output = []
        for item in cleaned_list:
            comp = item.split(', ')
            output.extend(comp)
        output = [el.replace(', ', ' ') for el in output]
        print(output)
        cl = {}
        re = []
        gr = []
        bl = []
        for i in output:
            value, key = i.split(" ")
            print(value, key)
            if key == "red":
                re.append(int(value))
            if key == "green":
                gr.append(int(value))
            if key == "blue":
                bl.append(int(value))
        suma += max(re) * max(gr) * max(bl)

sum_ = list(set(sum_))
sum_ = sum(sum_)
suma_ = [ix for ix in range(101)]
suma_ = sum(suma_)
print(suma_ - sum_)
print(suma)
