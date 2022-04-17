import bisect
mylist = [1, 8, 4, 7, 9, 11, 3, 5, 33]
mylist.sort()
print(bisect.bisect(mylist, 8))