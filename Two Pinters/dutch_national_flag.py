def dutch_national_flag(arr):
    low =0
    ptr = 0
    high = len(arr)-1
    while(ptr<high):
        if arr[ptr] == 0:
            arr[low] , arr[ptr] = arr[ptr], arr[low]
            low +=1
            ptr+=1
        elif arr[ptr] == 1:
            ptr+=1
        else:
            arr[ptr] , arr[high] = arr[high], arr[ptr]
            high -=1
    return arr

arr = [2,0,0,1,2,0,1,0,1,2]
print(dutch_national_flag(arr))
            
            
            
