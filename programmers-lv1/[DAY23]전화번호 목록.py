# 1차 시도: 효율성 테스트 실패
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for num in phone_book[i+1:]:
            if phone_book[i] == num[:len(str(phone_book[i]))]:
                return False
    return True
  
# 2차 : 속도 개선을 위해 dictionary 사용
def solution(phone_book):
    numbers = {}
    for num in phone_book:
        numbers[num] = 1
    for num in phone_book:
        temp = ""
        for digit in num:
            temp += digit
            if temp in numbers and temp != num:
                return False
    return True
