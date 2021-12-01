# DFS, BFS

그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

**탐색** : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

* 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다.

**자료구조** : 데이터를 표현하고 관리하고 처리하기 위한 구조

* 삽입(Push) : 데이터를 삽입한다.
* 삭제(Pop) : 데이터를 삭제한다.

Overflow : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생한다. (저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생한다.)

Underflow : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행시 발생

&nbsp;

##### 스택(Stack)

선입후출(First In Last Out), 후입선출(Last In First Out) 구조

##### 큐(Queue)

선입선출(First in First Out) 구조

```python
# stack
stack = []

stack.append(5)
stack.pop()
stack.append(5)

print(stack[]) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# queue
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# 결과
# dequeue([3, 7, 1, 4])
# dequeue([4, 1, 7, 3])

# queue를 list 자료형으로 변경할 때
# list(queue)
```

&nbsp;

**재귀 함수**

DFS와 BFS 구현하려면 재귀 함수가 필요하다.

**재귀 함수(Recursive Function)** : 자기 자신을 다시 호출하는 함수

```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recurisve_function()
    
recursive_function()
```

무한히 반복될 때

`RecursionError : maximum recursion depth exceeded while pickling an object`

: 재귀의 최대 깊이를 초과했다는 내용이다.

보통 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문이다.

&nbsp;

컴퓨터 내부에서 재귀 함수의 수행은 **스택 자료구조**를 이용한다.

함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.

재귀 함수는 내부적으로 스택 자료구조와 동일하다.

스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다.

ex) 2가지 방식으로 구현한 팩토리얼 예제

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)! 를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```

재귀 함수의 코드가 더 간결한 것을 알 수 있다. 이렇게 간결해진 이유는 재귀 함수가 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문이다.

수학에서 점화식 : 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미한다.

ex)

(1) n이 0 혹은 1일 때 : factorial(n) = 1

(2) n이 1보다 클 때 : factorial(n) = n x factorial(n - 1)

&nbsp;

### 탐색 알고리즘 DFS/BFS

**DFS** : 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

그래프 : Node, Edge으로 표현된다. (노드는 Vertex, 정점이라고도 말한다.)

그래프 탐색 : 하나의 노드를 시작으로 다수의 노드를 방문하는 것

두 노드는 인접하다.(Adjacent) : 두 노드가 간선으로 연결되어 있다.

<img src="https://user-images.githubusercontent.com/72541544/143729374-cfcb1a8a-11f8-4589-99e3-97e8a0d8ee3c.jpg" width="400" height="400"/>

**인접 행렬(Adjacency Matrix)** : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

```python
INF = 999999999 # 무한의 비용 선언 (연결되어 있지 않은 노드끼리는 무한의 비용)

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 결과
# [[0, 7, 5], [7, 0, 999999999], [5, 999999999, 0]]
```

&nbsp;

**인접 리스트(Adjacency List)** : 리스트로 그래프의 연결 관계를 표현하는 방식

![abs](https://user-images.githubusercontent.com/72541544/143729457-2e9c944c-8fcb-4a9e-aee7-a4c2f77dda68.jpg)

인접 리스트 방식에서는 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.

<img src="https://user-images.githubusercontent.com/72541544/143729555-20c76682-c8c0-479e-b79d-264cd153f55f.jpg" width="500" height="300"/>

파이썬에서는 배열을 리스트 자료형으로 표현할 수 있으므로 파이썬은 인접 행렬을 리스트로 구현한다.

파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때, 2차원 리스트를 이용하면 된다.

```python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)

# 결과
# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```

&nbsp;

**메모리 측면**

인접 리스트는 인접 행렬방식보다 메모리를 효율적으로 사용한다.

* 메모리 측면에서 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.

* 인접 리스트는 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.

**연결 관계 정보 얻는 속도**

인접 리스트방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.

* 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문이다.

ex) 노드 1과 노드 7이 연결되어 있는 확인할 때

인접 행렬 방식에서는 `graph[1][7]`만 확인하면 된다.

인접 리스트 방식에서는 노드 1에 대한 인접 리스트를 앞에서부터 차례대로 확인해야 한다.

&nbsp;

#### DFS

특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘

&nbsp;

**DFS 스택 자료구조를 이용하며 구체적인 동작 과정**

(1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.

(2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

(3) (2)번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

(방문 처리 : 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것, 각 노드를 한 번씩만 처리할 수 있다.)

&nbsp;

ex) dfs 예시

![dfs](https://user-images.githubusercontent.com/72541544/143729984-461010a0-06b3-449f-86ac-2dcd88774fff.jpg)

가장 깊숙이 위치하는 노드에 닿을 때까지 탐색한다.

일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다.

![dfs2](https://user-images.githubusercontent.com/72541544/143730135-08243de9-693f-49cf-a551-864d28d85256.jpg)

결과적으로 노드의 탐색 순서(스택에 들어간 순서)는 다음과 같다.

`1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5`

&nbsp;

깊이 우선 탐색 알고리즘인 DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단한다.

실제로는 스택을 쓰지 않아도 되며 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다는 특징이 있다.

또한 DFS는 스택을 이용하는 알고리즘이기 때문에 실제 구현은 재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있다.

소스코드

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 결과
# 1 2 7 6 8 3 4 5
```

&nbsp;

&nbsp;

#### BFS

너비 우선 탐색 : 가까운 노드부터 탐색하는 알고리즘

선입선출 방식

동작 과정

(1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.

(2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.

(3) (2)번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

ex) 숫자가 작은 노드부터 먼저 큐에 삽입

![dfs](https://user-images.githubusercontent.com/72541544/143729984-461010a0-06b3-449f-86ac-2dcd88774fff.jpg)

인접한 노드가 여러 개 있을 때, 숫자가 작은 노드부터 먼저 큐에 삽입한다.

![bfs](https://user-images.githubusercontent.com/72541544/143819189-69fe80fd-c364-42ec-aa5f-75cf29d2b72e.jpg)

노드의 탐색 순서

`1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6`

너비 우선 탐색 알고리즘인 BFS는 큐 자료구조에 기초한다는 점에서 구현이 간단한다.

실제로 구현함에 있어 앞서 언급한 대로 deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요된다.

일반적인 경우 실제 수행 시간은 BFS가 DFS보다 좋은 편이다.

소스코드

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 dequeue 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 변환(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 결과
# 1 2 3 8 7 4 5 6
```

&nbsp;

**DFS, BFS 정리**

|           | dfs            | bfs              |
| --------- | -------------- | ---------------- |
| 동작 원리 | 스택           | 큐               |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |

코딩 테스트 중 2차원 배열에서의 탐색 문제를 만나면 그래프 형태로 바꿔서 생각하면 풀이 방법을 조금 더 쉽게 떠올릴 수 있다.

**탐색 문제는 그래프 형태로 표현한 풀이법을 고민해야한다.**

&nbsp;

# 실전문제

### [Q 5-3] 음료수 얼려 먹기

```python
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x -1,y)
        dfs(x, y-1)
        dfs(x + 1 , y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
```

&nbsp;

### [Q 5-4] 미로 탈출

```python
from collections import deque

n, m = map(int,input().split())

graph = []
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))

    
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                print("nx, ny", nx, ny, "x, y" , x, y , "graph", graph[x][y])
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
```

&nbsp;

&nbsp;

&nbsp;

****

참고 자료

* '이것이 취업을 위한 코딩 테스트다' 책

