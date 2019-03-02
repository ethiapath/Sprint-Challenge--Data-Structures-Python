import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
So the inital aproch is to compare every name in O(n**2)
If we cached the names in one list with a dictionary
and sorted the other list then we could search the second list
with a binary search with O(n log n) time
'''
names_2.sort()
def findDups(cache, listA, listB):
    pass
def binary_search(arr, target):
    if len(arr) == 0:
        return -1 # empty array
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (high+low)//2
        if arr[middle] < target:
        # get RHS
            low = middle+1
        elif arr[middle] > target:
        # get LHS
            high = middle-1
        else:
            return True#middle
    return False # not found

names_in_1 = {}
duplicates = []
for name_1 in names_1:
    if binary_search(names_2, name_1):
        duplicates.append(name_1)
    '''
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
    '''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

