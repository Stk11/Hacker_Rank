# 2. Python: Vending Machine

# Implement class: Vending Machine according to the following requirements:

# • can be instantiated using the constructor Vending Machine num_items, item_price) where num items denotes the number of items in the machine, and item_price denotes the
# required number of coins to buy a single item. has a method buyreq items, money) that represents a buy request where req_items denotes the requested number of items, and 
# money is the amount the customer puts into the machine. Depending on the state of the machine, one of the following happens

# o If there are enough items in the machine to serve the request and the given money is sufficient to buy the requested number of items, the number of items in the machine 
# is reduced by the requested number of items. The method returns an integer denotes the change given back after the purchase. If there are fewer items in the machine than 
# the requested number, it raises a ValueError exception with the message "Not enough items in the machine". If there are enough items in the machine to serve the request
# but the given amount of money is less than their cost. It raises a ValueError exception with the message "Not enough coins".

# The class implementation will be tested by a provided code stub and several input files. Each input file contains parameters to test the implementation. First, the provided 
# code stub initializes an instance of the Vending Machine. Next, it performs the given operations on the Vending Machine instance. The result of their execution will be 
# printed to the standard output by the provided code.

# Constraints

# • There will be at most 100 operations to be performed

# ✓ Input Format Format for Custom Testing

# Input from stdin will be processed as follows and passed to the function.

# In the first line, there are two space-separated integers num_items and item_price denoting the parameters to initialize the Vending Machine. In the second line, there is 
# an integer n denoting the number of operations to be performed on a Vending Machine instance.

# Each of the following n lines contains two space separated integers, num_items and money, that denote a single operation to be performed on the Vending Machine, along with 
# its parameters if any.

# Sample Case 0

# Sample Input 0

# STDIN

# H

# Function

# 10 2 num_items = 10, item_price = 2

# 4

# 15

# →

# n = 4

# req_items = 1, money = 5

# (1st transaction)

# 10 100 ➜ req_items = 10, money = 100 (2nd transaction)

# 7 100

# req_items = 7, money = 100 (3rd transaction)

# 23

# req_items= 2, money = 3

# (4th transaction).

# Sample Output 0

# 3

# Not enough items in the machine.

# 86

# Not enough coins

# ALL

# 1

# 2 N

class VendingMachine:
    
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self,req_items, money):
        self.req_items = req_items
        self.money = money
        # print(num_items,item_price,req_items,money)
        if  self.num_items >= req_items and money >= (req_items*item_price):
            money -= (req_items*item_price)
            self.num_items -= req_items
            return print(money)
        elif money < (req_items*item_price):
            return print("Not enough coins")
        elif req_items >= num_items:
            return print("Not enough items in the machine")
    pass
if __name__ == '__main__':
    num_items, item_price = map(int, input().split())
    machine = VendingMachine(num_items, item_price)

    n = int(input())
    for _ in range(n):
        req_items, money = map(int, input().split())
        try:
            change = machine.buy(req_items, money)
        except ValueError as e:
            print(e)