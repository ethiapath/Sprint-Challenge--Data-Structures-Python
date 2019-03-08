import time
import sys
sys.path.append('../search')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


#runtime: 0.23628687858581543 seconds
# O( (log n) ^ 2)
bst = BinarySearchTree(names_2.pop())
for name_2 in names_2:
    bst.insert(name_2)

duplicates = []
for name_1 in names_1:
    if bst.contains(name_1): 
        duplicates.append(name_1)


'''
def binary_search(arr, target):
    if len(arr) <= 0:
        print('nope')
        return False
    print('finding ', target, ' on array', len(arr))
    # high = high #len(arr) - 1
    # low = low #0
    high = len(arr) - 1
    low = 0
    middle = high//2#(high-low)//2
    if arr[middle] == target:
        return True
    elif arr[middle] > target:
        # binary_search(arr, middle+1, high, target)
        binary_search(arr[middle+1:high], target)
    else:
        # binary_search(arr, low, middle-1, target)
        binary_search(arr[low:middle-1], target)


names_2.sort()
duplicates = []
for name_1 in names_1:
    if binary_search(names_2, name_1):
        duplicates.append(name_1)
'''

'''
# runtime: 10.018944025039673 seconds
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")