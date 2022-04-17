import collections
my_str = input().strip()
answer = collections.Counter(my_str)

print(answer[max(answer.values())])
