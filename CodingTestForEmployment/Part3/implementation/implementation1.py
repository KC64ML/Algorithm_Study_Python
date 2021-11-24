n = input()

front_n = n[0:len(n)//2]
back_n = n[len(n)//2:len(n)]

front_n = map(int,front_n)
back_n = map(int,back_n)

result_f = sum(front_n)
result_b = sum(back_n)

if result_f == result_b:
    print('LUCKY')
else:
    print('READY')