def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for k in range(len(phone_book[i])):
            if phone_book[i][k] != phone_book[i+1][k]:
                break
        else:
            answer = False
            return answer
    return answer
