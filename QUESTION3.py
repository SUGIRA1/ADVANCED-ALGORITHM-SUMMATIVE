def find_expensive_item(prices, budget):
    total = 0
    for i, price in enumerate(prices):
        if budget - total < price:
            return i
        else:
            total += price
    return -1  # return -1 if no item is found

# Test case 1
prices1 = [10, 20, 30, 40, 50]
budget1 = 100
result1 = find_expensive_item(prices1, budget1)
if result1 == -1:
    print("No item found within budget")
else:
    print("Item found at index:", result1)

# Test case 2
prices2 = [5, 10, 15, 20, 25]
budget2 = 18
result2 = find_expensive_item(prices2, budget2)
if result2 == -1:
    print("No item found within budget")
else:
    print("Item found at index:", result2)
