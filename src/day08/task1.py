import heapq
import math
from itertools import combinations

type jbox = tuple[int, int, int]

def get_distance(jbox1: jbox, jbox2: jbox) -> float:
    return sum((a - b) ** 2 for a, b in zip(jbox1, jbox2, strict=True))

def solve(input_data: str, is_test: bool = False) -> int:
    connect_count = 10 if is_test else 1000
    jboxes_list: list[jbox] = [tuple(int(x) for x in line.split(",")) for line in input_data.strip().splitlines()] # type: ignore[misc]
    jboxes = {j: {j} for j in jboxes_list}

    distances: list[tuple[float, tuple[jbox, jbox]]] = []
    for jbox1, jbox2 in combinations(jboxes.keys(), 2):
        distances.append((get_distance(jbox1, jbox2), (jbox1, jbox2)))
    heapq.heapify(distances) # linear time

    for _ in range(connect_count):
        _, (jbox1, jbox2) = heapq.heappop(distances)
        # this could be improved by using union_find...
        new_circuit = jboxes[jbox1].union(jboxes[jbox2])
        for jbox in new_circuit:
            jboxes[jbox] = new_circuit


    circuits = [len(circuit) for circuit in {frozenset(i) for i in jboxes.values()}]
    heapq.heapify_max(circuits)
    return math.prod([heapq.heappop_max(circuits) for _ in range(3)])
