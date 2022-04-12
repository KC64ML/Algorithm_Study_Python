N, S = map(int, input().split())

nums = list(map(int, input().split()))
nums2 = nums[0:int(N / 2)]
nums3 = nums[int(N / 2):int(N + 1)]
result = {}

l = 0
r = 0
total = 0


def reculse(count, sum):
    if count == len(nums2):
        result[sum] = result.get(sum, 0) + 1
        return

    reculse(count + 1, sum)
    reculse(count + 1, sum + nums2[count])


def reculse2(count, sum):
    global total
    if count == len(nums3):
        total += result.get(S - sum, 0)
        return

    reculse2(count + 1, sum)
    reculse2(count + 1, sum + nums3[count])


reculse(0, 0)
reculse2(0, 0)

if S == 0:
    print(total - 1)
else:
    print(total)