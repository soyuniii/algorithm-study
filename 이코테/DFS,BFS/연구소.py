# nxm 직사각형 연구소에 상하좌우로 퍼지는 바이러스. 새로 세울 수 있는 벽의 개수는 3개.
# 0: 빈칸, 1: 벽, 2: 바이러스 일때 벽을 세우고 얻을 수 있는 안전영역 크기의 최댓값을 구하는 프로그램.
from collections import deque
from itertools import combinations
import copy

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 빈칸과 바이러스 찾기
empty = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))

def get_safe_area():
    temp_graph = copy.deepcopy(graph)

    # 바이러스 퍼뜨리기
    q = deque(virus)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx, ny))

    # 남은 빈칸 개수
    cnt = 0 
    for row in temp_graph:
        cnt += row.count(0)
    return cnt

# 벽 3개 세우는 백트래킹
max_safe_area = 0

for walls in combinations(empty, 3):
    for r, c in walls:
        graph[r][c] = 1

    safe_area = get_safe_area()
    max_safe_area = max(max_safe_area, safe_area)

    # 다음 조합을 위해 다시 빈칸으로
    for r, c in walls:
        graph[r][c] = 0 

print(max_safe_area)
