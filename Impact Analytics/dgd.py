# # def max_weight_sum(matrix, n, m, x, y, memo):
# #     if x == n - 1 and y == m - 1:
# #         return matrix[x][y]

# #     if memo[x][y] != -1:
# #         return memo[x][y]

# #     down_sum = float('-inf')
# #     right_sum = float('-inf')

# #     if x + 1 < n:
# #         down_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x + 1, y, memo)

# #     if y + 1 < m:
# #         right_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x, y + 1, memo)

# #     memo[x][y] = max(down_sum, right_sum)
# #     return memo[x][y]

# # def process_queries(matrix, n, m, queries):
# #     results = []
# #     memo = [[-1] * m for _ in range(n)]

# #     for query in queries:
# #         query_type, x, y = query
# #         if query_type == 1:
# #             result = max_weight_sum(matrix, n, m, x - 1, y - 1, memo)
# #         elif query_type == 2:
# #             result = max_weight_sum(matrix, n, m, 0, 0, memo)

# #         results.append(result)

# #     return results

# # # Given input
# # n, m = 4, 5
# # matrix = [
# #     [-21, 1, 8, 35, 40],
# #     [14, -21, -26, -35, -29],
# #     [-40, 36, 48, 37, 24],
# #     [46, 8, 33, -21, -3]
# # ]
# # q = 10
# # queries = [
# #     [1, 1, 1],
# #     [1, 2, 2],
# #     [1, 2, 4],
# #     [1, 3, 5],
# #     [1, 4, 3],
# #     [2, 1, 1],
# #     [2, 2, 2],
# #     [2, 2, 4],
# #     [2, 3, 5],
# #     [2, 4, 3]
# # ]

# # # Get the results
# # results = process_queries(matrix, n, m, queries)

# # # Print the results
# # for result in results:
# #     print(result)

# def max_weight_sum(matrix, n, m, x, y, memo):
#     if x == n - 1 and y == m - 1:
#         return matrix[x][y]

#     if (x, y) in memo:
#         return memo[(x, y)]

#     down_sum = float('-inf')
#     right_sum = float('-inf')

#     if x + 1 < n:
#         down_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x + 1, y, memo)

#     if y + 1 < m:
#         right_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x, y + 1, memo)

#     memo[(x, y)] = max(down_sum, right_sum)
#     return memo[(x, y)]

# def process_queries(matrix, n, m, queries):
#     results = []
#     memo = {}

#     for query in queries:
#         query_type, x, y = query
#         if query_type == 1:
#             result = max_weight_sum(matrix, n, m, x - 1, y - 1, memo)
#         elif query_type == 2:
#             result = max_weight_sum(matrix, n, m, 0, 0, memo)

#         results.append(result)

#     return results

# # Given input
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
#     [1, 4, 3],
#     [2, 1, 1],
#     [2, 2, 2],
#     [2, 2, 4],
#     [2, 3, 5],
#     [2, 4, 3]
# ]

# # Get the results
# results = process_queries(matrix, n, m, queries)

# # Print the results
# for result in results:
#     print(result)

# def max_weight_sum(matrix, n, m, x, y, memo):
#     if x == n - 1 and y == m - 1:
#         return matrix[x][y]

#     if (x, y) in memo:
#         return memo[(x, y)]

#     down_sum = float('-inf')
#     right_sum = float('-inf')

#     if x + 1 < n:
#         down_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x + 1, y, memo)

#     if y + 1 < m:
#         right_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x, y + 1, memo)

#     memo[(x, y)] = max(down_sum, right_sum)
#     return memo[(x, y)]

# def process_queries(matrix, n, m, queries):
#     results = []
#     memo = {}

#     for query in queries:
#         query_type, x, y = query
#         if query_type == 1:
#             result = max_weight_sum(matrix, n, m, x - 1, y - 1, memo)
#         elif query_type == 2:
#             result = max_weight_sum(matrix, n, m, 0, 0, memo)

#         results.append(result)

#     return results

# # Given input
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
#     [1, 4, 3],
#     [2, 1, 1],
#     [2, 2, 2],
#     [2, 2, 4],
#     [2, 3, 5],
#     [2, 4, 3]
# ]

# # Get the results
# results = process_queries(matrix, n, m, queries)

# # Print the results
# for result in results:
#     print(result)

