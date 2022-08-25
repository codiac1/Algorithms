def heapify(arr , i , n):
  left = 2*i + 1
  right = 2*i + 2
  largest = i
  
  if left < n and arr[largest] < arr[left]:
    largest = left
  if right < n and arr[largest] < arr[right]:
    largest = right
    
  if largest != i :
    arr[largest] , arr[i] = arr[i] , arr[largest]
    heapify(arr, largest  , n)

def build_heap(arr):
  n = len(arr)
  for i in range(n//2 , -1, -1):
    heapify(arr , i , n)
    
  for i in range(n-1 , -1 ,-1):
    arr[0] , arr[i] = arr[i] , arr[0]
    heapify(arr ,0 , i)
    
def heap_sort(arr):
  build_heap(arr)
  return arr

arr = [7,2,10,5,1,8,3,6]
print(heap_sort(arr))
