tc = int(input())

arr = ['No'] * 110

for i in range(1, 10):
    for j in range(1, 10):
        arr[i*j] = 'Yes'

for i in range(1, tc+1):
    n = int(input())
    answer = arr[n]

    print('#{} {}'.format(i, answer))
