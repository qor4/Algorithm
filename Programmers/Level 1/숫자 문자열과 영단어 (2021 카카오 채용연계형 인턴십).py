def solution(s):
    answer = ""
    alphabet = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5",
                "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tmp = ""
    for i in s:
        tmp += i
        if tmp in alphabet:
            answer += alphabet[tmp]
            tmp = ""
        elif tmp in number:
            answer += tmp
            tmp = ""
    
    answer = int(answer)
    return answer
  
  '''
  number 배열에 담긴 값으로 말고 숫자인지 구분하는 방법은? -> tmp.isdigit(), number를 지우고 elif문을 elif tmp.isdigit()으로 하면 됨.
  int(tmp)는 숫자가 아닐 때는 ValueError 남.
  '''
