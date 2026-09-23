from common import GRAPH, HEURISTIC, START, GOAL
from greedy_code import greedy

for _ in range(500000):
    greedy(GRAPH, HEURISTIC, START, GOAL)