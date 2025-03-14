result = 0

with open("advent1.txt") as file:
    for line in file:
        num_list = [num for num in line if num.isdigit()]
        if len(num_list) == 1:
            num_list.append(num_list[0])
        num_list = num_list[::len(num_list)-1]
        result += int(''.join(num_list))
        num_list.clear()

print(result)
