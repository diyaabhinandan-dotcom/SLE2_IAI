import heapq
from common import GRAPH, START, GOAL

def dijkstra(graph, start, goal):
    pq = [(0, start, [start])]
    best_cost = {start: 0}
    nodes_expanded = 0

    while pq:
        cost, node, path = heapq.heappop(pq)
        nodes_expanded += 1

        if node == goal:
            return path, cost, nodes_expanded

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return None, float('inf'), nodes_expanded