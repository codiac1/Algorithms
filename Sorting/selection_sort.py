def selection_sort(self, arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

if __name__ == "__main__":
    nums = list(map(int , input().split()))
    nums = selection_sort(nums)
    print(nums)