from collections import deque
import copy
# 리스트 단순 대입연산 시 값이 변경될때 문제 발생할 수 있음
# -> 리스트 값 복제해야 할 때 ** deepcopy() ** 사용

v = int(input())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)] # 간선 정보 그래프
time = [0]*(v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번째 수는 강의 시간
    for x in data[1:-1]: # 두번째부터 마지막 수는 선행 강의번호
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행결과 담을 리스트
    q = deque()

    # 시작: 진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        #꺼낸 원소랑 연결된 노드들 진입차수-1
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            # 새롭게 진입차수 0되는 노드 삽입
            if indegree[i] == 0:
                q.append(i)


    # 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()