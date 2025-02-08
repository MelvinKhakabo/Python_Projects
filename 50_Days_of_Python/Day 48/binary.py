#Write a function called search_binary that searches for the number 
#22 in the following list and returns its index. The function should take 
#two parameters, the list and the item that is being searched for. Use 
#binary search (iterative Method).

def search_binary(lst, item):
    lst.sort()
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return "Item not found"

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search_binary(lst, 22))