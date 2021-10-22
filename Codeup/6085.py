w, h, b = 0, 0, 0
result = 0.0

w, h, b = input().split()

h = int(h)
b = int(b)
w = int(w)


result = (h*b*w)/8/1024/1024

print("%.2f MB"%(result))