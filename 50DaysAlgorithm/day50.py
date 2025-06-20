#그래프에서 순환을 찾는 문제
#순환이 존재하면 1 리턴 없으면 0 리턴
#HINT : dfs를 수행하다가 이미 지나온 경로면 -1로 초기화

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def dfs(graph, x, check):
    if check == 1:
        return True
    if check == -1:
        return False
    check[x] = 1
    for i in graph[x]:
        if dfs(graph, i, check):
            return True
    check[x] = -1

def solution(n, edges):
    check = [0] * (n+1)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    for i in range(1, n+1):
        if dfs(graph, i, check):
            return 1
        return 0
