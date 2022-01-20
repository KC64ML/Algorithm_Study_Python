

list_array = []
for i in range(1, 5):
    list_array.append(input())

print()
for list_idx in range(len(list_array)):
    n = list_array[list_idx]
    check = False
    print("|",end="")
    # print("n : ", n)
    for idx in range(len(n)):
        # print("idx:", idx, "n[idx]:", n[idx])
        if (check == False) and (n[idx] == "C" or n[idx] == "S" or n[idx] == "O"):
            print("|",end="")
            # print("check")
            check = True
        print(n[idx],end="")

    print("|")

