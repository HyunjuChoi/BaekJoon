# 230725
# 두용액

n = int(input())
array = list(map(int, input().split()))
array.sort()

start = 0
end = n-1
ans = abs(array[start] + array[end])

res_arr = [array[start], array[end]]

while(start < end):
    num1 = array[start]
    num2 = array[end]
    
    result = num1 + num2
    
    if abs(result) < ans:
        ans = abs(result)
        res_arr = [num1, num2]      
    if result == 0:
        break
    elif result > 0:
        end -=1
    else:
        start +=1
    
print(res_arr[0], res_arr[1])        
    