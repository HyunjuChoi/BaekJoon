# 230725
# 숫자 카드

def find_card(card, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if card[mid] == target:
        return 1
    elif card[mid] > target:
        return find_card(card, target, start, mid-1)
    else:
        return find_card(card, target, mid+1, end)
    

n = float(input())
n = int(n)
card = list(map(int, input().split()))
card.sort()

m = int(input())
array = list(map(int, input().split()))


for target in array:
    for _ in range(n):
        print(find_card(card, target, 0, n-1), end=' ')
        break
