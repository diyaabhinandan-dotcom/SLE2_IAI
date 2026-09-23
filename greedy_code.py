import heapq
from common import GRAPH, HEURISTIC, START, GOAL

def greedy(graph, heuristic, start, goal):
    pq = [(heuristic[start], start, [start], 0)]
    visited = set()
    nodes_expanded = 0

    while pq:
        h, node, path, cost = heapq.heappop(pq)
        nodes_expanded += 1

        if node == goal:
            return path, cost, nodes_expanded

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor, path + [neighbor], cost + weight)
                )

    return None, float('inf'), nodes_expanded