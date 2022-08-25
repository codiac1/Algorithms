def part(a , start , end):
    i = start
    j = end
    pivot = a[start]
    print("asd")
    while(i<j):
        while( i< len(arr) and a[i]<=pivot):
            i+=1
        while( j< len(arr) and a[j]>pivot):
            j-=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
    a[start],a[j] = a[j], a[start]
    return j

def quicksort(a , start , end):
    if(start<end):
        p = part(a, start , end)
        quicksort(a, start, p-1)
        quicksort(a, p+1, end)

arr = [12, 8, 4 ,18 , 76, 34, 23 , 7]
quicksort(arr,0, 7)
print(arr)
