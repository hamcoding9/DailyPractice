def solution(price, money, count):
    changes = money-sum(range(price, price*count+1, price))
    return (-1)*changes if changes < 0 else 0
 
# max 함수 사용
def solution(price, money, count):
    changes = money-sum(range(price, price*count+1, price))
    return max(0,(-1)*changes)
