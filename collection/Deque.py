# Import collections module:
from collections import deque

# Initialize deque:
dq = deque({4: 'harini', 5: 'moni', 6: 'siva'})

# Append to the right:
dq.append({7: 'priya'})
print("Append 7 to the right: ", list(dq))

# Append to the left:
dq.appendleft(3)
print("Append 3 to the left: ", list(dq))

# Append multiple values to right:
dq.extend([8, 9, 10])
print("Append 8, 9 and 10 to the right: ", list(dq))

# Append multiple values to left:
dq.extendleft([1, 2])
print("Append 2 and 1 to the left: ", list(dq))

# Insert -1 at index 5
dq.insert(5, -1)
print("Insert -1 at index 5: ", list(dq))

# Pop element from the right end:
dq.pop()
print("Remove element from the right: ", list(dq))

# Pop element from the left end:
dq.popleft()
print("Remove element from the left: ", list(dq))

# Remove -1:
dq.remove(-1)
print("Remove -1: ", list(dq))

# Count the number of times 5 occurs:
i = dq.count(5)
print("Count the number of times 5 occurs: ", i)

# Return index of '7' if found between index 4 and 6:
# i = dq.index(7, 4, 6)
# print("Search index of number 7 between index 4 and 6: ", i)

# Rotate the deque three times to the right:
dq.rotate(3)
print("Rotate the deque 3 times to the right: ", list(dq))

# Reverse the whole deque:
dq.reverse()
print("Reverse the deque: ", list(dq))

# from collections import deque
#
# a = deque()
# val = int(input('Enter the input : '))
# comment = input("Enter append to add the value to the last \nEnter anything to add values to first of list")
# for i in range(val):
#     if comment.lower() == 'append':
#         a.append(i)
#     elif comment.lower() == 'appendleft':
#         a.appendleft(i)
#
# print(a)



