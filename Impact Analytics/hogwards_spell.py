# # def construct_sequence(t, test_cases):
# #     result = []

# #     for case in test_cases:
# #         n = case
# #         spells_used = []

# #         for i in range(40, 0, -1):  # Iterate from 40 to 1
# #             if n % 2 == 0 and n >= 2 ** (i - 1):
# #                 spells_used.append(1)
# #                 n //= 2
# #             elif n % 2 == 1 and n > 1:
# #                 spells_used.append(2)
# #                 n = (n - 1) // 2
# #             else:
# #                 spells_used = []
# #                 break

# #             if n == 1:
# #                 spells_used.append(1)
# #                 break

# #         if not spells_used or n != 1:
# #             result.append((-1,))
# #         else:
# #             result.append((len(spells_used), spells_used[::-1]))

# #     return result


# # # Sample Input
# # t = 4
# # test_cases = [2, 3, 7, 17]

# # # Output
# # results = construct_sequence(t, test_cases)
# # for result in results:
# #     if result[0] == -1:
# #         print(-1)
# #     else:
# #         print(result[0])
# #         print(*result[1])

# class Node:
#     def __init__(self, value, spells_used=None):
#         self.value = value
#         self.spells_used = spells_used if spells_used is not None else []

# def construct_sequence(n):
#     root = Node(1)
#     queue = [root]

#     while queue:
#         current_node = queue.pop(0)

#         # Try using the first spell "2x - 1"
#         spell_1_result = Node(2 * current_node.value - 1, current_node.spells_used + [1])
#         if spell_1_result.value == n:
#             return (len(spell_1_result.spells_used), spell_1_result.spells_used[::1])
#         elif spell_1_result.value < n and len(spell_1_result.spells_used) <= 40:
#             queue.append(spell_1_result)

#         # Try using the second spell "2x + 1"
#         spell_2_result = Node(2 * current_node.value + 1, current_node.spells_used + [2])
#         if spell_2_result.value == n:
#             return (len(spell_2_result.spells_used), spell_2_result.spells_used[::1])
#         elif spell_2_result.value < n and len(spell_2_result.spells_used) <= 40:
#             queue.append(spell_2_result)

#     return (-1,)

# # Sample Input
# t = int(input())
# test_cases = []
# for i in range(t):
#     n = int(input())
#     test_cases.append(n)

# # Output
# for n in test_cases:
#     result = construct_sequence(n)
#     if result[0] == -1:
#         print(-1)
#     else:
#         print(result[0])
#         print(*result[1])

class Node:
    def __init__(self, value, spells_used=None):
        self.value = value
        self.spells_used = spells_used if spells_used is not None else []

def construct_sequence(n):
    if n%2 ==0:
        return (-1,)
    root = Node(1)
    queue = [root]

    while queue:
        current_node = queue.pop(0)

        # Try using the first spell "2x - 1"
        spell_1_result_value = 2 * current_node.value - 1
        if spell_1_result_value == n:
            return (len(current_node.spells_used) + 1, current_node.spells_used + [1])
        elif spell_1_result_value < n and len(current_node.spells_used) < 40:
            spell_1_result = Node(spell_1_result_value, current_node.spells_used + [1])
            queue.append(spell_1_result)

        # Try using the second spell "2x + 1"
        spell_2_result_value = 2 * current_node.value + 1
        if spell_2_result_value == n:
            return (len(current_node.spells_used) + 1, current_node.spells_used + [2])
        elif spell_2_result_value < n and len(current_node.spells_used) < 40:
            spell_2_result = Node(spell_2_result_value, current_node.spells_used + [2])
            queue.append(spell_2_result)

    return (-1,)

# Example Usage


test_cases = [2, 3, 7, 17]
for n in test_cases:
    result = construct_sequence(n)
    if result[0] == -1:
        print(-1)
    else:
        print(result[0])
        print(*result[1])