# def max_weight_sum(matrix, n, m, x, y, memo):
#     if x == n - 1 and y == m - 1:
#         return matrix[x][y]

#     if (x, y) in memo:
#         return memo[(x, y)]

#     down_sum = float('-inf')
#     right_sum = float('-inf')

#     if x + 1 < n:
#         down_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x + 1, y, memo)

#     if y + 1 < m:
#         right_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x, y + 1, memo)

#     memo[(x, y)] = max(down_sum, right_sum)

#     # Debugging prints
#     print(f"({x}, {y}) - down_sum: {down_sum}, right_sum: {right_sum}, memo: {memo[(x, y)]}")

#     return memo[(x, y)]

# def process_queries(matrix, n, m, queries):
#     results = []
#     memo = {}

#     for query in queries:
#         query_type, x, y = query
#         if query_type == 1:
#             result = max_weight_sum(matrix, n, m, x - 1, y - 1, memo)
#         elif query_type == 2:
#             result = max_weight_sum(matrix, n, m, 0, 0, memo)

#         results.append(result)

#     return results

# # Given input
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
#     [1, 4, 3],
#     [2, 1, 1],
#     [2, 2, 2],
#     [2, 2, 4],
#     [2, 3, 5],
#     [2, 4, 3]
# ]

# # Get the results
# results = process_queries(matrix, n, m, queries)

# # Print the results
# for result in results:
#     print(result)


# def max_weight_sum(matrix, n, m, x, y, memo):
#     if x == n - 1 and y == m - 1:
#         return matrix[x][y]

#     if (x, y) in memo:
#         return memo[(x, y)]

#     down_sum = float('-inf')
#     right_sum = float('-inf')

#     if x + 1 < n:
#         down_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x + 1, y, memo)

#     if y + 1 < m:
#         right_sum = matrix[x][y] + max_weight_sum(matrix, n, m, x, y + 1, memo)

#     # Check if down_sum and right_sum are still -inf
#     if down_sum == float('-inf') and right_sum == float('-inf'):
#         # If both are -inf, it means we are at the bottom-right corner
#         return matrix[x][y]
#     elif down_sum == float('-inf'):
#         # If only down_sum is -inf, update it with right_sum
#         down_sum = right_sum
#     elif right_sum == float('-inf'):
#         # If only right_sum is -inf, update it with down_sum
#         right_sum = down_sum

#     memo[(x, y)] = max(down_sum, right_sum)
#     return memo[(x, y)]

# def process_queries(matrix, n, m, queries):
#     results = []
#     memo = {}

#     for query in queries:
#         query_type, x, y = query
#         if query_type == 1:
#             result = max_weight_sum(matrix, n, m, x - 1, y - 1, memo)
#         elif query_type == 2:
#             result = max_weight_sum(matrix, n, m, 0, 0, memo)

#         results.append(result)

#     return results

# # Given input
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
#     [1, 4, 3],
#     [2, 1, 1],
#     [2, 2, 2],
#     [2, 2, 4],
#     [2, 3, 5],
#     [2, 4, 3]
# ]

# # Get the results
# results = process_queries(matrix, n, m, queries)

# # Print the results
# for result in results:
#     print(result)

def max_weight_sum(matrix, n, m, queries):
    dp = [[0] * m for _ in range(n)]

    # Initialize the bottom-right cell
    dp[n-1][m-1] = matrix[n-1][m-1]

    # Initialize the last column
    for i in range(n-2, -1, -1):
        dp[i][m-1] = matrix[i][m-1] + dp[i+1][m-1]

    # Initialize the last row
    for j in range(m-2, -1, -1):
        dp[n-1][j] = matrix[n-1][j] + dp[n-1][j+1]

    # Fill the DP table in a bottom-up manner
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            dp[i][j] = matrix[i][j] + max(dp[i+1][j], dp[i][j+1])

    # Process queries
    results = []
    for query in queries:
        query_type, x, y = query
        if query_type == 1:
            results.append(dp[x-1][y-1])
        elif query_type == 2:
            results.append(dp[0][0])

    return results

# Given input
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
    [2, 3, 5],
    [2, 4, 3]
]

# Get the results
results = max_weight_sum(matrix, n, m, queries)

# Print the results
for result in results:
    print(result)
