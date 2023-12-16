from itertools import combinations

def count_polygons(V,S,P,turns):

    edges = [[0] * V for i in range(V)]
    scores = [0]*P
    for turn in turns:
        player,v1,v2 = turn
        edges[v1][v2] = edges[v2][v1] = player +1
    player_edge_combinations = [list(combinations(range(V),S)) for i in range(P)]

    for player in range(P):
        for combination in player_edge_combinations[player]:
            is_polygon = True
            for i in range(S-1):
                for j in range(i+1, S):
                    if edges[combination[i]][combination[j]] != player +1:
                        is_polygon = False
                        break
            if is_polygon:
                scores[player] += 1
    
    return scores

V = int(input())
S = int(input())
P = int(input())
T = int(input())
turns = [list(map(int, input().spilt())) for i in range(T)]
result = count_polygons(V,S,P,turns)
print(" ".join(map(str, result)))