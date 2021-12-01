# DFS, BFS

**탐색** : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 한다.

**자료구조** : 데이터를 표현하고 처리하는 방법

**스택** : 선입후출 구조 또는 후입선출 구조

**큐** : 선입선출 구조

**dfs** : 깊이 우선 탐색, 그래프를 탐색하는 알고리즘, 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택 자료구조를 이용한다.

**bfs** : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘, 선입선출 방식의 큐를 이용하면 효과적으로 구현할 수 있다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면, 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색한다.

&nbsp;

### [Q 15]

모든 도로의 거리는 1이다. (간선의 비용 : 1)

**그래프에서 모든 간선의 비용이 동일할 때는 너비 우선 탐색(BFS)을 이용하여 최단 거리를 찾을 수 있다.**

모든 도로의 거리는 '1'이라는 조건 덕분에 너비 우선 탐색을 이용하여 간단히 해결할 수 있다.

너비 우선 탐색을 이용하여 시간 복잡도 O(N + M)으로 동작하는 소스코드를 작성하여 시간 초과 없이 해결할 수 있다.

특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤에, 각 최단 거리를 하나씩 확인하여 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.

소스

```python
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 -1로 초기화
distance = [-1] * (n + 1)

distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)



# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
```

&nbsp;

### [Q 16] 연구소

벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다.

전체 맵의 크기가 8 X 8 = 64 이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존재하지 않는 경우) 64C3이 될 것이다.

이는 100,000보다도 작은 수이므로, 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있다는 것을 알 수 있다.

**모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있다.**

벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다.

**안전 영역의 크기를 구하는 것 또한 DFS 혹은 BFS를 이용하여 계산할 수 있다.**

&nbsp;

초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치한다.

매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전 영역을 구해야 한다.

(각 바이러스 위치에서 DFS나 BFS를 수행하여 연결된 모든 부분을 감염시키도록 처리할 수 있다.)

&nbsp;

소스

```python
n, m = map(int, input().split())
data = [] # 초기 list
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(dfs)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for idx  in range(4):
        next_x = x + dx[idx]
        next_y = y + dy[idx]
        
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if temp[next_x][next_y] == 0:
            # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
            temp[next_x][next_y] = 2
            virus(next_x, next_y)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_zero_cnt():
    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero_cnt += 1

    return zero_cnt

# 깊이 우선 탐색(dfs)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
		# 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 바이러스 위치라면 전파하기
                    virus(i,j)
        # 0의 개수 찾기
        result = max(result, get_zero_cnt())
        return result
    else:
        # 빈 공간에 울타리 설치
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1



dfs(0)
print(result)
```

이번 문제를 풀며 알게 된 것

백준에서 채점을 할 때

복잡한 코드(반복)을 사용하는 경우 : PyPy3가 우세하기 때문에 PyPy3을 사용한다.

간단한 코드을 사용하는 경우 : Python3가 메모리, 속도 측에서 우세하기 때문에 Python3을 사용한다.

&nbsp;

### [Q 17] 경쟁적 전염

너비 우선 탐색을 이용하여 해결할 수 있다.

문제에 나와 있는대로 각 바이러스가 낮은 번호부터 중식한다.

초기, 큐에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야 한다.

이후에, 너비 우선 탐색을 수행하며 방문하지 않은 위치를 차례대로 방문하도록 한다.

&nbsp;

소스

```python
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))

    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, cur_s, cur_x, cur_y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == cur_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 해당 위치로 이동할 수 없는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, cur_s + 1, nx, ny))


print(graph[x-1][y-1])
```

&nbsp;

### [Q 18] 괄호 변환

DFS 알고리즘의 핵심이 되는 재귀 함수 구현을 요구한다는 점에서 DFS 연습 목적의 문제

이 문제를 실수 없이 풀려면 소스코드를 최대한 단순화하는 것이 좋다.

**특정 문자열에서 "균형잡힌 괄호 문자열"의 인덱스를 반화하는 함수와 특정한 "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 판단하는 메서드를 별도로 구현한다.**

&nbsp;

소스

```python

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def corrected(u):
    count = 0 # 왼쪽 괄호의 개수
    for idx in range(len(u)):
        if u[idx] == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1

    return True # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer

    p_cur_index = balanced(p)
    u = p[:p_cur_index + 1]
    v = p[p_cur_index + 1:]

    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if (corrected(u)):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        # 만약 ( 없이 )이 먼저 시작된다면
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'

        answer += "".join(u)

    return answer

a = "()))((()"
b = ")("
print(solution(a))
```



&nbsp;

&nbsp;

****

참고 자료

* '이것이 취업을 위한 코딩테스트다.' 한빛미디어