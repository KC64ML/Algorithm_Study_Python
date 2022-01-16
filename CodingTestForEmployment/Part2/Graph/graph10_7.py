# 특정 원소가 속한 집합을 찾기
def find_def(parent, data):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[data] != data:
        parent[data] = find_def(parent, parent[data])
    return parent[data]


# 두 원소가 속한 집합을 합치기
def union_def(parent, a, b):
    a = find_def(parent, a)
    b = find_def(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화
graph = []

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for idx in range(1, n + 1):
    parent[idx] = idx

# 각 연산을 하나씩 확인
for idx in range(0, m):
    num, a, b = map(int, input().split())

    # 합집합(union) 연산인 경우
    if num == 0:
        union_def(parent, a, b)
    # 찾기(find) 연산인 경우
    else:
        if find_def(parent, a) == find_def(parent, b):
            print("YES")
        else:
            print("NO")