def count_sort(arr):
    n = len(arr)
    max_ele = max(arr)+1
    count_array = [0]*max_ele

    for ele in arr:
        count_array[ele] += 1
    
    for i in range(1 ,max_ele):
        count_array[i] += count_array[i-1] 
    
    result = [0]*n

    for ele in arr:
        index = count_array[ele] - 1
        result[index] = ele
        count_array[ele] -= 1

    return result

if __name__ == "__main__":
    nums = list(map(int , input().split()))
    nums = count_sort(nums)
    print(nums)

