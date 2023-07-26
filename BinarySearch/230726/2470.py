# 230725
# 두용액

n = int(input())
array = list(map(int, input().split()))
array.sort()
num = 1000000000
result = []

for i in range(n):
    for j in range(i+1, n):
        if array[i] + array[j] == 0:
            result.append(array[i])
            result.append(array[j])
            break
        else:
            if abs(array[i]+array[j]) < num:
                result.append(array[i])
                result.append(array[j])
                num = abs(array[i]+array[j])  

length = len(result)

print(result[length-2], result[length-1])