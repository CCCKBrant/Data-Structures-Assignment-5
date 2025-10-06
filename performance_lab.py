# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
def most_frequent(numbers):
    base = 0
    most_frqnt = None
    for x in numbers:
        current_count = numbers.count(x)
        if current_count > base:
            base = current_count
            most_frqnt = x
    return most_frqnt

        

print(most_frequent([1, 3, 2, 3, 4, 1, 3])) 
 

"""
Time and Space Analysis for problem 1:
- Best-case: The first item in the list is the most frequent. O(n)
- Worst-case: All items in the list are unique.O(n)
- Average-case: The more frequent items are somewhere in the middle of the list. O(n)
- Space complexity: O(1) It does not create a new list or stor items in a list, and only uses the numbers provided in the initial function.
- Why this approach? Uses count() which is one of the simple built-in list methods making the code minimal and optimal for smaller lists.
- Could it be optimized? Without imporing other python material, I don't think it can be optimized.

"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for item in nums:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([4, 5, 4, 6, 5, 7]))

"""
Time and Space Analysis for problem 2:
- Best-case: There are no duplicates needing to be removed O(n).
- Worst-case: There are many duplicates needing to be removed O(n^2).
- Average-case: There are few duplicates needing to be removed O(n^2).
- Space complexity: I am creating a list so it would be an O(n) space complexity.
- Why this approach? This approach allows me to removed duplicates, but also keep the same order by using the loop function to make a correctly ordered list.
- Could it be optimized? To my knowledge no, according to ChatGPT it says it is already optimal in terms of Big O.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num,complement))))
        seen.add(num)
    return list(pairs)

print(find_pairs([1, 2, 3, 4], target=5))

"""
Time and Space Analysis for problem 3:
- Best-case: None of the numbers in the list can pair up to make a sum of the target O(n)
- Worst-case: All the numbers in the list can make a pair that adds up to be the target O(n)
- Average-case: Some numbers will form a pair thats sum is the target, and some numbers don't O(n)
- Space complexity: We are creating another list so we can store values that add up to the target, so O(n)
- Why this approach? Most simple and effective way to find the unique pairs, and only runs through the list once.
- Could it be optimized? No, because it is already optimal at O(n).
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    seen = set()
    result = []
    for item in nums:
        current_count = nums.count(item)
        if current_count > base:
            result.append(item + current_count)
    return result
    
print(running_total([1, 2, 3, 4]))

""""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized? 
"""
#I will understand this! 