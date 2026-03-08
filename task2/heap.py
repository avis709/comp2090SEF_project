def heap(arr, n, i):
     biggest = i
     l = 2 * i + 1
     r = 2 * i + 2
  
     if l < n and arr[i] < arr[l]:
          biggest = l
  
     if r < n and arr[biggest] < arr[r]:
         biggest = r
  
     if biggest != i:
         arr[i], arr[biggest] = arr[biggest], arr[i]
         heap(arr, n, biggest)
  
  
def heapSort(arr):
     n = len(arr)
  
     for i in range(n//2, -1, -1):
         heap(arr, n, i)
  
     for i in range(n-1, 0, -1):

         arr[i], arr[0] = arr[0], arr[i]
  
         heap(arr, i, 0)
  
  
deafult = [1, 12, 9, 5, 6, 10]
heapSort(deafult)
n = len(deafult)
print("Sorted array is")
for i in range(n):
    print("%d " % deafult[i], end='')
