def max_weight_sum(matrix, n, m, queries):
    dp = [[0] * m for _ in range(n)]

    # Populate dp table with maximum sum of weights
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                dp[i][j] = matrix[i][j]
            elif i == n-1:
                dp[i][j] = matrix[i][j] + dp[i][j+1]
            elif j == m-1:
                dp[i][j] = matrix[i][j] + dp[i+1][j]
            else:
                dp[i][j] = matrix[i][j] + max(dp[i+1][j], dp[i][j+1])

    # Process queries and print results
    for query in queries:
        query_type, x, y = query
        if query_type == 1:
            print(dp[x-1][y-1])
        elif query_type == 2:
            print(max(dp[x-1][y-1], dp[x][y-1], dp[x-1][y]))

# # Sample input
# n, m = 4, 5
# matrix = [
#     [-21, 1, 8, 35, 40],
#     [14, -21, -26, -35, -29],
#     [-40, 36, 48, 37, 24],
#     [46, 8, 33, -21, -3]
# ]
# q = 10
# queries = [
#     [1, 1, 1],
#     [1, 2, 2],
#     [1, 2, 4],
#     [1, 3, 5],
#     [2, 1, 1],
#     [2, 1, 2],
#     [2, 2, 1],
#     [2, 2, 3],
#     [2, 3, 2],
#     [2, 3, 4]
# ]

# # Get the results and print them
# max_weight_sum(matrix, n, m, queries)

# def max_weight_sum(matrix, n, m, queries):
#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     # Populate dp table with maximum sum of weights
#     for i in range(n, 0, -1):
#         for j in range(m, 0, -1):
#             dp[i-1][j-1] = matrix[i-1][j-1] + max(dp[i][j-1], dp[i-1][j])

#     # Process queries
#     results = []
#     for query in queries:
#         query_type, x, y = query
#         if query_type == 1:
#             path_sum = dp[x][y]
#             i, j = x, y
#             while i < n and j < m:
#                 path_sum += matrix[i][j]
#                 if i + 1 < n and j + 1 < m:
#                     if dp[i + 1][j] > dp[i][j + 1]:
#                         i += 1
#                     else:
#                         j += 1
#                 elif i + 1 < n:
#                     i += 1
#                 elif j + 1 < m:
#                     j += 1
#                 else:
#                     break
#             results.append(path_sum)
#         elif query_type == 2:
#             results.append(dp[x][y])

#     return results

# Example usage:
# Read input
n, m = 4, 5
matrix = [
    [-21, 1, 8, 35, 40],
    [14, -21, -26, -35, -29],
    [-40, 36, 48, 37, 24],
    [46, 8, 33, -21, -3]
]
q = 10
queries = [
    [1, 1, 1],
    [1, 2, 2],
    [1, 2, 4],
    [1, 3, 5],
    [1, 4, 3],
    [2, 1, 1],
    [2, 2, 2],
    [2, 2, 4],
    [2, 3, 5]
]
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# q = int(input())
# queries = [list(map(int, input().split())) for _ in range(q)]

# Get the results
results = max_weight_sum(matrix, n, m, queries)

# Print the results
for result in results:
    print(result)


