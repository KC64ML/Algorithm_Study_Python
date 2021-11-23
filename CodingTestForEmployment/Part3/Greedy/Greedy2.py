s = input()

list_data = list(s)
check_cal = False
result = 1

list_data.sort()
print(list_data)
for idx in range(len(list_data)):
    if list_data[idx] == '0':
        continue

    if check_cal == False and list_data[idx] == '1':
        result += 1
    else:
        check_cal = True
        result *= int(list_data[idx])

print(result)