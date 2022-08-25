def bubble_sort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
                        
        return arr
if __name__ == "__main__":
    nums = list(map(int , input().split()))
    nums = bubble_sort(nums)
    print(nums)