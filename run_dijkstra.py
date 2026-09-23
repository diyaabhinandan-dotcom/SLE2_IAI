import timeit
from common import GRAPH, START, GOAL
from dijkstra_code import dijkstra

NUMBER = 10000
REPEAT = 5

results = timeit.repeat(
    stmt="dijkstra(GRAPH, START, GOAL)",
    globals=globals(),
    number=NUMBER,
    repeat=REPEAT
)

per_run_us = [(t / NUMBER) * 1e6 for t in results]
print("DIJKSTRA RESULTS")
print("Repeats (us):", [round(x, 3) for x in per_run_us])
print("Best  (us):", round(min(per_run_us), 3))
print("Avg   (us):", round(sum(per_run_us)/len(per_run_us), 3))

path, cost, expanded = dijkstra(GRAPH, START, GOAL)
print("Path:", " -> ".join(path))
print("Cost:", cost)
print("Nodes expanded:", expanded)