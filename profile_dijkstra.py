from common import GRAPH, START, GOAL
from dijkstra_code import dijkstra

for _ in range(500000):
    dijkstra(GRAPH, START, GOAL)