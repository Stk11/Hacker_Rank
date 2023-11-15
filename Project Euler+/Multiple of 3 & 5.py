# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23 .

# Find the sum of all the multiples of 3 or 5 below N.

# Input Format

# First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, N .

def total_sum(n):
    n -= 1
    num_threes = n // 3
    num_fives = n // 5
    num_fifteens = n // 15
    
    sum_threes = (num_threes * (num_threes + 1)) // 2  # Using simple method of n(n+1)/2 we could do this
    sum_fives = (num_fives * (num_fives + 1)) // 2
    sum_fifteens = (num_fifteens * (num_fifteens + 1)) // 2 #Since the result will contain multiple of 3 and 5 aka 15 in both output we have to delete the duplicate
    
    total_sum = 3 * sum_threes + 5 * sum_fives - 15 * sum_fifteens
    return total_sum

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    
    print(total_sum(n))