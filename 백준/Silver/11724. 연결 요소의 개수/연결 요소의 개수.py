from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 정점 수, 간선 수
graph = [[] for _ in range(n + 1)]  # 인접 리스트
visited = [0] * (n + 1)  # 방문 여부 표시

# 그래프 만들기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

count = 0  # 연결 요소 개수

# 전체 정점 순회
for i in range(1, n + 1):
    if visited[i] == 0:  # 아직 방문하지 않은 정점이면
        Q = deque([i])
        visited[i] = 1
        while Q:
            c = Q.popleft()
            for nx in graph[c]:
                if visited[nx] == 0:
                    Q.append(nx)
                    visited[nx] = 1
        count += 1  # 하나의 연결 요소 탐색 완료

print(count)
