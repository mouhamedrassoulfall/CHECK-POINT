
#1-recherche binaire

def binary_search(A, l, h, k):
    if h >= l:
        mid = int(l + (h - l)/2)

        if A[mid] == k:
            return print('vrai')
        elif A[mid] > k:
            return binary_search(A, l, mid-1, k)
        else:
            return binary_search(A, mid+1, h, k)
    else:
        return print('faux')

A=[1, 2, 3, 5, 8]
k=5;l=0; h=len(A)-1;
binary_search(A, l, h, k)


#2- a à la puissance b

def puissance(a, b):
    resultat = 1

    for i in range(b):
        resultat *= a

    return resultat

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist


#3-tri à bulle

nlist =  [29,13,22,37,52,49,46,71,56]
print(bubbleSort(nlist))


#4-tri fusion

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)

#5-tri rapide

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29,13,22,37,52,49,46,71,56]
quick_sort(array, 0, len(array) - 1)
print(array)