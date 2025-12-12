import numpy as np
import numpy.typing as npt


def simplify_connections(connections: dict[str, list[str]]) -> dict[str, list[str]]:
    """Remove nodes with single outgoing edges (except special nodes) by bypassing them.

    This optimization reduces graph size while preserving path counts, since:
    - A node with 1 output acts as a simple passthrough
    - All paths through it can be counted by directly connecting its inputs to its output

    Note: Special nodes (svr, out, dac, fft) are never removed as they're required
    for the path decomposition logic.
    """
    to_del = []
    for k in connections:
        if len(connections[k]) == 1 and k not in ("svr", "out", "dac", "fft"):
            to_del.append(k)
            for x in connections:
                connections[x] = [y if y != k else connections[k][0] for y in connections[x]]
    for k in to_del:
        del connections[k]
    return connections


def create_adjacency_matrix(connections: dict[str, list[str]]) -> tuple[npt.NDArray[np.int_], dict[str, int]]:
    """Convert connection dictionary to adjacency matrix representation.

    Returns:
        Tuple of (adjacency_matrix, node_to_index_mapping)
        Matrix[i][j] = number of edges from node i to node j
    """
    nodes = set().union(*connections.values()).union(set(connections.keys()))
    index_map = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)
    matrix = np.zeros((size, size), dtype=int)
    for node, neighbors in connections.items():
        for neighbor in neighbors:
            matrix[index_map[node]][index_map[neighbor]] += 1
    return matrix, index_map


def find_path_count(
    adjacency: npt.NDArray[np.int_], start: str, end: str, stop_nodes: list[str], index_mapping: dict[str, int]
) -> int:
    """Count all paths from start to end, avoiding specified stop_nodes.

    Uses matrix multiplication where A^n[i][j] counts paths of length n from i to j.
    Sums across all path lengths to get total count.

    Args:
        adjacency: Adjacency matrix of the graph
        start: Starting node name
        end: Ending node name
        stop_nodes: Nodes to exclude from paths (set their edges to 0)
        index_mapping: Maps node names to matrix indices

    Returns:
        Total number of paths from start to end avoiding stop_nodes
    """
    adjacency_orig = adjacency.copy()
    for node in stop_nodes:
        idx = index_mapping[node]
        adjacency_orig[idx, :] = 0
        adjacency_orig[:, idx] = 0

    start_idx = index_mapping[start]
    end_idx = index_mapping[end]

    # Count paths: start with length-1 paths (direct edges)
    total_paths = adjacency_orig[start_idx, end_idx]
    current_length = adjacency_orig.copy()

    # Keep multiplying to get longer paths until no more paths exist
    for _ in range(adjacency_orig.shape[0]):
        current_length = np.matmul(current_length, adjacency_orig)
        new_paths = current_length[start_idx, end_idx]
        total_paths += new_paths
        # For a DAG, the matrix will eventually become all zeros (no paths of that length exist)
        if not current_length.any():
            break

    print(f"Paths from {start} to {end} avoiding {stop_nodes}: {total_paths}")
    return total_paths


def solve(input_data: str) -> int:
    # assume the graph is acyclic
    connections = {k: v.split(" ") for line in input_data.strip().splitlines() for k, v in [line.split(": ")]}
    connections = simplify_connections(connections)
    adjacency, index_map = create_adjacency_matrix(connections)
    if fft_to_dac := find_path_count(adjacency, "fft", "dac", ["svr", "out"], index_map):
        # svr -> fft -> dac -> out
        return (
            fft_to_dac
            * find_path_count(adjacency, "svr", "fft", ["dac", "out"], index_map)
            * find_path_count(adjacency, "dac", "out", ["svr", "fft"], index_map)
        )
    # since there is no path from fft to dac:
    # svr -> dac -> fft -> out
    return (
        find_path_count(adjacency, "svr", "dac", ["out", "fft"], index_map)
        * find_path_count(adjacency, "dac", "fft", ["svr", "out"], index_map)
        * find_path_count(adjacency, "fft", "out", ["svr", "dac"], index_map)
    )
