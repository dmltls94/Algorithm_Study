#이진탐색 반복문
n, k = map(int,input().split())

array = list(map(int,input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if(array[mid]==target):
      return mid
    elif(array[mid]<target):
      start = mid+1
    else:
      end = mid-1
  return None

print(binary_search(array,k,0,n-1))