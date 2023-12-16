from itertools import combinations

def count_polygons(V, S, P, turns):
    # Initialize the adjacency matrix
    edges = [[0] * V for _ in range(V)]

    # Count polygons for each player
    scores = [0] * P

    # Process turns and update edges
    for turn in turns:
        player, v1, v2 = turn
        edges[v1][v2] = edges[v2][v1] = player + 1  # Use player + 1 to differentiate players

    # Generate all possible combinations of edges for each player
    player_edge_combinations = [list(combinations(range(V), S)) for _ in range(P)]

    # Count polygons for each player
    for player in range(P):
        for combination in player_edge_combinations[player]:
            is_polygon = True
            for i in range(S - 1):
                for j in range(i + 1, S):
                    if edges[combination[i]][combination[j]] != player + 1:
                        is_polygon = False
                        break
                if not is_polygon:
                    break
            if is_polygon:
                scores[player] += 1

    return scores

# Example usage with the provided input
V = int(input())
S = int(input())
P = int(input())
T = int(input())

turns = [list(map(int, input().split())) for _ in range(T)]

# Calculate and print scores
result = count_polygons(V, S, P,turns)
print(" ".join(map(str, result)))

result = count_polygons(V, S, P, T, turns)
print(" ".join(map(str, result)))
