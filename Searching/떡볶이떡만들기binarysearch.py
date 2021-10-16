n,m = map(int,input().split())
ddk = list(map(int,input().split()))
result = 0
def binary_search(target, start, end):
  while(start <= end):
    mid = (start+end) // 2
    sum = 0
    for i in range(n):
      rest = target[i]-mid
      if(rest<0):
        rest = 0
      sum += rest
    if(sum < m):
      end = mid-1
    else:
      global result
      result = mid
      start = mid+1
      
binary_search(ddk, 0, max(ddk))
print(result)