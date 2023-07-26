#230725
#랜선 자르기

n, k = map(int, input().split())
array = []*1000000

for i in range(n):
    lan = int(input())
    array.append(lan)

#print(array)    
start = 1
end = max(array)
#print(end)

result = 0

while(start <= end):
    div = 0
    mid = (start+end)//2
    for x in array:
        if mid >0:
            div += x //mid
    if div < k:
        end = mid -1
    else:
        result = mid        # 최대값 출력해야 하므로 여기서 result 받음
        start = mid+1
   
print(result)


    