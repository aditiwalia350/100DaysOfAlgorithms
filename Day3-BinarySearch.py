
def binary_search(A,search,start,end,mid):
    if(A[mid]==search):
        print(mid+1)
        return
    elif(mid==start or mid==end):
        print ("Not found")
        return
    elif(A[mid]>search):
        end=A[mid]
        mid=(start+end)//2
        binary_search(A,search,start,end,mid)
    elif(A[mid]<search):
        start=A[mid]
        mid=(start+end)//2
        binary_search(A,search,start,end,mid)


A=[1,2,3,4,5,6,7,8,9,10]
search=2
start = 0
end = len(A) - 1
mid = (start + end) // 2
binary_search(A,search,start,end,mid)
