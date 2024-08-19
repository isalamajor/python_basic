from dlist import DNode
from dlist import DList

# FIND MAXIMUM ELEMENT IN AN ARRAY
a = [1,5,7,9,2,4,5,0,0,2,2,3]
def max_elem(array):
    if len(array) == 1:
        return array[0]
    m = len(array)//2
    m_left = max_elem(array[0:m])
    m_right = max_elem(array[m:])
    return max(m_left, m_right)
#print(max_elem(a))

# FIND NUM IN A SORTED ARRAY
a = [1,3,5,7,8,10,11,14,16,17,29,32]
num = 33
def find_num(array, num):
    m = len(array)//2
    if array[m] == num:
        return True
    if len(array) <= 1:
        return False
    if array[m] > num:
        return find_num(array[0:m], num)
    if array[m] < num:
        return find_num(array[m:], num)
#print(find_num(a, num))

# MERGE-SORT
def merge_sort(array):
    m = len(array)//2
    if len(array) == 1:
        return array
    left = merge_sort(array[0:m])
    right = merge_sort(array[m:])
    aux = []
    for element in right:
        aux.append(element)
    for element in left:
        aux.append(element)
    return aux


#print(merge_sort([1,2,3,4,5,6,7,8]))


# IS X IN SORTED ARRAY??
def search_in_array(array, x):
    if len(array) == 1 and array[0]!= x:
        return False
    m = len(array)//2
    if x > array[m]:
        return search_in_array(array[m:], x)
    if x < array[m]:
        return search_in_array(array[0:m], x)
    return True


#print(search_in_array([1,3,5,6,8,9,10,13,14,20,21], 32))


# PROBLEM 5 - INDEX OF X IN SORTED ARRAY

def array_index(array, x):
    if array is None or len(array) == 0:
        return None
    return _array_index(array, x, 0, len(array)-1)[0]

def _array_index(array, x, start, end):
    if start == end:
        if array[start] == x:
            return [start]
        else:
            return []

    m = (start+end)//2
    left = _array_index(array, x, start, m)
    right = _array_index(array, x, m+1, end)

    return left + right

print(array_index([1, 3, 5, 6, 8, 9, 10, 13, 14, 20, 21], 20))


def arraySorteList(array, x):
    if array is None or len(array) == 0:
        return None
    a = _array_index(array, x, 0, len(array)-1)
    if len(a) != 0:
        return a[0]
    else:
        return None

def _arraySorteList(array, x, start, end):
    if start == end:
        if array[start] == x:
            return start
        else:
            return None

    m = (start + end) // 2
    if array[m] == x:
        return m
    elif array[m] < x:
        return _arraySorteList(array, x, start, m)
    else:
        return _arraySorteList(array, x, m+1, end)


print("ArraySorteList: ", arraySorteList([1, 3, 5, 6, 8, 9, 10, 13, 14, 20, 21], 22))


# MERGE-SORT FOR DLISTS
def d_merge_sort(dlist):
    """The list is first split, then merged"""
    m = dlist.size // 2
    if dlist.size == 1:
        return dlist
    left_list, right_list = divide(dlist)
    left = d_merge_sort(left_list)
    right = d_merge_sort(right_list)
    return merge(left, right)


def merge(dlist1, dlist2):
    """Takes two lists and swaps them so the order is first list2 then list1."""
    aux = DList()
    current2 = dlist2.head
    while current2 is not None:
        aux.addLast(current2.elem)
        current2 = current2.next
    current1 = dlist1.head
    while current1 is not None:
        aux.addLast(current1.elem)
        current1 = current1.next
    return aux

def divide(dlist):
    dlist1 = DList()
    dlist2 = DList()
    i = 0
    current = dlist.head
    while current is not None:
        if i < len(dlist)//2:
            dlist1.addLast(current.elem)
        else:
            dlist2.addLast(current.elem)
        i += 1
        current = current.next
    return dlist1, dlist2


mylist = [0,1,2,3,4,5,6,7,8,9]
myDlist = DList()
for e in mylist:
    myDlist.addLast(e)
print(d_merge_sort(myDlist).__str__())


# QUICK SORT
def _quicksort(data, left, right):
    i = left
    j = right
    m = (left + right) // 2
    p = data[m]  # pivot element in the middle
    if i <= j:  # if left index < right index
        while data[i] < p:
            i += 1
        while data[j] > p:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i] # swap
            i += 1
            j -= 1
    if left < j:  # sort left list
        _quicksort(data, left, j)
    if i < right: # sort right list
        _quicksort(data, i, right)

def quicksort(data):
    return _quicksort(data, 0, len(data) - 1)

print("Quicksort: ", quicksort([9,7,6,4,3,2,1,0]))