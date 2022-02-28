# 트리 순회

import sys

n = int(sys.stdin.readline())

# 문자열 배열일 때는 딕셔너리 사용하기

tree = {}


def pre_order(root):
    if root != ".":
        print(root, end="")
        pre_order(tree[root][0])
        pre_order(tree[root][1])

def mid_order(root):
    if root != ".":
        mid_order(tree[root][0])
        print(root, end="")
        mid_order(tree[root][1])

def post_order(root):
    if root != ".":
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end="")

for _ in range(n):
    node, left, right = sys.stdin.readline().split()

    tree[node] = [left, right]

pre_order('A')
print()
mid_order('A')
print()
post_order('A')
print()
