def binarySearch(a, left, right, x):
    if right >= left: 
        mid = (left + right) // 2
        print(mid, left, right)
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binarySearch(a, left, mid - 1, x)
        else:
            return binarySearch(a, mid + 1, right, x)
    else:
        return -1 